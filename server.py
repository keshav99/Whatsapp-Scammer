from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

name = 'Roshni'

browser = webdriver.Chrome('./chromedriver')
browser.get("https://web.whatsapp.com")

input("Press Enter to continue...")
chat = browser.find_element_by_xpath("//*[@class='_1wjpf _3NFp9 _3FXB1' and text()='"+name+"']")
chat.click()
messageBox = browser.find_element_by_xpath("//*[@class='_1Plpp']")
i = 1
for i in range(1,201):
    messageBox.send_keys("I'm asking you whatsup for the "+str(i)+"th time")
    sendButton = browser.find_element_by_xpath("//button[@class='_35EW6']")
    sendButton.click() 