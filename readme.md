# 🚀 Four Junctions Assignment

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Framework-Playwright-green.svg" alt="Playwright"/>
  <img src="https://img.shields.io/badge/Testing-Pytest-orange.svg" alt="Pytest"/>
  <img src="https://img.shields.io/badge/CI-GitHub%20Actions-brightgreen.svg" alt="GitHub Actions"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License"/>
</div>

<div align="center">
  <h3>Automated Browser Testing Suite for Amazon India</h3>
  <p>A comprehensive test automation framework validating key user flows using Playwright and Pytest</p>
</div>

---

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [⚙️ Installation](#️-installation)
- [🚀 Usage](#-usage)
- [🧪 Test Suite](#-test-suite)
- [📊 CI/CD Integration](#-cicd-integration)
- [📈 Reports](#-reports)
- [🤝 Contributing](#-contributing)
- [👤 Author](#-author)

---

## 🎯 Project Overview

This repository contains a comprehensive suite of automated browser tests for the Amazon India website. The framework validates critical user journeys including product search, responsive design, pagination navigation, and detailed product page interactions.

## ✨ Features

- 🔍 **Product Search Testing** - Validates search functionality with various keywords
- 📱 **Responsive Design Testing** - Tests across desktop, tablet, and mobile viewports
- 🔄 **Pagination Navigation** - Ensures smooth navigation through search results
- 🛍️ **Product Page Validation** - Tests UI elements and interactions on product pages
- 📊 **Data Export** - Extracts product information to CSV format
- 🚀 **Parallel Execution** - Supports concurrent test execution for faster results
- 📋 **HTML Reporting** - Generates detailed test reports
- 🔄 **CI/CD Integration** - Automated testing with GitHub Actions

## 🛠️ Tech Stack

<table>
  <tr>
    <td align="center" width="100">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40" height="40"/>
      <br><strong>Python 3.8+</strong>
    </td>
    <td align="center" width="100">
      <img src="https://playwright.dev/img/playwright-logo.svg" width="40" height="40"/>
      <br><strong>Playwright</strong>
    </td>
    <td align="center" width="100">
      <img src="https://docs.pytest.org/en/stable/_static/pytest1.png" width="40" height="40"/>
      <br><strong>Pytest</strong>
    </td>
    <td align="center" width="100">
      <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="40" height="40"/>
      <br><strong>GitHub Actions</strong>
    </td>
  </tr>
</table>

| Component | Purpose | Version |
|-----------|---------|---------|
| **Python** | Programming language | 3.8+ |
| **Pytest** | Testing framework | Latest |
| **Playwright** | Browser automation | Latest |
| **pytest-html** | HTML report generation | Latest |
| **pytest-xdist** | Parallel test execution | Latest |
| **CSV** | Data output format | Built-in |

## ⚙️ Installation

### Prerequisites
- Python 3.8 or higher
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/SurajKukkipady/fourjunctions_assignment.git
   cd fourjunctions_assignment
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers**
   ```bash
   playwright install
   ```

## 🚀 Usage

### Basic Test Execution

```bash
# Run all tests
pytest

# Run specific test file
pytest test/test_responsiveness.py

# Run with verbose output
pytest -v

# Run in headed mode (visible browser)
pytest --headed
```

### Advanced Options

```bash
# Generate HTML report
pytest --html=report.html

# Run tests in parallel (4 workers)
pytest -n 4

# Combine parallel execution with HTML reporting
pytest -n 4 --html=report.html

# Run specific test by name
pytest -k "test_product_search"
```

## 🧪 Test Suite

<details>
<summary><strong>📁 Test Files Overview</strong></summary>

| Test File | Description | Key Features |
|-----------|-------------|--------------|
| **`test_basic_crawling.py`** | Product listing scraper | • Extracts top 5 laptop listings<br>• Exports to `amazon_products.csv`<br>• Validates title, price, rating, URL |
| **`test_multiple_pages.py`** | Pagination navigation | • Tests page navigation<br>• Validates page numbers<br>• Ensures content updates |
| **`test_product_page.py`** | Product page validation | • Tests "Add to Cart" functionality<br>• Validates accordion sections<br>• Checks product specifications<br>• Tests immersive view images |
| **`test_responsiveness.py`** | Cross-device testing | • Desktop viewport (1920x1080)<br>• Tablet viewport (768x1024)<br>• Mobile viewport (375x667) |
| **`test_valid_invalid.py`** | Search functionality | • Valid keyword searches<br>• Invalid/gibberish keyword handling<br>• Error message validation |
| **`test_functions.py`** | Unit tests | • Tests utility functions<br>• Validates helper methods |

</details>

### Test Coverage Areas

- 🔍 **Search Functionality** - Valid and invalid keyword handling
- 📱 **Responsive Design** - Multi-device viewport testing
- 🔄 **Navigation** - Page traversal and pagination
- 🛍️ **Product Interactions** - Cart operations and UI elements
- 📊 **Data Extraction** - CSV export functionality
- 🧪 **Unit Testing** - Helper function validation

## 📊 CI/CD Integration

This project uses **GitHub Actions** for continuous integration:

- ✅ Automated test execution on push/PR

## 📈 Reports

### HTML Reports
Generate comprehensive test reports with:
```bash
pytest --html=report.html --self-contained-html
```

### CSV Output
Product data is automatically exported to:
- `amazon_products.csv` - Contains product details from search results

### Coverage Reports
```bash
pytest --cov=. --cov-report=html
```


## 👤 Author

**Suraj Kukkipady**
- GitHub: [@SurajKukkipady](https://github.com/SurajKukkipady)

---

