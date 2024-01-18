from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

Google_form = "https://docs.google.com/forms/d/e/1FAIpQLSfDkSTFnu1PIGWfOm3ztzbrsoGogPL39pFIgYb0P0ex3ZYfqQ/viewform?usp=sf_link"

Zillow = "https://appbrewery.github.io/Zillow-Clone/"

responce = requests.get(Zillow)
data = responce.text
soup = BeautifulSoup(data, "html.parser")
Ul_data = soup.find_all("ul",  class_="List-c11n-8-84-3-photo-cards")
li_data = Ul_data[0].find_all("li")
link = []
address = []
price = []
for data in li_data:
    Link = data.find("a")
    if Link:
        Links = Link["href"]
        link.append(Links)
        Address = data.find("address").text
        Address = Address.replace("\n", "")
        address.append(Address)
        all_price_elements = data.find('span', class_="PropertyCardWrapper__StyledPriceLine")
        all_price = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
        price.append(all_price[0])
print(link)
print(address)
print(price)


Chrome_option = webdriver.ChromeOptions()
Chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(Chrome_option)
driver.get(Google_form)
time.sleep(2)
for i in range(len(link)):
    first_Q = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    first_Q.send_keys(price[i])
    Sec_Q = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    Sec_Q.send_keys(address[i])
    Third_Q = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    Third_Q.send_keys(link[i])
    Submit = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    Submit.click()
    time.sleep(2)
    Another = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    Another.click()