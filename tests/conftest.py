import pytest
from utils.driver_factory import create_driver

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="web", help="web or mobile")

@pytest.fixture(scope="session")
def driver(request):
    platform = request.config.getoption("--platform")
    drv = create_driver(platform)

    if platform == "web":
        # drv를 dict 형태로 받아서 page만 넘겨줌
        yield drv["page"]
        drv["browser"].close()
        drv["pw"].stop()

    elif platform == "mobile":
        yield drv["driver"]
        drv["driver"].quit()