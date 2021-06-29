from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        usernameInput = self.browser.find_element_by_xpath(
            "//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath(
            "//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)

    # Followeds

    def getFollowed(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(2)
        self.browser.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(2)
        dialog2 = self.browser.find_element_by_css_selector(
            "div[role=dialog] ul")
        followedCount = len(dialog2.find_elements_by_css_selector("li"))
        print(f'first followed count : {followedCount}')
        action2 = webdriver.ActionChains(self.browser)

        while True:
            dialog2.click()
            action2.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action2.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newFollowedCount = len(dialog2.find_elements_by_css_selector("li"))
            if followedCount != newFollowedCount:
                followedCount = newFollowedCount
                print(f"second followed count {newFollowedCount}")
                time.sleep(1)
            else:
                break

        followed = dialog2.find_elements_by_css_selector("li")
        followedList = []
        followedName = []
        for user in followed:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followedList.append(link)

        for a in followedList:
            followedList = [a.split("com/")]
            followedName.append(followedList[0][1])

        return followedName

    # Followers

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(2)
        self.browser.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)
        dialog = self.browser.find_element_by_css_selector(
            "div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))
        print(f"first count : {followerCount}")
        action = webdriver.ActionChains(self.browser)
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newCount = len(dialog.find_elements_by_css_selector("li"))
            if followerCount != newCount:
                followerCount = newCount
                print(f"second count : {newCount}")
                time.sleep(1)
            else:
                break
        followers = dialog.find_elements_by_css_selector("li")
        followerList = []
        followerName = []
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)

        for a in followerList:
            followerList = [a.split("com/")]
            followerName.append(followerList[0][1])

        return followerName

    def followComparison(self, x, z):
        self.x = x
        self.z = z
        abc = []
        for tekrar in x:
            if tekrar not in z:
                abc.append(tekrar)
        print(abc)
        print(len(abc))

        with open("followed.txt", "w", encoding="UTF-8") as file:
            for item in abc:
                file.write(item + "\n")

    def followComparison2(self, x, z):
        self.x = x
        self.z = z
        abc = []
        for tekrar in z:
            if tekrar not in a:
                abc.append(tekrar)
        print(abc)
        print(len(abc))

        with open("followers.txt", "w", encoding="UTF-8") as file:
            for item in abc:
                file.write(item + "\n")


instagram = Instagram(username, password)
instagram.signIn()
a = instagram.getFollowed()
b = instagram.getFollowers()
instagram.followComparison(a, b)
instagram.followComparison2(a, b)
