"""
Sequential Selenium tests for the Portfolio website.

Run with:
    pytest tests/test_portfolio.py -v

Requires Chrome to be installed. ChromeDriver is managed automatically by
webdriver-manager — no manual download needed.

The portfolio dev server (or `serve`) must be running at BASE_URL before
running these tests.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Change to 5000 when running against `serve -s portfolio/build -l 5000`
BASE_URL = "http://localhost:3000"


# ---------------------------------------------------------------------------
# Fixture: one Chrome session shared by all tests in this file
# ---------------------------------------------------------------------------
@pytest.fixture(scope="module")
def driver():
    """
    Set up Chrome WebDriver once for the entire test module.

    scope="module" means the browser opens once and is reused across all 7
    tests, then closed at the end. This is faster than opening a new browser
    per test and more realistic (same session, same state flow).

    The --headless flag allows Chrome to run without a graphical display,
    which is required in CI environments (GitHub Actions runners have no GUI).
    """
    options = Options()
    options.add_argument("--headless")          # run without GUI (required in CI)
    options.add_argument("--no-sandbox")        # required in Linux CI containers
    options.add_argument("--disable-dev-shm-usage")  # avoids /dev/shm crash in CI
    options.add_argument("--window-size=1280,800")

    # webdriver-manager auto-downloads the ChromeDriver version that matches
    # the installed Chrome — eliminates version mismatch errors.
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # implicitly_wait tells Selenium to retry finding an element for up to N
    # seconds before raising NoSuchElementException.
    driver.implicitly_wait(5)

    yield driver  # hand the browser to the tests

    driver.quit()  # teardown: close the browser after all tests finish


# ---------------------------------------------------------------------------
# Helper: explicit wait for a visible element
# ---------------------------------------------------------------------------
def wait_for(driver, by, value, timeout=10):
    """
    Wait until an element is visible on the page.

    WebDriverWait + expected_conditions is the professional way to wait for
    elements in Selenium. Prefer this over time.sleep() — it waits only as
    long as needed and raises a clear TimeoutException if the element never
    appears.
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value))
    )


# ---------------------------------------------------------------------------
# Test 1: Homepage loads and the About Me section is present
# ---------------------------------------------------------------------------
def test_01_homepage_loads(driver):
    """
    Navigate to the root URL and verify the About Me section renders.

    This is the baseline test — if this fails, all other tests will fail too
    because the server isn't running or the app didn't render.
    """
    driver.get(BASE_URL)

    about_section = wait_for(driver, By.CSS_SELECTOR, "[data-testid='about-section']")

    assert about_section.is_displayed(), "About Me section should be visible on load"
    assert "About Me" in driver.page_source, "Page should contain the text 'About Me'"


# ---------------------------------------------------------------------------
# Test 2: Projects tab shows thumbnail cards
# ---------------------------------------------------------------------------
def test_02_projects_tab_shows_thumbnails(driver):
    """
    Click the Projects tab and verify that thumbnail cards appear.

    The Projects tab is the default (active on load), but we explicitly click
    it to test that the tab interaction works.
    """
    projects_tab = wait_for(driver, By.CSS_SELECTOR, "[data-testid='tab-projects']")
    projects_tab.click()

    grid = wait_for(driver, By.CSS_SELECTOR, "[data-testid='thumbnail-grid']")

    # Card IDs are prefixed with 'proj-' (e.g. proj-1, proj-2)
    cards = grid.find_elements(By.CSS_SELECTOR, "[data-testid^='card-proj']")

    assert len(cards) > 0, "Projects tab should display at least one thumbnail card"


# ---------------------------------------------------------------------------
# Test 3: Clicking a project thumbnail opens its detail page
# ---------------------------------------------------------------------------
def test_03_project_detail_page_opens(driver):
    """
    Click the first project card and verify the detail page renders.

    Checks both that the detail page container appears and that the title
    is non-empty (i.e. real data was loaded).
    """
    first_card = wait_for(driver, By.CSS_SELECTOR, "[data-testid^='card-proj']")
    first_card.click()

    detail_page = wait_for(driver, By.CSS_SELECTOR, "[data-testid='detail-page']")
    assert detail_page.is_displayed(), "Detail page should appear after clicking a project card"

    title = driver.find_element(By.CSS_SELECTOR, "[data-testid='detail-title']")
    assert title.text != "", "Detail page title should not be empty"


# ---------------------------------------------------------------------------
# Test 4: Back button returns to homepage; Blogs tab shows thumbnail cards
# ---------------------------------------------------------------------------
def test_04_blogs_tab_shows_thumbnails(driver):
    """
    Use the Back button to return to the homepage, then click Blogs tab.

    Tests both the back navigation and the Blogs tab rendering.
    """
    back_btn = wait_for(driver, By.CSS_SELECTOR, "[data-testid='back-button']")
    back_btn.click()

    # Wait for the tab bar to re-appear (confirms we're back on the homepage)
    blogs_tab = wait_for(driver, By.CSS_SELECTOR, "[data-testid='tab-blogs']")
    blogs_tab.click()

    grid = wait_for(driver, By.CSS_SELECTOR, "[data-testid='thumbnail-grid']")

    # Card IDs are prefixed with 'blog-'
    cards = grid.find_elements(By.CSS_SELECTOR, "[data-testid^='card-blog']")

    assert len(cards) > 0, "Blogs tab should display at least one thumbnail card"


# ---------------------------------------------------------------------------
# Test 5: Clicking a blog thumbnail opens its detail page
# ---------------------------------------------------------------------------
def test_05_blog_detail_page_opens(driver):
    """
    Click the first blog card and verify the blog detail page renders.
    """
    first_card = wait_for(driver, By.CSS_SELECTOR, "[data-testid^='card-blog']")
    first_card.click()

    detail_page = wait_for(driver, By.CSS_SELECTOR, "[data-testid='detail-page']")
    assert detail_page.is_displayed(), "Detail page should appear after clicking a blog card"

    title = driver.find_element(By.CSS_SELECTOR, "[data-testid='detail-title']")
    assert title.text != "", "Blog detail page title should not be empty"


# ---------------------------------------------------------------------------
# Test 6: Back button returns to homepage; News tab shows thumbnail cards
# ---------------------------------------------------------------------------
def test_06_news_tab_shows_thumbnails(driver):
    """
    Use the Back button to return, then click the News tab.
    """
    back_btn = wait_for(driver, By.CSS_SELECTOR, "[data-testid='back-button']")
    back_btn.click()

    news_tab = wait_for(driver, By.CSS_SELECTOR, "[data-testid='tab-news']")
    news_tab.click()

    grid = wait_for(driver, By.CSS_SELECTOR, "[data-testid='thumbnail-grid']")

    # Card IDs are prefixed with 'news-'
    cards = grid.find_elements(By.CSS_SELECTOR, "[data-testid^='card-news']")

    assert len(cards) > 0, "News tab should display at least one thumbnail card"


# ---------------------------------------------------------------------------
# Test 7: Clicking a news thumbnail opens its detail page
# ---------------------------------------------------------------------------
def test_07_news_detail_page_opens(driver):
    """
    Click the first news card and verify the news detail page renders.
    """
    first_card = wait_for(driver, By.CSS_SELECTOR, "[data-testid^='card-news']")
    first_card.click()

    detail_page = wait_for(driver, By.CSS_SELECTOR, "[data-testid='detail-page']")
    assert detail_page.is_displayed(), "Detail page should appear after clicking a news card"

    title = driver.find_element(By.CSS_SELECTOR, "[data-testid='detail-title']")
    assert title.text != "", "News detail page title should not be empty"
