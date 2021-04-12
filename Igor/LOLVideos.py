from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

usuario = 'igorV44'  # input('Informe o usuário: ')
senha = 'i4g4o6r7'  # input('Informe a senha: ')
minutos = ""
CONT = 25
CONT2 = 2

# abrir o site
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_patch = r'C:\Users\igora\PycharmProjects\Driver\chromedriver.exe'
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_patch)
driver.get('https://watch.lolesports.com/')
driver.maximize_window()

wait = WebDriverWait(driver, 30)
print('Iniciando Automacao: ' + str(datetime.today().hour) + ':' + str(datetime.today().minute))

# logon
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="riotbar-account"]/div/a')))
driver.find_element_by_xpath('//*[@id="riotbar-account"]/div/a').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div/input').send_keys(usuario)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/input').send_keys(senha)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div[4]/div[1]/label').click()
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/button').click()

# Espera o site carregar e clica em partidas gravadas
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="riotbar-navbar"]/div[3]/a')))
driver.find_element_by_xpath('//*[@id="riotbar-navbar"]/div[3]/a').click()

time.sleep(2)
while CONT > 1:
    # clica na partida
    # wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/div[3]/div/div[{}]/a/div[1]'.format(CONT))))
    time.sleep(3)

    driver.find_element_by_xpath('/html/body/div[2]/main/div[3]/div/div[{}]/a/div[1]'.format(CONT)).click()
    print(CONT)
    time.sleep(1500)
    if CONT2 == 4:
        CONT = CONT - 2
        CONT2 = 1
    else:
        CONT = CONT - 1
        CONT2 = CONT2 + 1
    driver.find_element_by_xpath('//*[@id="riotbar-navbar"]/div[3]/a').click()
    driver.find_element_by_xpath('//*[@id="riotbar-navbar"]/div[3]/a').click()

