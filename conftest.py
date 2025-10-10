import os
import pytest
from datetime import datetime
from markupsafe import escape
from emoji_encoder_automation.utils.helper import take_screenshot

REPORT_DIR = os.path.join(os.getcwd(), "reports")
SCREENSHOT_DIR = os.path.join(REPORT_DIR, "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# ---------------- HTML REPORT CONFIG ---------------- #
def pytest_configure(config):
    """Configure HTML report and metadata."""
    report_name = f"emoji_encoder_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    report_path = os.path.join(REPORT_DIR, report_name)

    config.option.htmlpath = report_path
    config.option.self_contained_html = True

    # Add nice metadata
    if not hasattr(config, "_metadata"):
        config._metadata = {}
    config._metadata.update({
        "Project Name": "Emoji Encoder Automation",
        "Module": "Encode/Decode Validation",
        "Tester": "Automation Framework",
        "Browser": "Chrome (Auto-managed)",
        "Execution Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def pytest_html_report_title(report):
    report.title = "✨ Emoji Encoder Automation Test Report"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "<h2>🎯 Project Summary</h2>",
        "<p>This report validates the encode/decode flow on the Emoji Encoder web app.</p>",
        "<p>All actions are logged and screenshots are captured automatically for every step.</p>"
    ])

def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Description</th>")
    cells.insert(2, "<th>Screenshot</th>")
    cells.pop()

def pytest_html_results_table_row(report, cells):
    description = getattr(report, "description", "N/A")
    screenshot_link = getattr(report, "screenshot", None)
    screenshot_html = (
        f'<a href="{escape(screenshot_link)}" target="_blank">View</a>'
        if screenshot_link else "N/A"
    )
    cells.insert(1, f"<td>{escape(description)}</td>")
    cells.insert(2, f"<td>{screenshot_html}</td>")
    cells.pop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot and attach to pytest-html report."""
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    driver = item.funcargs.get("setup_teardown", None)
    if driver and report.when == "call":
        screenshot_name = f"{item.name}_{report.outcome}_{datetime.now().strftime('%H%M%S')}.png"
        screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)
        take_screenshot(driver, screenshot_name)

        if os.path.exists(screenshot_path):
            # Attach clickable thumbnail
            html_img = (
                f'<div><a href="screenshots/{screenshot_name}" target="_blank">'
                f'<img src="screenshots/{screenshot_name}" '
                f'style="width:320px;height:180px;border-radius:8px;box-shadow:0 0 5px #999;"></a></div>'
            )
            extra.append(pytest.html.extras.html(html_img))
            report.screenshot = f"screenshots/{screenshot_name}"

    report.extra = extra

# Optional: color-coding
def pytest_html_results_table_html(report, data):
    color = (
        "#e8f5e9" if report.passed else
        "#ffebee" if report.failed else
        "#fffde7"
    )
    data.append(f'<style>tr.result-{report.outcome} {{ background-color: {color}; }}</style>')
