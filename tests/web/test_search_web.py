import allure, time

@allure.title("웹 검색 기능 테스트")
def test_web_search(driver):
    driver.goto("https://playwright.dev")
    # driver.fill("input[name='q']", "playwright")
    # driver.press("input[name='q']", "Enter")
    time.sleep(2)
    assert "playwright" in driver.content()