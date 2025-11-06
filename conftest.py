import pytest
from utils import load_json_datas
import logging

logger = logging.getLogger(__name__)
viewports = list(load_json_datas.load_json_data("config/viewports.json").items())

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="test",
        help="environment to run tests against: dev, test, stage, prod",
        choices=("test", "dev", "stage", "prod"),
    )

@pytest.fixture(scope="session")
def get_env_datas(request):
    env = request.config.getoption("--env")
    test_data = load_json_datas.load_json_data(f"./tests/test_data/{env}_env_data.json")
    return test_data

@pytest.fixture(scope="function", autouse=True, params=viewports, ids=[f"{device}-{viewport['width']}x{viewport['height']}" for device, viewport in viewports])
def browser_context_args(browser_context_args, request):
    device, viewports = request.param
    logger.info(f"Running test on {device} with viewports: {viewports}")
    return {
                **browser_context_args,
                "ignore_https_errors": True,
                "viewport": {"width": viewports['width'],"height": viewports['height']}
               
        }   

@pytest.fixture(scope="session", autouse=True)
def browser_type_launch_args(browser_type_launch_args, request, get_env_datas):
    return {
                **browser_type_launch_args,
                "slow_mo": 2000
        }   