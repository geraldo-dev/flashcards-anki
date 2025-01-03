from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class FlashCards():
    def __init__(self):
        self.drive = webdriver.Firefox()
        self.list_phrase_english = []

    def find_list(self, start_page=1, final_page=1):
        local_drive = self.drive

        for count in range(start_page, final_page):

            local_drive.get(f'https://www.englishspeak.com/pt/english-phrases?category_key={str(count)}')
            all_phrases_page = local_drive.find_elements(By.TAG_NAME, 'td')


            for phrases in all_phrases_page:

                phrase = phrases.text.strip(" ").replace("\n",",")

                if phrase != "":
                    self.list_phrase_english.append(phrase)

    def close_page(self):
        self.drive.close()

    def save_csv(self, name_file, list_phrases):

        for phrase in list_phrases:
            new_file = open(f"{name_file}.csv",'a')
            new_file.write(phrase+'\n')
            new_file.close()


flash_card = FlashCards()

#this site goes to page 18
flash_card.find_list(1,2)

flash_card.close_page()

#You can use another name, by default it is "default"
flash_card.save_csv('default',flash_card.list_phrase_english)