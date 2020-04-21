from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from os import system

system('cls')

url = "https://orteil.dashnet.org/cookieclicker/"
LOOPS = 50
BAKERY_NAME = "SN33DS"
MAX_OPTIONS = 16

class Cookie_Clicker_Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
        
        assert "Cookie Clicker" in self.driver.title

        sleep(10)
        self.load_game()
        sleep(5)
        self.set_bakery_name()
        sleep(5)
        self.game()
        #sleep(5)
        #self.save_game()
        sleep(10)
        self.driver.close()
    

    def set_bakery_name(self):
	# As you have probably guessed, this sets your bakery's name if it isn't already set | Change BAKERY_NAME at the top to set your own name. 
        if self.driver.find_element_by_xpath('//*[@id="bakeryName"]').text != (BAKERY_NAME + "' bakery"):
            self.driver.find_element_by_xpath('//*[@id="bakeryName"]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="bakeryNameInput"]').send_keys(BAKERY_NAME)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="promptOption0"]').click()
        else:
            pass

    
    def load_game(self):
        self.driver.find_element_by_xpath('/html').send_keys(Keys.CONTROL, 'o')

        with open('save.txt', 'r') as file:
            save_text = file.read()
            self.driver.find_element_by_xpath('//*[@id="textareaPrompt"]').send_keys(save_text)
        
        self.driver.find_element_by_xpath('//*[@id="promptOption0"]').click()

        
    def save_game(self):
        reset = ActionChains(self.driver)
        action = ActionChains(self.driver)
        
        self.driver.find_element_by_xpath('//*[@id="prefsButton"]').click()
        sleep(2)
        
        body = self.driver.find_element_by_xpath('/html/body')
        # el = self.driver.find_element_by_css_selector('#menu > div.subsection > div:nth-child(3) > a:nth-child(1)')
        # location = el.location
        # print(location)
        
        reset.move_to_element_with_offset(body ,0, 0)
        reset.perform()
        action.move_by_offset(493, 305).click()
        action.perform()

        sleep(1)
        save = self.driver.find_element_by_xpath('//*[@id="textareaPrompt"]').text

        with open('save.txt', 'w') as file:
            file.write(save)
        
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="promptOption0"]').click()

        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="menu"]/div[1]').click()

    
    def golden_cookie(self):
        try: # Should click on the golden cookie if it is on screen
            self.driver.find_element_by_xpath('//*[@id="shimmers"]/div').click()
        except NoSuchElementException:
            pass


    def remove_achievements(self):
        try: # This is to remove the achievements
            self.driver.find_element_by_class_name('framed close sidenote').click()
        except NoSuchElementException:
            for f in range(10):
                try:
                    self.driver.find_element_by_xpath(f'//*[@id="notes"]/div[{f}]').click()
                except NoSuchElementException:
                    pass


    def game(self):
	# This is the 'game' loop
        cookies = 500
        buys = 15
        for i in range(LOOPS): # Loop throught 'LOOPS' amount of time
            self.golden_cookie()

            for c in range(cookies): # Starts by clicking the cookie 'cookies' amount of time
                self.driver.find_element_by_id('bigCookie').click()
                if c % 55 == 0:
                    self.golden_cookie()
            
            self.golden_cookie()

            if i >= 1: # Then tries to buy the first 'power up' but only after second loop
                try:
                    self.driver.find_element_by_xpath('//*[@id="upgrade0"]').click()
                except StaleElementReferenceException:
                    pass
            
            self.remove_achievements()
            self.golden_cookie()

            for _ in range(buys): # Finally it loops throught all buyable items 'buys' amount of time
                for n in range(MAX_OPTIONS, -1, -1):
                    try:
                        self.driver.find_element_by_xpath(f'//*[@id="product{n}"]').click()
                    except ElementNotInteractableException:
                        pass
            
            self.save_game()
			# Also adds a few units to cookies cause you will need more cookies over time        
            cookies += 5
            print(i)

bot = Cookie_Clicker_Bot()
