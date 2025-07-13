# test/test_multiple_pages.py

import pytest
from playwright.sync_api import Page, expect

def test_click_first_amazon_product(page: Page):
    page.goto("https://www.amazon.in")

    # Search for "laptop"
    search_box = page.locator("input[name='field-keywords']")
    search_box.fill("laptop")
    page.keyboard.press("Enter")

    # Wait for search results to load
    page.wait_for_selector("div.s-main-slot")

    # Click Next twice (to go to page 3)
    for _ in range(2):
        next_button = page.locator("a.s-pagination-next")
        expect(next_button).to_be_visible()
        next_button.click()
        page.wait_for_selector("div.s-main-slot")  # Wait for new results to load
    

    # we can use code from test_basic_crawling to implement the next steps
