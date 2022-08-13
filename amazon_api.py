import json
import os

import requests
from bs4 import BeautifulSoup


class AmazonApi:
    def __init__(self):
        self.url = "https://www.amazon.in/s?k=watch+for+boys&sprefix=watch%2Caps%2C299&ref=nb_sb_ss_softlines-tsdoa-contextual-iss_2_5"
        self.img_src = []
        self.img_name = []
        self.down_img = []
        self.img_link = []
        self.get_data()

    def get_data(self):
        headers = {"User-Agent": "Custom"}
        r = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        img = soup.find_all("img")
        watch = soup.find("div", class_="s-main-slot s-result-list s-search-results sg-row")
        for img in img:
            #print(img['src']+ " has been added")
            self.img_src.append(img['src'])

        watch_name = watch.find_all("h2")
        watch_link = watch.find_all("a")
        for text in watch_name:
            #print(text.text+" has been added")
            self.img_name.append(text.text)

        for watch_link in watch_link:
            #print("https://www.amazon.in/" + watch_link["href"])
            self.img_link.append("https://www.amazon.in/" +watch_link['href'])
        self.check_file("watches.txt")
        self.write_file(self.img_name,self.img_src,self.img_link)


    def write_file(self,names,img_srcs,img_links):
        num = 1
        for name in names:
            f = open("watches.txt","a",encoding='utf-8')
            text = {"Id":num,"Name":name,"Img":img_srcs[num],"Link":img_links[num]}
            data = json.dumps(text)
            f.write(data)
            f.close()
            #self.write_img(name,img_srcs)
            num += 1


    def read_file(self):
        f = open("watches.txt",'r',encoding='utf-8')
        details = f.read()
        f.close()
        return details

    def get_link(self):
        return self.img_src


    def check_file(self,file_path):
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("File has been deleted")
        else:
            print("File does not exist")