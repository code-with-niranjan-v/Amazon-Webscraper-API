import json
import requests

def main():
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
