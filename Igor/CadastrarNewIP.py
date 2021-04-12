import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



print('Iniciando Automacao: ' + str(datetime.today().hour) + ':' + str(datetime.today().minute))
acao = input('1-Liberar ou 2-Excluir?')
if acao == 1:
    CWifi = input('Qual o WiFi Liberar, 1-Wifi 2.4 ou 2-Wifi 5.0?')
else:
    CWifi = input('Qual o WiFi Bloquear, 1-Wifi 2.4 ou 2-Wifi 5.0?')
# PEGA O NUMERO DO ENDEREÇO
EndMac = input('Informe o Numero do Endereço MAC: ')

time.sleep(1800)
def LogarSite():
    global driver, wait, webdriver
    # ABRE O SITE
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_patch = r'C:\Users\igora\PycharmProjects\Driver\chromedriver.exe'
    driver = webdriver.Chrome(chrome_patch)
    driver.get('http://192.168.0.1')
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)
    # LOGA NO SITE
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'submitBtn')))
    driver.find_element_by_id("UserName").send_keys("NET_E64822")
    driver.find_element_by_id("Password").send_keys("4C1265E64822")
    driver.find_element_by_class_name("submitBtn").click()
    time.sleep(2)


def SelecionarRede(TipoWiFi, TipoAcao):
    wait = WebDriverWait(driver, 30)
    # SELECIONA A ABA QUE VAI LIBERAR
    if TipoWiFi == '1':
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tabs"]/ul/li[4]/a'))), 100000
        driver.find_element_by_xpath('//*[@id="tabs"]/ul/li[4]/a').click()
    elif TipoWiFi == '2':
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tabs"]/ul/li[5]/a'))), 100000
        driver.find_element_by_xpath('//*[@id="tabs"]/ul/li[5]/a').click()
    else:
        quit()
    # CONTROLE DE ENDEREÇO
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="navigation_bar"]/ul/li[3]/a'))), 100000
    driver.find_element_by_xpath('//*[@id="navigation_bar"]/ul/li[3]/a').click()
    # ADICIONA O ENDEREO MAC
    if TipoAcao == '1':
        # CLICA EM ADICIONAR
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Mac_Add"]'))), 100000
        driver.find_element_by_xpath('//*[@id="Mac_Add"]').click()
        time.sleep(3)
        # ADICIONA O END MAC
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="MacAddress"]'))), 100000
        driver.find_element_by_xpath('//*[@id="MacAddress"]').send_keys(EndMac)
        time.sleep(1)
        # CLICA EM ADICIONAR
        driver.find_element_by_xpath('/html/body/div[2]/div[11]/div/button[1]').click()
        time.sleep(2)
        # CLICA EM SALVAR
        driver.find_element_by_xpath('//*[@id="Mac_Apply"]').click()
        time.sleep(5)
        # CASO APRESENTE ERRO CLICA NO POP UP E INFORMA QUE O END JA ESTA CADASTRADO OU ERRADO
        try:
            driver.find_element_by_xpath('//*[@id="tabs"]/ul/li[1]/a').click()
            print('Cadastrado com Sucesso!')
        except:
            driver.switch_to.alert.accept()
            print('Erro ao cadastrar, End MAC ja está cadastrado ou está incorreto!')
    elif TipoAcao == '2':
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="MACAddressFilterTable"]/tbody/tr'))), 100000
        qtdElements = len(driver.find_elements_by_xpath('//*[@id="MACAddressFilterTable"]/tbody/tr'))
        x = 1
        NMacRede = ''
        while x <= qtdElements and NMacRede != EndMac:
            NMacRede = driver.find_element_by_xpath('//*[@id="MACAddressFilterTable"]/tbody/tr[{}]/td[2]'.format(x)).text
            x = x + 1
        time.sleep(1)
        # SELECIONA A LINHA
        if NMacRede == EndMac:
            driver.find_element_by_xpath('//*[@id="MACAddressFilterTable"]/tbody/tr[{}]/td[1]/input'.format(x-1)).click()
            driver.find_element_by_xpath('//*[@id="Mac_Delete"]').click()
            time.sleep(3)
            print('Endereço MAC "' + str(EndMac) + '" excluído com sucesso.')
        else:
            print('Endereço MAC "' + str(EndMac) + '" não encontrado.')
            quit()
    driver.quit()

LogarSite()
SelecionarRede(CWifi, acao)
