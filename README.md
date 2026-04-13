# 🚀 Completcha

Python library for solving **Arkose Labs / FunCaptcha** challenges, built to deliver **high success rates, speed, and real-world reliability in production**.

### [Free trial for new users on completcha.com](https://completcha.com)

Unlike traditional approaches, **Completcha** was designed to solve the most common problems faced when dealing with captchas:

- ❌ Challenges that never get solved  
- ⏳ Long waiting times for responses  
- 🔁 Constant need to generate new captcha URLs  
- 🚫 Limited attempts per challenge  

---

## 💡 Key Advantages

### 🚀 Bypass Resolution (Main Advantage)

The biggest advantage of Completcha is its **full Arkose bypass capability**.

- Most challenges are solved **without requiring image solving**
- The system accurately replicates real browser behavior
- This results in:
  - ⚡ Much faster responses  
  - 🎯 Extremely high success rates  
  - 🔄 Reduced need to generate new challenges  

👉 In practice, this eliminates the most frustrating issue: waiting for a captcha that often never gets solved.

---

### 🖼️ Image Solving with Smart Retries

When bypass is not possible (e.g., using rotating proxies), Completcha still stands out:

- 🔁 Performs **all necessary retries automatically**
- 🧠 Designed to handle harder image challenges
- 📉 Significantly reduces failure rates
- ♻️ Avoids the need to generate new captcha URLs

Additionally:

- Full integration with Arkose's original flow ensures:
  - Fewer images are generated
  - Behavior closely matches a real browser

👉 Result: **one of the highest solving success rates on the market**, even in difficult scenarios.

---

## 📦 Installation

```bash
pip install completcha
```

---

## 🔐 Solving Methods

**Completcha** provides two main methods for solving Arkose challenges:

---

### 🚀 1. Bypass (Recommended)

The fastest and most reliable method.

**How it works:**
- The Arkose challenge URL must be requested using a **fixed proxy**
- The solution is executed on the **same IP as the request**
- No images need to be solved

**Advantages:**
- ⚡ High speed  
- 🎯 Maximum reliability  
- 🧠 No image solving required  

⚠️ **Important:**
- Use **fixed (dedicated) proxies**
- **Do NOT use sticky proxies**

> ❗ Sticky proxies will change IP addresses because they depend on the same source IP address to remain static since your source IP address is different from ours in the resolution side.

---

### 🖼️ 2. Image Solving

Used when bypass is not possible.

**When it happens:**
- When using **rotating proxies**
- The request IP differs from the solving IP

**Features:**
- 🧩 Automatically solves any image challenge  
- 📊 Real-time logs for tracking progress  

---

## ⚙️ Best Practices

- ✅ Use the **same User-Agent** from the original request  
- ♻️ Reuse the same API instance (avoids rate limiting)  
- 🔒 Prefer fixed proxies for best performance  

---

## 💻 Example Usage

```python
from completcha import SolverApi

# Instantiate only once to maintain same completcha session to avoid rate limit
completcha_session = SolverApi(
    api_key='xxx-xxxx-xxx-xxx-xxxx-xxx',
    show_logs=True
)

arkose_data = 'Q9xL2mVtF8yZk/rW.JpG4aH6uSnoqLDEBvCwR5Xf3sYt0ZlN8Peu/jK3qTz7rVbA1MHi9UdWcE2Ox+gFJYnKsL0QpR4t6BvXy7zN5hMeCq8GjAfD3uWPlZrT1n/SoIkVxYcE2mH7F9QaUpbXgRZK5V3nTtLj8wQh4Gv0p2fMsYkJ6CDeaI1Xo7r8s9NwBtU5lE3ZcHyPgQfO2uV1dKjSxA7mW9bL0FvRzJq6YH3XcD8tUpnK5wIeM4aG2ZQh7sVb9C0fYkT1xP8LrNwD3mE6uJgS2AqXv5oFz+HyR8c7LkW9p0VJtN3ZbGdE6xF2aQs8UoYhP1rM4iTnK7wC5vLzX9qD2jH0BfE3R6gPZs1yN4t8uAqI5WcKXoM7dVhFzYJ2bL9xC6rT3gUpvSnQ0='
proxy = 'proxyusername:proxypassword@proxyhost:proxyport'
site_key = '2CB16598-CB82-4CF7-B332-5990DB66F3AB'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'

solved_token_arkose = completcha_session.arkose(
    arkose_data,
    proxy,
    site_key,
    user_agent
)
```

### Return Solved Token
```
70103a5dafe122e18.1833610001|r=us-east-1|meta=3|meta_width=558|meta_height=523|metabgclr=transparent|metaiconclr=%23555555|guitextcolor=%23000000|pk=2CB16598-CB82-4CF7-B332-5990DB66F3AB|at=30|ag=201|cdn_url=https%3A%2F%2Fclient-api.arkoselabs.com%2Fcdn%2Ffc|surl=https%3A%2F%2Fclient-api.arkoselabs.com|smurl=https%3A%2F%2Fclient-api.arkoselabs.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager
```
---

## ⭐ Method Comparison

| Method              | Speed     | Reliability |
|--------------------|----------|------------|
| 🚀 Bypass          | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 🖼️ Image Solving   | ⭐⭐⭐⭐   | ⭐⭐⭐⭐   |

---

## 🏆 Final Recommendation

- 🚀 **Bypass** → ⭐⭐⭐⭐⭐ (Best overall choice)  
- 🖼️ **Image** → ⭐⭐⭐⭐  

✔ Always prefer **bypass with fixed proxies** for optimal performance.

---

## 💬 Community & Support

<p align="center">
  <a href="https://discord.gg/cdgHgF2ySG">
    <img src="https://img.shields.io/badge/Join%20our%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord">
  </a>
</p>

<p align="center">
Join the community for support, updates, and discussions 🚀
</p>
