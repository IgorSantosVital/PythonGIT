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
cont1 = 0

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
driver.find_element_by_xpath('/html/body/div[1]/div/a[1]').click()



# entra no Multiply
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'double_your_btc_link')))
time.sleep(1)
driver.find_element_by_class_name('double_your_btc_link').click()
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="auto_bet_on"]')))

while cont == 1:
    # seleciona o autobet
    driver.find_element_by_xpath('//*[@id="auto_bet_on"]').click()
    driver.find_element_by_xpath('//*[@id="autobet_roll_count"]').clear()
    driver.find_element_by_xpath('//*[@id="autobet_roll_count"]').send_keys('20')
    driver.find_element_by_xpath('//*[@id="autobet_base_bet"]').clear()
    driver.find_element_by_xpath('//*[@id="autobet_base_bet"]').send_keys('0.00000001')

    # escolhe entre hi ou lo
    if cont1 == 0:
        driver.find_element_by_xpath('//*[@id="autobet_bet_hi"]').click()
        cont1 = 1
    else:
        driver.find_element_by_xpath('//*[@id="autobet_bet_lo"]').click()
        cont1 = 0

    # define maximo de ganho e maximo de perda
    driver.find_element_by_xpath('//*[@id="stop_after_profit"]').click()
    driver.find_element_by_xpath('//*[@id="stop_after_profit_value"]').clear()
    driver.find_element_by_xpath('//*[@id="stop_after_profit_value"]').send_keys('0.00000020')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="stop_after_loss"]').click()
    driver.find_element_by_xpath('//*[@id="stop_after_loss_value"]').clear()
    driver.find_element_by_xpath('//*[@id="stop_after_loss_value"]').send_keys('0.00000020')

    # seleciona on lose e marca increase
    driver.find_element_by_xpath('//*[@id="show_double_your_btc_auto_bet_on_lose"]').click()
    driver.find_element_by_xpath('//*[@id="autobet_lose_increase_bet"]').click()
    driver.find_element_by_xpath('//*[@id="autobet_lose_increase_bet_percent"]').clear()
    driver.find_element_by_xpath('//*[@id="autobet_lose_increase_bet_percent"]').send_keys('100')

    # marca do not refresh
    driver.find_element_by_xpath('//*[@id="autobet_dnr"]').click()

    # clica em start auto bet
    driver.find_element_by_xpath('//*[@id="start_autobet"]').click()
    time.sleep(15)