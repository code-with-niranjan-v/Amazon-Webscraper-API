import json
import requests
import amazon_api
import manga_scraper
import novel_scarp
import translate
import googletrans
def main():
    # text = "Hi,How are you?"
    # print(googletrans.LANGCODES)
    # language = input("Select a Language from a options: ")
    # translate1 = translate.Translate(text,language)
    # print(translate1.get_translate())
    # novel_data = novel_scarp.NovelScrap(1)
    # print(novel_data.get_chapter())
   # url = f"https://img.1stkissmanga.tv/image/2020/07/Overgeared-Chapter-{chapter}-{page}.jpg"

    # for i in range(1,3):
    #     manga = manga_scraper.MangaScraper(i)
    #     print(manga.get_link())

    r = requests.get("http://127.0.0.1:7777/get")
    data = r.json()
    num=0
    for i in data['links']:
        print(data['links'][num])
        num+=1
        if num>78:
            break

    print(len(data['links']))


if __name__ == '__main__':
    main()
