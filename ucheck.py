from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

UTORID = ""
PASSWORD = ""

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://ucheck.utoronto.ca/')

j_username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'j_username')))

search = driver.find_element(By.NAME, 'j_username')
search.send_keys(UTORID)
search = driver.find_element(By.NAME, 'j_password')
search.send_keys(PASSWORD)
search.send_keys(Keys.RETURN)

button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'MuiButton-label')))

button.click()

frame = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'label')))
frame.click()

submit = driver.find_elements(By.TAG_NAME, 'button')
submit[1].click()
