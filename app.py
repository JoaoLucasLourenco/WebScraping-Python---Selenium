from selenium import webdriver
import quote

driver = webdriver.Firefox()
driver.get("http://quotes.toscrape.com/login")

#Função para logar, precisa apenas da variável do webdriver
quote.login(driver)

#Função para pegar o texto das quotes, precisa da variável do webdriver e da quantidade de quotes a que desejar (MÁXIMO DE 10 QUOTES)
quote.getText(driver,10)

#Função para pular de página, precisa apenas da variável do webdriver
quote.nextpage(driver)

