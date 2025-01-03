from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

#https://www.englishspeak.com/pt/english-phrases?category_key=1

class FlashCards():
    def __init__(self):
        self.drive = webdriver.Firefox()

    def find_list(self,start_page=1, final_page=1):
        pass

    def save_csv(self, name_file, list_phrases ):
        pass
