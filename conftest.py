import pytest
from utils import load_json_datas
import logging

logger = logging.getLogger(__name__)

# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser",
#         action="store",
#         default="chromium",
#         help="Browser to run tests against: chromium, firefox, webkit"
#     )


@pytest.fixture(scope="function", autouse=True)
def cmdopt(request):
    browsers = request.config.getoption("--browser")
    return browsers

@pytest.fixture(scope="function", autouse=True, params=list(load_json_datas.load_json_data("config/viewports.json").items()))
def browser_context_args(browser_context_args, request):

    device, viewports = request.param
    logger.info(f"Running test on {device} with viewports: {viewports}")
    return {
                **browser_context_args,
                "ignore_https_errors": True,
                "viewport": {"width": viewports['width'],"height": viewports['height']}
        }   