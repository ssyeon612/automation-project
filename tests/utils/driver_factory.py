from playwright.sync_api import sync_playwright
from appium import webdriver

def create_driver(platform):
    if platform == "web":
        pw = sync_playwright().start()
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        return {
            "pw": pw,
            "browser": browser,
            "context": context,
            "page": page
        }
    
    elif platform == "mobile":
        caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.example.app",
            "appActivity": ".MainActivity",
            "automationName": "UiAutomator2"
        }
        driver = webdriver.Remote("http://127.0.0.1:4723", caps)
        return { "driver": driver }