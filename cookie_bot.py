from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from time import sleep
from os import system

system('cls')

url = "https://orteil.dashnet.org/cookieclicker/"
LOOPS = 200
BAKERY_NAME = "SN33DS"
MAX_OPTIONS = 16

class Cookie_Clicker_Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

        assert "Cookie Clicker" in self.driver.title

        sleep(10)
        self.set_bakery_name()
        sleep(10)
        self.game()
    

    def set_bakery_name(self):
	# As you have guessed, this sets your bakery's name ! Change BAKERY_NAME at the top to set your own name. 
        self.driver.find_element_by_xpath('//*[@id="bakeryName"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="bakeryNameInput"]').send_keys(BAKERY_NAME)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="promptOption0"]').click()

    
    def game(self):
	# This is the 'game' loop
        cookies = 500
        buys = 15
        for i in range(LOOPS): # Loop throught 'LOOPS' amount of time
            for _ in range(cookies): # Starts by clicking the cookie 'cookies' amount of time
                self.driver.find_element_by_id('bigCookie').click()
            
            if i >= 1: # Then tries to buy the first 'power up' but only after second loop
                self.driver.find_element_by_xpath('//*[@id="upgrade0"]').click()
           
            try: # This is to remove the achievements
                self.driver.find_element_by_class_name('framed close sidenote').click()
            except NoSuchElementException:
                for f in range(10):
                    try:
                        self.driver.find_element_by_xpath(f'//*[@id="notes"]/div[{f}]').click()
                    except NoSuchElementException:
                        pass
            

            for _ in range(buys): # Finally it loops throught all buyable items 'buys' amount of time
                self.driver.find_element_by_xpath('//*[@id="product0"]').click()
                self.driver.find_element_by_xpath('//*[@id="product1"]').click()
                
                for n in range(2, MAX_OPTIONS):
                    try:
                        self.driver.find_element_by_xpath(f'//*[@id="product{n}"]').click()
                    except ElementNotInteractableException:
                        pass
            
			# Also adds a few units to buys and cookies cause you will get more cookies over time        
            buys += 5
            # print(buys)
            cookies += 50
            # print(cookies)

bot = Cookie_Clicker_Bot()
