import openpyxl
import pyautogui
from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pyautogui import typewrite

# variaveis
cont = 1

# abrir o site
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_patch = r'C:\Users\igora\PycharmProjects\Driver\chromedriver.exe'
driver = webdriver.Chrome(chrome_patch)
driver.get('http://moonbit.co.in/')
driver.maximize_window()

wait = WebDriverWait(driver, 30)
# coloca o nome do grupo
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="BodyPlaceholder_PaymentAddressTextbox"]')))
driver.find_element_by_xpath('//*[@id="BodyPlaceholder_PaymentAddressTextbox"]').send_keys('igor.budex@gmail.com')

# digita o texto
driver.find_element_by_xpath('//*[@id="SignInButton"]').click()
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="recaptcha-anchor"]/div[2]')))
driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[2]').click()

# clica em enviar
driver.find_element_by_xpath('//*[@id="SignInSubmitButton"]').click()
