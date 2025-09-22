# tests/conftest.py
import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)  # headless=True in CI
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://example.com")  # Replace with your actual target URL

    yield page

    context.close()
    browser.close()
