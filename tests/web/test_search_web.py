import allure

@allure.title("웹 검색 기능 테스트")
def test_web_search(driver):
    driver.goto("https://example.com")
    driver.fill("input[name='q']", "playwright")
    driver.press("input[name='q']", "Enter")
    assert "playwright" in driver.content()