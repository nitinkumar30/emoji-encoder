import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def wait_for_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

def take_screenshot(driver, name):
    """Save screenshot in /reports/screenshots/."""
    screenshots_dir = os.path.join(os.getcwd(), "reports", "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(path)
    return path

def screenshot_step(step_name):
    """Decorator for auto screenshots at each page action."""
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            take_screenshot(self.driver, step_name.replace(" ", "_"))
            return result
        return wrapper
    return decorator
