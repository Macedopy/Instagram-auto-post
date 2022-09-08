import autoit
from ssl import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Instagramautopost(App):

    def callback(self, send_button):
        chrome_options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(chrome_options=chrome_options)

        driver.get("https://www.instagram.com/")

        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))

        username.clear()
        username.send_keys(self.user_account_inp.text)

        password.send_keys(self.pass_account_inp.text)

        btn = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'))).click()

        not_now= WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Agora não')]"))).click()

        not_now2= WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Agora não')]"))).click()

        publication_feed= WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button"))).click()
        select_image_insta= WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button"))).click()

        photopath=self.file_account_inp.text

        autoit.win_active("Abrir")
        time.sleep(0.5)
        autoit.control_send("Abrir", "Edit1", photopath)
        time.sleep(0.5)
        autoit.control_send("Abrir", "Edit1", "{ENTER}")

        WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button'))).click()
        WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button'))).click()

        feed_caption=WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea')))
        feed_caption.clear()
        feed_caption.send_keys(self.title_post_inp.text)

        share_photo_feed=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button"))).click()
        time.sleep(5)

    def build(self):

        self.window=GridLayout(cols=1)
        self.window.size_hint=(0.8,0.8)
        self.window.pos_hint= {"center_x": 0.5, "center_y": 0.5}
        self.title='Instagram auto post'
        self.icon="Instagram_logo.png"

        self.window.add_widget(Image(source="Instagram_logo.png"))

        self.user_account= Label(text="User",
                                font_size=20,
                                color='#666699')
        self.window.add_widget(self.user_account)

        self.user_account_inp=TextInput(multiline=False,
                                        padding_y=(5,5),
                                        size_hint=(1,0.5))
        self.window.add_widget(self.user_account_inp)

        self.pass_account= Label(text="Password", 
                                font_size=20, 
                                color='#666699')
        self.window.add_widget(self.pass_account)

        self.pass_account_inp=TextInput(multiline=False,
                                        padding_y=(5,5),
                                        size_hint=(1,0.5))
        self.window.add_widget(self.pass_account_inp)

        self.file_account= Label(text="Filepath", 
                                font_size=20, 
                                color='#666699')
        self.window.add_widget(self.file_account)

        self.file_account_inp=TextInput(multiline=False,
                                        padding_y=(5,5),
                                        size_hint=(1,0.5))
        self.window.add_widget(self.file_account_inp)

        self.title_post= Label(text="Title Post",
                                font_size=20,
                                color='#666699')
        self.window.add_widget(self.title_post)

        self.title_post_inp=TextInput(multiline=False,
                                    padding_y=(5,5),
                                    size_hint=(1,0.5))
        self.window.add_widget(self.title_post_inp)

        self.send_button= Button(text="Send", size_hint=(1,0.5), background_color='#666699')
        self.send_button.bind(on_press = self.callback)
        self.window.add_widget(self.send_button)



        return self.window

if __name__ == "__main__":
    Instagramautopost().run()