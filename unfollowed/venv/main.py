from selenium import webdriver
from time import sleep


class Instabot:
    def __init__(self, username, pw):
        # if on windows use this
        self.driver = webdriver.Chrome(executable_path='C:\ProgramData\Bin\chromedriver.exe')
        # Else if on mac this will work
        # self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")\
            .click()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names_following()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names_followers()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names_following(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]")\
            .click()
        return names
 # The scroll box for followers and following have different xpath codes
    def _get_names_followers(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]")\
            .click()
        return names

    
usr_bot = Instabot('promiseo_', 'Wilfred123')
usr_bot.get_unfollowers()
