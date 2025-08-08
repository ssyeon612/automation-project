import subprocess
import threading

def run_web():
    subprocess.run(["pytest", "tests/web/test_search_web.py", "--platform", "web", "--alluredir=allure-results/web"], check=True)

def run_mobile():
    subprocess.run(["pytest", "tests/mobile/test_search_mobile.py", "--platform", "mobile", "--alluredir=allure-results/mobile"], check=True)

if __name__ == "__main__":
    t1 = threading.Thread(target=run_web)
    t2 = threading.Thread(target=run_mobile)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
