# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 01:32:45 2019

@author: S533488
"""

from bs4 import BeautifulSoup
import requests


def get_download_link_all_pages():

    list =[]
    for page_number in range(1, 7):		
        page_url = 'https://www.imdb.com/gallery/rg1624939264?page={0}&ref_=nv_ph_lp'.format(page_number)
        print(page_url)
        list.append(page_url)
        

    return list
    

    

pages_list = get_download_link_all_pages()
print(pages_list)


def get_poster(pages_list):
    count = 0
    print('before the loop')
    
    for url in pages_list:
        print('after the loop')
        headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
        #page_url = "https://www.imdb.com/gallery/rg1624939264?ref_=nv_ph_lp"
        getPage = requests.get(url, headers=headers)
        getPage.raise_for_status()
        latest_posters_page = BeautifulSoup(getPage.text, 'html.parser')
        poster_div = latest_posters_page.find('div',class_="media_index_thumb_list")

        for posterLink in poster_div.find_all('a'):
            poster_title = posterLink['title']
            count = count + 1
            print(poster_title)
            poster_image_link = posterLink.find('img')
            poster_image = poster_image_link['src']
            #print(poster_link['src'])
            imageLink = poster_image.split('@')[0] + "@._V1_.jpg"
            print(imageLink)
            if(poster_title != ""):
                try:
                    imageDownload = open('{0}.jpg'.format(poster_title.replace(':','')),'wb')
                    imageDownload.write(requests.get(imageLink).content)
                    imageDownload.close()
                except:
                    pass
            
    print(count)
get_poster(pages_list)
