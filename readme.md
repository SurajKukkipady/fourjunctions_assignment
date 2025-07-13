Four Junctions Assignment
This repository contains a suite of automated browser tests for the Amazon India website using Playwright and Pytest. It validates key user flows such as searching for products, checking responsiveness, navigating paginated results, and validating product details.

📦 Tools & Frameworks Used
Tool/Framework	Purpose
Python 3.8+	Programming language
Pytest	Testing framework
Playwright	Browser automation
pytest-html	Generate HTML reports (optional)
pytest-xdist	Parallel test execution
CSV	Data output (for product info)

⚙️ GitHub Actions CI Integration
This project uses GitHub Actions to automatically run tests and measure code coverage.

🚀 Steps to Execute the Scripts
Clone this repository:
git clone https://github.com/SurajKukkipady/fourjunctions_assignment.git

Install dependencies:
pip install -r requirements.txt
playwright install

Run all tests:
pytest

Run a specific test (e.g., responsiveness):
pytest test/test_responsiveness.py

Generate HTML report:
pytest --html=report.html

Run tests in headed mode (to see browser actions):
pytest --headed

Run tests in parallel (e.g., 4 workers):
pytest -n 4

You can also combine parallel mode with HTML reporting:
pytest -n 4 --html=report.html

🧪 Test Files Overview
File	Description
test_basic_crawling.py	Opens and scrapes the top 5 product listings for "laptop". Exports title, price, rating, and URL to amazon_products.csv.
test_multiple_pages.py	Validates navigation through multiple pages of search results.
test_product_page.py	Tests UI elements on a product page: "Add to Cart", accordion sections, product specs, and immersive view images.
test_responsiveness.py	Ensures the site renders correctly on desktop, tablet, and mobile viewports.
test_valid_invalid.py	Performs searches with valid and gibberish keywords to confirm expected results and error handling.
test_functions.py   Unit tests for utility functions in functions.py.

👤 Author
Suraj K