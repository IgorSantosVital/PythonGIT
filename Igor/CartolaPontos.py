import openpyxl
from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pyautogui import typewrite

usuario = 'igoralexandre2@hotmail.com'  # input('Informe o usuário: ')
senha = 'i4g4o6r7'  # input('Informe a senha: ')
# nomeArq = str(input('Informe o nome do arquivo:'))
rodadaF = int(input('Informe a ultima rodada: '))

# variaveis
rodadaI = 1
cont1 = rodadaI
rodada = rodadaF
cont = 4
times = 3
nomedotime = 'B'

# abrir o site
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_patch = r'C:\Users\igora\PycharmProjects\Driver\chromedriver.exe'
driver = webdriver.Chrome(chrome_patch)
driver.get('https://globoesporte.globo.com/cartola-fc/')
driver.maximize_window()

wait = WebDriverWait(driver, 100)
print('Iniciando Automacao: ' + str(datetime.today().hour) + ':' + str(datetime.today().minute))

# acessar o arquivo
arq = r'C:\Users\igora\OneDrive\Documentos\CARTOLA FC\CARTOLA 2019.xlsx'
doc = openpyxl.load_workbook(arq)
aba = doc.worksheets[1]
time.sleep(1)

# logon
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="buttonToCartola"]')))
driver.find_element_by_xpath('//*[@id="buttonToCartola"]').click()
# time.sleep(5)

input('Faça login e aperte enter aqui!')
while aba['{}{}'.format(nomedotime, times)].value is not None:
    while rodadaI <= rodadaF:
        if aba['{}{}'.format(nomedotime, cont)].value is None:
            # pegar nome do time
            selecao = aba['{}{}'.format(nomedotime, times)].value
            print(selecao)
            # procurar nome do time
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/header-v2/header/div/div[3]/di'
                                                                       ''
                                                                       'v/form/input')))
                driver.find_element_by_xpath('/html/body/div[1]/div[4]/header-v2/header/div/div[3]/div/form/input').click()
            except:
                wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[3]/div[3]/div/div/a/svg/svg')))
                driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div/div/a/svg/svg').click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div[4]/header-v2/header/div/div[3]/div/form/input').clear()
            driver.find_element_by_xpath('/html/body/div[1]/div[4]/header-v2/header/div/div[3]/div/form/input').send_keys(selecao)
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div[4]/header-v2/header/div/div[3]/div/form/input').submit()
            if selecao == 'F.C. Achou errado, otário!':
                wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/div/div[2]/div/ul/li/a/div/div/div[2]/div/span[2]')))
                nome = driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div[2]/div/ul/li/a/div/div/div[2]/div/span[2]').text
                if nome == 'Vinícius do Sandero':
                    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/div/div[2]/div/ul/li[1]/a/div/div/div[2]')))
                    driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div[2]/div/ul/li[1]/a/div/div/div[2]').click()
                else:
                    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/div/div[2]/div/ul/li[2]/a/div/div/div[2]')))
                    driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div[2]/div/ul/li[2]/a/div/div/div[2]').click()
            else:
                # wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[5]/div/div[2]/div/ul/li[1]/a/div/div/div[2]')))
                # driver.find_element_by_xpath('/html/body/div/div[5]/div/div[2]/div/ul/li[1]/a/div/div/div[2]').click()
                wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[6]/div/div[2]/div/ul/li/a/div/div/div[2]')))
                driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div[2]/div/ul/li/a/div/div/div[2]').click()
            # procurar a rodada
            while rodadaI <= rodadaF:
                if aba['A{}'.format(cont)].value is None:
                    aba['A{}'.format(cont)].value = str('RODADA ' + str(rodadaI))
                time.sleep(5)
                # clica no botão para ver as rodadas
                wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/ui-view/div[3]/div/div[1]/div[1]/span[2]')))
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div[6]/ui-view/div[3]/div/div[1]/div[1]/span[2]').click()
                # clica na rodada escolhida
                wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/ui-view/div[3]/div/div[1]/div[2]/label[{}]l/div'.format(rodada))))
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div[6]/ui-view/div[3]/div/div[1]/div[2]/label[{}]l/div'.format(rodada)).click()
                time.sleep(2)
                # copia a pontuação da rodada
                wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/ui-view/div[2]/div[1]/div/div[2]/div'.format(rodada))))
                pontos = driver.find_element_by_xpath('/html/body/div[1]/div[6]/ui-view/div[2]/div[1]/div/div[2]/div').text
                time.sleep(1)
                # imprimir e salvar rodada na planilha
                if pontos == "":
                    pontos = 0
                print('pontuação rodada {}: '.format(rodadaI) + pontos)
                aba['{}{}'.format(nomedotime, cont)] = float(pontos)
                rodadaI += 1
                rodada -= 1
                cont += 1
                doc.save(arq)
        else:
            rodadaI += 1
            rodada -= 1
            cont += 1
            doc.save(arq)
    # alterar coluna dos nomes dos times
    if nomedotime == 'B':
        nomedotime = 'C'
    elif nomedotime == 'C':
        nomedotime = 'D'
    elif nomedotime == 'D':
        nomedotime = 'E'
    elif nomedotime == 'E':
        nomedotime = 'F'
    elif nomedotime == 'F':
        nomedotime = 'G'
    elif nomedotime == 'G':
        nomedotime = 'H'
    elif nomedotime == 'H':
        nomedotime = 'I'

    # reiniciar valores das variaveis
    rodadaI = cont1
    rodada = rodadaF
    cont = 4
doc.close()
driver.quit()

