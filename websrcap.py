#Samy Idesis - Processo seletivo Revio - TESTE PYTHON

import selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.omelete.com.br/")
time.sleep(15) #Ocasionalmente a página pode demorar a carregar por completo

botao_pesquisa = driver.find_element(By.XPATH, '/html/body/header/div[2]/div[1]/div/div[4]/div[1]/i')
botao_pesquisa.click()
time.sleep(2)
botao_input = driver.find_element(By.XPATH,'/html/body/footer/section/div/div/div/form/div/input')
botao_input.send_keys('Deadpool')
botao_pesquisa2 = driver.find_element(By.XPATH, '/html/body/footer/section/div/div/div/form/div/button')
botao_pesquisa2.click()
time.sleep(10)

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    try:
        botao_vermais = driver.find_element(By.XPATH, '//*[@id="loadMore"]')
        botao_vermais.click()
        time.sleep(3)
        
    except Exception as e:
        #Fim notícias "Deadpool"
        time.sleep(3)
        break

print("Aguarde até que o arquivo txt seja gerado.")

elementos_titulos = driver.find_elements(By.CLASS_NAME, 'mark__title')
titulos = []

for elemento in elementos_titulos:
    texto_completo = elemento.text
    titulo_puro = texto_completo
    titulos.append(titulo_puro)

titulos_Deadpool = [titulo for titulo in titulos if 'Deadpool' in titulo]
    
time.sleep(8)
    
elementos_datas = driver.find_elements(By.CLASS_NAME, 'mark__time')
datas = []

for elemento in elementos_datas:
    texto_completo = elemento.text
    data_somente = texto_completo.split(',')[0] #Retira horário
    datas.append(data_somente)

noticia_data = []
for titulo in titulos:
    if 'Deadpool' in titulo:
        index = titulos.index(titulo)
        if index < len(datas):
            noticia_data.append((titulo, datas[index]))

with open('noticias&datas.txt', 'w', encoding='utf-8') as arquivo:
    for titulo, data in noticia_data:
        arquivo.write(f"{titulo} - {data}\n")

print("Arquivo 'noticias&datas.txt' criado com sucesso.")


