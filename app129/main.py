import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / "chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=str(CHROME_DRIVER_PATH))
chrome_browser = webdriver.Chrome(
    service=chrome_service, options=chrome_options)

chrome_browser.get("https://www.google.com")
time.sleep(30)
