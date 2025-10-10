import pytest
from emoji_encoder_automation.utils.driver_factory import get_driver
from emoji_encoder_automation.pages.emoji_encoder_page import EmojiEncoderPage
from emoji_encoder_automation.utils.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture(scope="module")
def setup_teardown():
    driver = get_driver()
    logger.info("🚀 Test session started. Driver initialized.")
    yield driver
    driver.quit()
    logger.info("🧹 Test session completed. Driver closed.")

def test_encode_decode(setup_teardown):
    driver = setup_teardown
    page = EmojiEncoderPage(driver)
    secret_text = "This is my secret text."

    logger.info("========== TEST START: Encode → Decode Flow ==========")
    page.open()
    page.click_encoder_switch()
    page.enter_secret_text(secret_text)
    page.select_emoji()

    encoded_text = page.copy_output_text()
    page.click_encoder_switch()
    page.enter_text(encoded_text)

    decoded_text = page.get_decoded_text()

    logger.info(f"🔍 Verifying decoded text matches input: '{decoded_text}' == '{secret_text}'")
    assert decoded_text.strip() == secret_text.strip(), "❌ Decoded text does not match the input text."
    logger.info("✅ Text validation successful.")
    logger.info("========== TEST END ==========")
