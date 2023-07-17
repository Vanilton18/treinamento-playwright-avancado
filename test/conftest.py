import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "timezone_id": "America/Manaus",
        # "timezone_id": "America/New_York",
        "locale": "pt-BR",
        # "locale": "en-US",
        # https://www.science.co.il/language/Locale-codes.php
    }
