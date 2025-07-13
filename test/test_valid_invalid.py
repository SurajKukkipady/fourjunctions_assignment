# test/test_valid_invalid.py

import pytest
from playwright.sync_api import Page

@pytest.mark.parametrize("search_term, should_find_results", [
    ("laptop", True),              # Expected to pass
    ("oioioioioioio", False),       # Expected to pass
])
def test_amazon_search_with_logging(page: Page, search_term, should_find_results):
    page.goto("https://www.amazon.in")

    # Search input
    search_box = page.locator("input[name='field-keywords']")
    search_box.fill(search_term)
    page.keyboard.press("Enter")

    # Wait for results section
    page.wait_for_selector("div.s-main-slot")
    page.wait_for_timeout(1000)

    result_summary = page.locator("span", has_text="1-16 of over")
    no_result_msg = page.locator("span.a-size-medium.a-color-base.a-text-normal", has_text="No results for")

    failures = []

    if should_find_results:
        try:
            page.wait_for_selector("span:has-text('1-16 of over')", timeout=5000)
            assert result_summary.count() > 0
        except Exception as e:
            failures.append(f"Expected results for '{search_term}', but none were found.")
    else:
        try:
            page.wait_for_selector("span.a-size-medium.a-color-base.a-text-normal:has-text('No results for')", timeout=5000)
            assert no_result_msg.count() > 0
        except Exception as e:
            failures.append(f"Expected 'No results' message for '{search_term}', but it was not found.")

    # Fail at the end if any issues occurred
    if failures:
        pytest.fail("\n".join(failures))
