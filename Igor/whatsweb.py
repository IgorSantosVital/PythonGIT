import openpyxl
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
driver.get('https://web.whatsapp.com')
driver.maximize_window()

wait = WebDriverWait(driver, 100)
print('Iniciando Automacao: ' + str(datetime.today().hour) + ':' + str(datetime.today().minute))
# ('Libere o codigo e aperte enter aqui')

wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pane-side"]/div/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span')))
cont = len(driver.find_elements_by_xpath('//*[@id="pane-side"]/div/div/div/div'))
cont2 = cont
cont3 = 0
cont4 = 1
# print(cont)

while cont != 0:
    lista = []
    for x in range(cont2):
        lista.append(driver.find_element_by_xpath(
            '//*[@id="pane-side"]/div/div/div/div[{}]/div/div/div[2]/div[1]/div[1]/span'.format(cont2)).text)
        cont2 -= 1
    # fazer lista somente uma vez
    if cont3 == 0:
        print(lista)
        nome = input('Informe o nome que quer conversar: ')
        cont3 += 1
    texto = driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[{}]/div/div/div[2]/div[1]/div[1]/span'.format(cont)).text

    # print(texto)
    if texto == nome:
        # clicar no nome
        driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[{}]/div/div/div[2]/div[1]/div[1]/span'.format(cont)).click()
        # verificar conversa
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div[3]/div/div/div[3]/div')))
        cont1 = len(driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div'))
        # enviar msg inicial
        if cont1 is None:
            msgI = input('Mensagem: ')
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(msgI)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[3]/button')))
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
        # responder msg
        elif cont1 >= 0:
            while cont4 == 1:
                msganterior = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]/div[{}]/div/div/div[1]/div/span'.format(cont1)).text
                print(msganterior)
                msgR = input('Mensagem: ')
                driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(msgR)
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[3]/button')))
                driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
                break
        cont -= 1
    else:
        cont -= 1

if cont == 0:
    # clicar em buscar
    driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div').click()
    # colocar o nome que vai buscar
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="side"]/div[2]/div/label/input')))
    driver.find_element_by_xpath('//*[@id="side"]/div[2]/div/label/input').send_keys(nome)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div[2]/div/div/div/div/div/div/div[2]')))
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div[2]/div/div/div/div/div/div/div[2]').click()
    # enviar mensagem

    while cont4 == 1:
        msganterior = driver.find_element_by_xpath(
        '//*[@id="main"]/div[3]/div/div/div[3]/div[{}]/div/div/div[1]/div/span'.format(cont1)).text
        print(msganterior)
        msgI = input('Mensagem: ')
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(msgI)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[3]/button')))
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
        break

driver.quit()
