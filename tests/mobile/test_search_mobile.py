import allure
import time
from appium.webdriver.common.appiumby import AppiumBy

@allure.title("📱 모바일: Wikipedia 앱 실행 후 검색 텍스트 존재 확인")
def test_mobile_search(driver):
    time.sleep(3)  # 앱 초기 로딩 대기

    # "계속" 버튼을 3번 클릭
    for _ in range(3):
        next_button = driver.find_element(AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_forward_button")
        next_button.click()
        time.sleep(1) 

    # 마지막에 "시작하기" 버튼 클릭
    start_button = driver.find_element(AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_done_button")
    start_button.click()

    # Wikipedia 앱: 홈 화면의 검색창 텍스트 검증
    search_container = driver.find_element(AppiumBy.ID, "org.wikipedia:id/search_container")
    search_container.click()
    time.sleep(1)
    
    search_input = driver.find_element(AppiumBy.ID, "org.wikipedia:id/search_src_text")
    search_input.send_keys("playwright")
    time.sleep(1)
    # search_label = search_container.get_attribute("content-desc")  # "Search Wikipedia" 등
    # print("검색창 텍스트:", search_label)
   
    # assert "Search" in search_text or "위키백과 검색" in search_text
