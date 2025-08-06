from playwright.sync_api import sync_playwright
from appium import webdriver

def create_driver(platform):
    if platform == "web":
        pw = sync_playwright().start()
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context()
        return context.new_page()
    
    elif platform == "mobile":
        caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.example.app",
            "appActivity": ".MainActivity",
            "automationName": "UiAutomator2"
        }
        return webdriver.Remote("http://127.0.0.1:4723", caps)