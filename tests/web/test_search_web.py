import allure
import time

@allure.title("[Web] Playwright 사이트 접속 테스트")
def test_web_search(driver):
    driver.goto("https://playwright.dev")
    time.sleep(2)

    page_text = driver.content()
    assert "Playwright" in page_text or "playwright" in page_text
