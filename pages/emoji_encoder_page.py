import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from emoji_encoder_automation.utils.helper import wait_for_element, wait_for_clickable, screenshot_step
from emoji_encoder_automation.utils.logger import get_logger
import pyperclip

logger = get_logger(__name__)

class EmojiEncoderPage:
    URL = "https://emojiencoder.netlify.app/"
    MODE_SWITCH = (By.XPATH, "//input[@id='mode-switch']")
    TEXT_INPUT = (By.XPATH, "//textarea[@id='text-input']")
    EMOJI_PICKER = (By.XPATH, "(//div[@id='emoji-picker']/*)[1]")
    OUTPUT_TEXTAREA = (By.XPATH, "//textarea[@id='output']")

    def __init__(self, driver):
        self.driver = driver

    @screenshot_step("Open Page")
    def open(self):
        logger.info(f"Opening URL: {self.URL}")
        self.driver.get(self.URL)
        logger.info("✅ Page opened successfully.")

    @screenshot_step("Click Encoder Switch")
    def click_encoder_switch(self):
        logger.info("Attempting to click encoder/decoder switch.")
        element = wait_for_clickable(self.driver, self.MODE_SWITCH)
        try:
            element.click()
            logger.info("✅ Clicked encoder/decoder switch successfully.")
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)
            logger.warning("⚠️ Fallback to JS click due to interception.")
        time.sleep(1)

    @screenshot_step("Enter Secret Text")
    def enter_secret_text(self, secret_text):
        logger.info(f"Entering secret text: {secret_text}")
        text_area = wait_for_element(self.driver, self.TEXT_INPUT)
        text_area.clear()
        text_area.send_keys(secret_text)
        logger.info("✅ Secret text entered successfully.")

    @screenshot_step("Pick Emoji")
    def select_emoji(self):
        logger.info("Selecting first emoji from the list.")
        emoji = wait_for_clickable(self.driver, self.EMOJI_PICKER)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", emoji)
        emoji.click()
        logger.info("✅ Emoji selected.")
        time.sleep(0.5)

    @screenshot_step("Copy Encoded Output")
    def copy_output_text(self):
        logger.info("Copying encoded text using CTRL+A and CTRL+C.")
        output_area = wait_for_element(self.driver, self.OUTPUT_TEXTAREA)
        output_area.send_keys(Keys.CONTROL, 'a')
        output_area.send_keys(Keys.CONTROL, 'c')
        encoded = output_area.get_attribute('value')
        logger.info(f"✅ Encoded text copied: {encoded[:60]}...")  # Limit log length
        return encoded

    @screenshot_step("Paste Encoded Text")
    def paste_text(self, text):
        logger.info("Pasting encoded emoji text back into input field.")
        input_area = wait_for_element(self.driver, self.TEXT_INPUT)
        input_area.clear()
        input_area.send_keys(text)
        logger.info("✅ Text pasted successfully.")

    @screenshot_step("Enter Decoded Text")
    def enter_text(self, text):
        logger.info("Entering (or pasting) text with emoji support.")
        input_area = wait_for_element(self.driver, self.TEXT_INPUT)
        input_area.clear()

        if any(ord(ch) > 0xFFFF for ch in text):
            logger.info("Detected emoji/non-BMP text; using clipboard paste.")
            pyperclip.copy(text)
            input_area.click()
            input_area.send_keys(Keys.CONTROL, 'v')
        else:
            input_area.send_keys(text)
        logger.info("✅ Text entered successfully.")

    @screenshot_step("Get Decoded Output")
    def get_decoded_text(self):
        logger.info("Retrieving decoded text from output field.")
        decoded = wait_for_element(self.driver, self.OUTPUT_TEXTAREA).get_attribute('value')
        logger.info(f"✅ Decoded text retrieved: {decoded[:60]}...")
        return decoded
