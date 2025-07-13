# test/test_responsiveness.py
import pytest
from playwright.sync_api import Page, expect

# Define viewports to test responsiveness
viewports = [
    {"name": "Desktop", "width": 1920, "height": 1080},
    {"name": "Tablet", "width": 768, "height": 1024},
    {"name": "Mobile", "width": 375, "height": 667}
]

@pytest.mark.parametrize("viewport", viewports)
def test_amazon_responsiveness(page: Page, viewport):
    try:
        # Set viewport size
        page.set_viewport_size({"width": viewport["width"], "height": viewport["height"]})

        # Step 1: Navigate to Amazon.in
        page.goto("https://www.amazon.in", timeout=15000)

        # Step 2: Ensure search box is visible
        search_box = page.locator("input[name='field-keywords']")
        expect(search_box).to_be_visible(timeout=5000)

        # Step 3: Perform search
        search_box.fill("laptop")
        page.keyboard.press("Enter")
        page.wait_for_selector("div.s-main-slot", timeout=10000)

        # Step 4: Validate at least one product result is visible
        results = page.locator("div.s-main-slot div[data-component-type='s-search-result']")
        expect(results.nth(0)).to_be_visible()

    except Exception as e:
        pytest.fail(f"Test failed in {viewport['name']} view: {str(e)}")
