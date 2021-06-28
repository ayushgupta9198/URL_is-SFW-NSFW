# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
import urllib.request
from bs4 import BeautifulSoup 
import requests 
import PIL.Image
import PIL.ImageDraw
import face_recognition
import glob
import cv2
import sys
import concurrent.futures


driver=webdriver.Chrome('/home/ayush-ai/Music/final_model/chromedriver_linux64/chromedriver')

def get_detail(sr_no, path , url = None):

    if url is None:
        return "Empty URL"

    li_url = url  #Enter website url

    driver.get(li_url)
    time.sleep(5)

    img_name=0
    images=driver.find_elements_by_css_selector('img')
    for im in images:
        f_image=im.get_attribute('src')
        
        if 'jpg' in f_image:

            urllib.request.urlretrieve(f_image,path+'/'+str(img_name)+'.jpg')
            img_name=img_name+1
            print ('Image '+str(img_name)+' is downloading....')
            time.sleep(1)

    return '-----Downloaded-----' 

def remover(img):  
        cv_img = []
        # print(img)

        n= cv2.imread(img)
        cv_img.append(n)
        g = img.split('/')[-1]
        # print(g)
        image = face_recognition.load_image_file(img)
        face_locations = face_recognition.face_locations(image)
        number_of_faces = len(face_locations)
        # print("I found {} face(s) in this photograph.".format(number_of_faces))

        if number_of_faces!=1:
            os.remove(img)
            print("All unwanted images are removed now")


def image_scrapper(path):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for img in glob.glob(path+"/*.jpg"):
            executor.submit(remover, img)


    driver.close()
    driver.quit()
    print('scrapping and data cleaning completed.')

if __name__ == '__main__':
    path="scrapped_images"   
    url =  'https://exweb.jp/'
    try:
        os.mkdir("scrapped_images")   # Enter folder name
    except Exception as e:
        print (e)
    sr_no=0
    try:
        get_detail(sr_no,path, url)
        sr_no=sr_no+1
    except Exception as e:
        print (e)
    image_scrapper(path)




