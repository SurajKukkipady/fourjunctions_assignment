import pytest
from playwright.sync_api import Page
import csv
import time

def test_click_each_amazon_product(page: Page):
    page.goto("https://www.amazon.in")

    # Search for "laptop"
    page.locator("input[name='field-keywords']").fill("laptop")
    page.keyboard.press("Enter")

    # Wait for search results to load
    page.wait_for_selector("div.s-main-slot")
    time.sleep(2)

    # Select top 5 product links
    product_links = page.locator("div.s-main-slot a.a-link-normal.s-no-outline").all()
    if not product_links:
        pytest.fail("No product links found.")
    top_5_links = product_links[:5]

    # Open CSV for writing
    with open("amazon_products.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Rating", "URL"])

        for i, link in enumerate(top_5_links):
            href = link.get_attribute("href")
            if not href:
                continue

            full_url = "https://www.amazon.in" + href
            new_tab = page.context.new_page()
            try:
                new_tab.goto(full_url)
                new_tab.wait_for_load_state("domcontentloaded")

                # Validate title
                title_elem = new_tab.locator("h1#title span")
                if title_elem.count() == 0:
                    pytest.fail(f"Product {i+1}: Title not found.")
                title = title_elem.inner_text().strip()

                # Validate price
                price_elem = new_tab.locator("span.a-price-whole").first
                if price_elem.count() == 0:
                    pytest.fail(f"Product {i+1}: Price not found.")
                price = price_elem.inner_text().strip()

                # Validate rating
                rating_elem = new_tab.locator("span.a-icon-alt").first
                if rating_elem.count() == 0:
                    pytest.fail(f"Product {i+1}: Rating not found.")
                rating_text = rating_elem.inner_text().strip()
                rating = rating_text.split()[0]

                # Write to CSV
                writer.writerow([title, price, rating, full_url])

            except Exception as e:
                pytest.fail(f"Product {i+1}: Exception occurred - {e}")
            finally:
                new_tab.close()
