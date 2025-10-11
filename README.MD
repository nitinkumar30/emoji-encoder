# 🧠 **Emoji Encoder Automation — Test Framework**

![GitHub Actions](https://img.shields.io/github/actions/workflow/status/nitinkumar30/emoji-encoder/deploy.yaml?label=GitHub%20Actions&logo=github)
![Latest Commit](https://img.shields.io/github/last-commit/nitinkumar30/emoji-encoder?color=green)

Welcome to **Emoji Encoder Automation**, an end-to-end **Python + Selenium** automation framework 🧩 built to test the functionality of the [Emoji Encoder Web App](https://emojiencoder.netlify.app/).
It ensures the app correctly **encodes** and **decodes** secret text using emojis 🔐.

---

## 🏗️ **Project Overview**

| Feature                  | Description                                |
| ------------------------ | ------------------------------------------ |
| 🚀 **Framework Type**    | UI Test Automation Framework               |
| 🧰 **Core Stack**        | Python, Selenium, Pytest                   |
| 🧪 **Reporting**         | Custom HTML + Allure + Logs + Screenshots  |
| 🪄 **Design Pattern**    | Page Object Model (POM)                    |
| 🧭 **Browser Support**   | Google Chrome (Headless / UI mode)         |
| 📂 **Reports Generated** | Screenshots, logs, and custom HTML summary |

---

## ⚙️ **Project Structure**

```
emoji_encoder_automation/
│
├── pages/                    # All Page Object Model (POM) classes
│   └── emoji_encoder_page.py
│
├── tests/                    # Test files
│   └── test_emoji_encoder.py
│
├── utils/                    # Helper utilities, logging, and reporting
│   ├── driver_factory.py
│   ├── helper.py
│   ├── transform_report.py   # Custom HTML report generator
│   └── custom_report.html    # Jinja2 template for HTML report
│
├── reports/                  # Generated screenshots, logs & reports
│   ├── screenshots/
│   ├── logs/
│   └── final_report_*.html
│
└── conftest.py               # Pytest setup & teardown configuration
```

---

## 💡 **Key Highlights**

### 🧱 Page Object Model (POM)

The framework follows the **POM pattern** for modularity:

* Each page action (click, input, copy, paste, etc.) is wrapped inside reusable methods.
* Decorated with `@screenshot_step` to automatically capture step-wise screenshots 📸.

---

### 🧪 Pytest-Based Automation

Run tests using:

```bash
pytest -v --json-report \
  --json-report-file=emoji_encoder_automation/reports/pytest_report.json
```

✔ Automatically opens Chrome in headless mode
✔ Captures screenshots at each logical step
✔ Logs every XPath, action, and timestamp
✔ Generates a **fully styled HTML report**

---

### 🧾 Custom HTML Reporting ✨

A dynamic, visually rich HTML report is generated post execution:

* ✅ Step-wise results (Pass / Fail)
* 📸 Linked screenshots for every action
* 🕒 Execution time for each step
* 🧩 XPaths used during element interaction
* 🧱 System + Config details (browser, OS, Python)
* 🌙 Light / Dark theme toggle

**Report Example Path:**

```
emoji_encoder_automation/reports/final_report_2025xxxx_xxxxxx.html
```

**Custom report generator:**
`emoji_encoder_automation/utils/transform_report.py`
uses Jinja2 templates to create a modern, client-friendly layout.

---

### 🗂️ Logs & Screenshots

| Folder                     | Description                                 |
| -------------------------- | ------------------------------------------- |
| 🧾 `reports/logs/`         | All runtime logs with timestamps and status |
| 🖼️ `reports/screenshots/` | Captured after every significant step       |
| 🧠 `pytest_report.json`    | Intermediate JSON used to create HTML       |

**Example Log Path:**

```
emoji_encoder_automation/reports/logs/test_log_20251010_202628.log
```

---

### 🧰 Setup & Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/emoji_encoder_automation.git
   cd emoji_encoder_automation
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # (Windows)
   source .venv/bin/activate   # (Mac/Linux)
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the tests**

   ```bash
   pytest -v
   ```

5. **Generate the custom report**
   The report is automatically created post-test in:

   ```
   emoji_encoder_automation/reports/
   ```

---

## 🌈 **Advanced Features**

### 🧠 Smart Screenshot Decorator

Each step in the test is automatically captured with:

```python
@screenshot_step("Step Description")
```

This provides better debugging and visual validation.

---

### 🪶 Logging

The `setup_logger()` method records every test step with timestamps:

```
[INFO] 2025-10-11 21:36:58 - Opening Emoji Encoder page
[PASS] 2025-10-11 21:36:59 - Encoder switch clicked
```

---

### 🕵️‍♂️ Failure Handling

* Screenshots are attached automatically for **failed steps**.
* Failure reason & traceback are clearly logged in the HTML report.

---

## 🌍 **Customization**

You can easily modify:

* **Theme toggle** (🌙 Dark / ☀️ Light)
* **Report title / company logo**
* **Additional metadata** (e.g. project, module, version)
* **Chart.js summary** (Pass/Fail distribution pie chart)

Edit:

```
utils/transform_report.py
utils/custom_report.html
```

---

## 🧑‍💻 **Tech Stack**

| Category    | Tools Used                   |
| ----------- | ---------------------------- |
| Language    | 🐍 Python 3.11+              |
| Test Runner | 🧪 Pytest                    |
| Automation  | 🧭 Selenium WebDriver        |
| Reporting   | 🪄 Jinja2, Pytest-HTML, JSON |
| Logging     | 📜 Python logging module     |
| Utilities   | ⏱ Pyperclip, datetime        |

---

## 🧩 **Future Enhancements**

* 📊 Add interactive charts (Pass/Fail trend)
* ☁️ Integrate with CI/CD (GitHub Actions / Jenkins)
* 🔔 Slack / Email notifications for reports
* 🧾 Export report as PDF

---

## 🏁 **Conclusion**

This framework transforms ordinary Selenium automation into a **complete client-facing test solution** — combining:

✅ **Code structure**
✅ **Visual reporting**
✅ **Traceable logs**
✅ **Error transparency**

> 💬 “A test is not complete until it tells its story — visually, clearly, and confidently.”

---

### ❤️ Credits

* Built by: **Nitin Kumar**
* Guided by: *ChatGPT (GPT-5)*
* Framework: **Emoji Encoder Automation Project**
* Year: **2025**

---

# 😎 Author

[Nitin Kumar](https://linkedin.com/in/nitin30kumar/)

