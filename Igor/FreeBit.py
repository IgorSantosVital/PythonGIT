from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

usuario = 'igor.budex@gmail.com'  # input('Informe o usuário: ')
senha = 'i4g4o6r7'  # input('Informe a senha: ')
minutos = ""
cont = 1

# abrir o site cartola
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_patch = r'C:\Users\igora\PycharmProjects\Driver\chromedriver.exe'
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_patch)
driver.get('https://freebitco.in/')
driver.maximize_window()

wait = WebDriverWait(driver, 30)
print('Iniciando Automacao: ' + str(datetime.today().hour) + ':' + str(datetime.today().minute))

# logon
wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/nav/section/ul/li[10]/a')))
driver.find_element_by_xpath('/html/body/div[2]/div/nav/section/ul/li[10]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login_form_btc_address"]').send_keys(usuario)
driver.find_element_by_xpath('//*[@id="login_form_password"]').send_keys(senha)
driver.find_element_by_xpath('//*[@id="login_button"]').click()
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="push_notification_modal"]/div[1]/div[2]/div/div[1]')))
driver.find_element_by_xpath('//*[@id="push_notification_modal"]/div[1]/div[2]/div/div[1]').click()

# pega os minutos que faltam
minutos = driver.find_element_by_xpath('//*[@id="time_remaining"]').text

# se não estiver vazio transforma em inteiro
if minutos != '':
    minutos = int(minutos[0:1])

while cont == 1:
    if minutos == '':
        driver.find_element_by_xpath('//*[@id="login_form_password"]').send_keys(senha)
        driver.find_element_by_xpath('//*[@id="free_play_form_button"]').click()
    else:
        while minutos >= 0:
            time.sleep(minutos)
            minutos = int(driver.find_element_by_xpath('//*[@id="time_remaining"]').text)

    minutos = driver.find_element_by_xpath('//*[@id="time_remaining"]').text
    if minutos >= 0:
        minutos = int(minutos[0:1])