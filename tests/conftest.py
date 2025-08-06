import pytest
from utils.driver_factory import create_driver

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="web", help="web or mobile")

@pytest.fixture(scope="session")
def driver(request):
    platform = request.config.getoption("--platform")
    driver_instance = create_driver(platform)
    yield driver_instance
    driver_instance.quit()