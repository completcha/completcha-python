import requests
from requests.exceptions import HTTPError, ConnectTimeout
import time
import random
from completcha.logger_print import SimpleLogger
from completcha.exceptions import *


class SolverApi:
    def __init__(self, api_key: str, show_logs: bool = False):
        self._show_log: bool = show_logs
        self._apikeycompletcha: str = api_key
        if self._show_log:
            self._log = SimpleLogger(level=SimpleLogger.DEBUG, name='COMPLETCHA')
        else:
            self._log = SimpleLogger(level=SimpleLogger.DISABLED)
        self.session = requests.session()

    @staticmethod
    def _verify_new_update(json_response):
        detail = json_response.get('detail') or []
        if (
                isinstance(detail, list) and
                len(detail) > 0 and
                isinstance(detail[0], dict) and
                detail[0].get("type") == "missing" and
                isinstance(detail[0].get("loc"), list) and
                len(detail[0]["loc"]) > 0 and
                detail[0]["loc"][0] == "body"
        ):

            raise DeprecatedLibrary(f"New parameter \033[31;4m{detail[0]["loc"][1]}\033[0m required in the payload. Update to the latest version of the completcha library.")

    def _request_with_retry(self, func, max_retries=5, base_delay=1):
        for attempt in range(1, max_retries + 1):
            try:
                return func()

            except ConnectTimeout as err:
                delay = base_delay * (2 ** (attempt - 1))
                jitter = random.uniform(0, 0.5)
                final_delay = delay + jitter

                self._log.warning(
                    f"Attempt {attempt}/{max_retries} to connect to the server failed: {err} | waiting {final_delay:.2f}s"
                )

                time.sleep(final_delay)

        raise MaxRetriesServerExceeded("Maximum number of attempts to connect to the server reached")

    def arkose(self, arkose_data_blob: str, proxy: str, public_key: str, user_agent: str | None = None) -> str:
        """
        Creates an Arkose resolution task and returns the resolved token.

        Args:
            arkose_data_blob (str): Parameter data blob.
            proxy (str): Proxy in the format username:password@host:port.
            public_key (str): The public key.
            user_agent (str, optional): The User-Agent to be used. Defaults to None.

        Returns:
            str: The resolved challenge token.
        """
        if not self._apikeycompletcha or not isinstance(self._apikeycompletcha, str):
            raise MissingApiKey(
                "Invalid configuration: 'SolverApi()._apikeycompletcha' must be set to a valid string API key before calling SolverApi methods.")

        root_path = 'arkose_token'
        payload_create_task = {"datablob": arkose_data_blob, "user_agent": user_agent, "proxy": proxy,
                               "public_key": public_key}

        create_task_url = f'https://api.completcha.com/{root_path}/task/create'
        get_status_url = f'https://api.completcha.com/{root_path}/task/status/'

        headers_solver = {'x-api-key': self._apikeycompletcha}

        def post_request(url, payload):
            return self._request_with_retry(lambda: self.session.post(
                url,
                headers=headers_solver,
                json=payload
            ))

        def get_request(url: str, task_id_passed: str):
            return self._request_with_retry(lambda: self.session.get(
                url + task_id_passed,
                headers=headers_solver
            ))

        # Criar Tarefa
        name_show = 'Arkose'
        print(f"Requesting {name_show} Token in Completcha Solver ...")
        response_create_task = post_request(create_task_url, payload_create_task)
        status_response_create_task = response_create_task.status_code
        text_response_create_task = response_create_task.text
        self._log.debug(f"Status: {status_response_create_task}, Text: {text_response_create_task} ...")

        try:
            response_create_task.raise_for_status()
        except HTTPError as e:
            if e.response.status_code == 422:
                if "application/json" in e.response.headers.get("Content-Type", ""):
                    json_error_res = e.response.json()
                    self._verify_new_update(json_error_res)
            raise ServerError(
                f'Error when trying to create a task >>\nStatus Code Error: {e.response.status_code}, Response: {e.response.text}')

        json_response_create_task = response_create_task.json()
        task_id = json_response_create_task["task_id"]

        print_result = None
        # Aguardar Resolução
        while True:
            response_status_resolution = get_request(get_status_url, task_id)
            text_response_status_resolution = response_status_resolution.text

            if not print_result == text_response_status_resolution:
                print_result = text_response_status_resolution
                self._log.debug(f"{print_result} ...")

            try:
                response_status_resolution.raise_for_status()
            except HTTPError as e:
                raise ServerError(
                    f'Error when trying to get the task response >>\nStatus Code Error: {e.response.status_code}, Response: {e.response.text}')

            json_response_status_resolution = response_status_resolution.json()
            if json_response_status_resolution['status'] == 'completed':
                token_solved = json_response_status_resolution['result']
                print(f"{name_show} challenge completed", token_solved)
                return token_solved
            elif json_response_status_resolution['status'] == 'failed':
                raise SolverApiError(f"Error in {name_show} challenge solution: {json_response_status_resolution['result']}")
            elif json_response_status_resolution['status'] in ('in resolution', 'pending'):
                time.sleep(1.2)
            else:
                raise ProgrammerError(
                    f"The response status does not match any programmed criteria: {json_response_status_resolution}")


if __name__ == '__main__':
    breakpoint()
