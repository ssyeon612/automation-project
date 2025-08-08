from playwright.sync_api import sync_playwright
from appium import webdriver
from appium.options.android import UiAutomator2Options

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
            "deviceName": "Android Device",
            "uuid": "R3CRA0VDCQL",
            "appPackage": "org.wikipedia",
            "appActivity": ".main.MainActivity",
            "automationName": "UiAutomator2",
        }
        options = UiAutomator2Options().load_capabilities(caps)
        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        return { "driver": driver }