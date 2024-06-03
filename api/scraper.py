from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def scraper(url: str, wait:int=5):
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager(driver_version="125.0.6422.112").install()
            ),
            options=options,
        )

        driver.get(url)
        time.sleep(wait)
        content = driver.page_source
        driver.quit()

        return content
    except Exception as e:
        return str(e)
