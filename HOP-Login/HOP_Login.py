from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from HOP_functions import *

print('-' * 120)
login_name = input("Enter login name for the member you want to test: ")
print('-' * 120)
password = input("Enter password for that member: ")
print('-' * 120)

logging.getLogger('WDM').setLevel(logging.NOTSET)
os.environ['WDM_LOG'] = "false"
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://qaportal.hartlinkonline.co.uk/corvidae")
driver.maximize_window()
accept_cookies(driver)

login_as_member(driver, login_name, password)
log_off(driver)
# scrape_demo()

time.sleep(5)

driver.quit()
