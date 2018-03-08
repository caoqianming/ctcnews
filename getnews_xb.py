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
import random

data = wxm.data
username = '18911936305'
password = 'Aq123456'
def startdriver():
    firsturl = 'https://www.newrank.cn/public/login/login.html?back=https%3A//www.newrank.cn/'
    driver = webdriver.Firefox(firefox_binary = binary)
    driver.get(firsturl)
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]').click()
    driver.find_element_by_id('account_input').send_keys(username)
    driver.find_element_by_id('password_input').send_keys(password)
    driver.find_element_by_id('pwd_confirm').click()
    return driver

def getstore():
    f = open('data.txt','a',encoding='utf-8')
    conn = sqlite3.connect('wxnews.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists news (id integer primary key autoincrement,wxname varchar,wxzb varchar,wxsj text,wxread integer,wxhref varchar, imgurl varchar, ispublished integer)')
    sql1 = 'update news set ispublished = ' + '\'5\'' + 'where ispublished = ' + '\'1\''
    cursor.execute(sql1)
    #cursor.execute('select count(*) from news')
    #ni = cursor.fetchall()[0][0]
    driver = startdriver()
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.ID,'txt_account')))
    for m in list(data.keys()):
        driver.find_element(By.ID,'txt_account').clear()
        driver.find_element(By.ID,'txt_account').send_keys(m)
        time.sleep(5)
        driver.find_element(By.ID,'txt_account').click()
        driver.find_element(By.ID,'txt_account').send_keys(Keys.ENTER)
        time.sleep(5)
        xpathwx = '//*[@data-account="'+ m + '"]'
        driver.find_element_by_xpath(xpathwx).click()
        time.sleep(4)
        driver.switch_to_window(driver.window_handles[-1])
        #WebDriverWait(driver, 10).until_not(lambda driver: driver.find_element_by_class_name("loading"))
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.ID,'info_detail_article_lastest')))
        s = driver.find_element(By.ID,'info_detail_article_lastest').get_attribute('innerHTML')
        soup = BeautifulSoup(s, 'html.parser')
        listsoup = soup.findAll('li')
        wxname = data[m]
        for i in listsoup:
            wxsj = i.find('span',{'class':'info-detail-article-date'}).get_text() + ':00'
            wxhref = i.find('p').a['href']
            cursor.execute('select count(*) from news where wxhref = "%s"'% wxhref)
            if cursor.fetchall()[0][0] == 0:
                wxzb = i.find('p').a['title']

            #print(wxsj)
            #if wxsj[0:10] == str(datetime.date.today() - datetime.timedelta(days = 1)) or wxsj == str(datetime.date.today() - datetime.timedelta(days = 2)):
            #if wxsj[0:10] == str(datetime.date.today() - datetime.timedelta(days = 1)) or wxsj == str(datetime.date.today() - datetime.timedelta(days = 2)):
                
                wxread = i.find('span',{'class':'read-count'}).get_text()
                
                wxdetail = i.find('p',{'class':'article-text'}).a.string
                if wxdetail == None:
                    wxdetail = '无'
                wxzan = i.find('span',{'class':'links-count'}).get_text()
                #imgurl = i.find('img')
                #if imgurl == None:
                #   imgurl = ''
                #x = random.randint(0,ni)
                #cursor.execute('select imgurl from news where id = "'+ str(x) +'"')
                sgurl = 'http://www.sogou.com/web?&query=' + wxzb
                imgrq = requests.get(sgurl).content.decode('utf-8')
                #js = " window.open('%s')"% sgurl
                #driver.execute_script(js)
                #imgrq = driver.get_attribute('innerHTML')
                imgurl = BeautifulSoup(imgrq,'html.parser').find('div', {'class':'str_div'}).find('a').find('img')['src']
                imgurl_name = 'media/wechatimages/'+ wxname + wxread + '.jpg'
                with open(imgurl_name , 'wb') as f:
                    f.write(requests.get(imgurl).content)
                
                imgurl = '/'+ imgurl_name  
                ispublished = str(1)
                sql = 'insert into news (wxname, wxzb, wxsj, wxread, wxhref, imgurl, ispublished, wxdetail, wxzan)values (\'' + wxname + '\',\'' + wxzb +'\',\''+ wxsj +'\',\''+ wxread + '\',\''+ wxhref + '\',\''+ imgurl + '\',\''+ ispublished + '\',\''+ wxdetail+ '\',\''+ wxzan + '\')'
                #f.write(wxname + '**' + wxzb +  '**' + wxsj + '**' + wxread + '**' + wxhref + '**' + imgurl + '***')
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
    conn = sqlite3.connect('wxnews.db')
    cursor = conn.cursor()
    cursor.execute('select count(*) from news where ispublished = "1"')
    if cursor.fetchall()[0][0] == 0:
        cursor.execute('update news set ispublished ="1" where ispublished = "5"')
    cursor.execute('update news set ispublished ="0" where ispublished = "5"')
    conn.commit()
    cursor.close()
    conn.close()

    #print(getdetailurl("Safety-T"))
