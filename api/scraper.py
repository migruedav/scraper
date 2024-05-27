from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def scraper(url: str):
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager(driver_version="125.0.6422.77").install()
            ),
            options=options,
        )

        driver.get(url)
        content = driver.page_source

        return content
    except Exception as e:
        return str(e)
