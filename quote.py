import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import selenium


def login(driver):
    user = driver.find_element(By.NAME,"username")
    user.send_keys("Teste")

    password = driver.find_element(By.NAME,"password")
    password.send_keys("Teste")

    time.sleep(3)

    bnt_login = driver.find_element(By.XPATH,"//input[@value='Login']").click()


def getText(driver,divNumber):
    i = 1
    
        
    while i <=divNumber:
        texto = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div["+str(i)+"]/span[1]").text
        autor = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div["+str(i)+"]/span[2]/small").text
        tags = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div["+str(i)+"]/div/meta").get_attribute('content')

        quoteimp = {
            'Autor':autor,
            'Frase':texto,
            'Tags':tags.split(',')
        }

        print(json.dumps(quoteimp,indent=2))            
                
        i+=1


def nextpage(driver):
    time.sleep(2)
    clickbtn=driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/nav/ul/li/a").click()
