import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import sqlite3
import os
import requests
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import wxm

data = wxm.data


def startdriver():
    firsturl = 'http://www.gsdata.cn/query/wx?q='
    driver = webdriver.Firefox(firefox_binary = binary)
    driver.get(firsturl)
    return driver

def getstore():
    f = open('data.txt','a',encoding='utf-8')
    conn = sqlite3.connect('wxnews.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists news (id integer primary key autoincrement,wxname varchar,wxzb varchar,wxsj text,wxread integer,wxhref varchar, imgurl varchar, ispublished integer)')
    sql1 = 'update news set ispublished = ' + '\'0\'' + 'where ispublished = ' + '\'1\''
    cursor.execute(sql1)
    driver = startdriver()
    for i in list(data.keys()):
        driver.find_element(By.ID,'search_input').clear()
        driver.find_element(By.ID,'search_input').send_keys(i)
        driver.find_element_by_tag_name('button').click()
        time.sleep(2)
        driver.find_element_by_id('nickname').click()
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[-1])
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME,'wxAti-li')))
        s = driver.find_element(By.CLASS_NAME,'wxAti-li').get_attribute('innerHTML')
        soup = BeautifulSoup(s, 'html.parser')
        listsoup = soup.findAll('li','clearfix')
        wxname = data[i]
        for i in listsoup:
            wxsj = i.find('span').get_text()
            if wxsj[0:10] == str(datetime.date.today() - datetime.timedelta(days = 1)):
                wxzb = i.find('h4').a.string
                wxread = i.find('i',{'class':'icons1 icon1-see'}).parent.get_text()
                if wxread == '--':
                    wxread = '100'
                wxhref = i.find('h4').a['href']
                imgurl = i.find('img')['src']
                ispublished = str(1)
                sql = 'insert into news (wxname, wxzb, wxsj, wxread, wxhref, imgurl, ispublished)values (\'' + wxname + '\',\'' + wxzb +'\',\''+ wxsj +'\',\''+ wxread + '\',\''+ wxhref + '\',\''+ imgurl + '\',\''+ ispublished + '\')'
                f.write(wxname + '**' + wxzb +  '**' + wxsj + '**' + wxread + '**' + wxhref + '**' + imgurl + '***')
                cursor.execute(sql)
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
    conn.commit()
    cursor.close()
    conn.close()
    f.close()
    driver.quit()


def isfile():
    if os.path.exists('data.txt'):
        os.remove('data.txt')
        
if __name__=='__main__':
    isfile()
    binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
    getstore()
    #print(getdetailurl("Safety-T"))
