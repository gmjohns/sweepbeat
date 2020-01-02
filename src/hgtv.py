from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time


emails = ['gmjohns@g.clemson.edu', 'gjohnso@ncsu.edu', 'garrett@hightenfund.com', 
                'ebhammel@outlook.com', 'ebhammel27@gmail.com', 'oricky@comcast.net', 
                'aben@comcast.net', 'nrbaime@yahoo.com', 'jeannehammel@me.com', 
                'cameronhammel@me.com', 'kvh5021@gmail.com', 'dbegley4@gmail.com']

HGTV_URL = 'https://www.hgtv.com/design/hgtv-dream-home/sweepstakes'
DIY_URL = 'https://www.diynetwork.com/hgtv-dream-home'

HGTV_ngxFrame = '163659'
DIY_ngxFrame = '163663'


driver = webdriver.Chrome(ChromeDriverManager().install())
for email in emails:
    ##HGTV
    try:
        driver.get(HGTV_URL)
        time.sleep(10)
        driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ngxFrame""" + HGTV_ngxFrame + """"]"""))
        time.sleep(2)
        driver.find_element_by_id("xReturningUserEmail").send_keys(email)
        time.sleep(5)
        driver.find_element_by_xpath("""//*[@id="xCheckUser"]/span""").click()
        time.sleep(10)
        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ngxFrame""" + HGTV_ngxFrame + """"]"""))
        driver.find_element_by_xpath("""//*[@id="multioptin_0_Secondary"]""").click()
        driver.find_element_by_xpath("""//*[@id="multioptin_0_Secondary"]""").click()
        action = ActionChains(driver)
        action.send_keys(Keys.TAB)
        action.send_keys(Keys.ENTER)
        action.perform()
        time.sleep(10)
    except:
        print('Email: ' + email + ' has already been used at HGTV today.')
        pass

    ##DIY
    try:
        driver.get(DIY_URL)
        time.sleep(10)
        driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ngxFrame""" + DIY_ngxFrame + """"]"""))       
        driver.find_element_by_id("xReturningUserEmail").send_keys(email)
        time.sleep(5)
        driver.find_element_by_xpath("""//*[@id="xCheckUser"]/span""").click()
        time.sleep(10)
        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element_by_xpath("""//*[@id="ngxFrame""" + DIY_ngxFrame + """"]"""))
        driver.find_element_by_xpath("""//*[@id="multioptin_06_0_Secondary"]""").click()
        driver.find_element_by_xpath("""//*[@id="multioptin_06_0_Secondary"]""").click()
        action = ActionChains(driver)
        action.send_keys(Keys.TAB)
        action.send_keys(Keys.ENTER)
        action.perform()
        time.sleep(10)
    except:
        print('Email: ' + email + ' has already been used at DIY today.')
        pass

driver.quit()
