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

    # Click the first product directly
    first_product = page.locator("div.s-main-slot a.a-link-normal.s-no-outline").first
    first_product.click()

    # Wait for product page to load
    page.wait_for_load_state("domcontentloaded")

    failures = []

    # Expand accordion section
    try:
        accordion = page.locator("div.a-accordion-row[role='button'][data-csa-c-slot-id='newAccordionRow_1']")
        if accordion.count() > 0:
            accordion.first.click()
    except Exception:
        failures.append("Failed to click accordion section.")

    # Validate Add to Cart button
    try:
        add_to_cart = page.locator("input#add-to-cart-button")
        expect(add_to_cart).to_be_visible()
    except Exception:
        failures.append("'Add to Cart' button not visible.")

    # Validate About this item section
    try:
        about_section = page.locator("div#feature-bullets")
        expect(about_section).to_be_visible()
    except Exception:
        failures.append("'About this item' section not visible.")

    # Validate product details table
    try:
        prod_detail = page.locator("td.a-size-base.prodDetAttrValue")
        assert prod_detail.count() > 0
    except Exception:
        failures.append("Product details <td> not found.")

    # Try immersive view thumbnails
    try:
        full_view_button = page.locator("a.a-declarative:has-text('Click to see full view')")
        if full_view_button.count() > 0:
            full_view_button.first.click()
            for i in [4, 5]:
                thumb = page.locator(f"div.ivThumb[id='ivImage_{i}']")
                if thumb.count() > 0:
                    thumb.first.click()
    except Exception:
        failures.append("Immersive image thumbnail interaction failed.")

    # Report if any step failed
    if failures:
        pytest.fail("\n".join(failures))
