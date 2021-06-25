# requests爬取盗墓笔记
import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

def get_content(target):
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find_all('div', id='content')
    content = (texts[0].text.replace('<br/>'*2, '\n'))
    return content

if __name__ == '__main__':
    print("\n欢迎使用<笔趣阁>小说下载小工具\n")
    print("请在https://www.biquge7.com/中搜索你想要的小说\n")
    print("*************************************************************************")
    target = str(input("请输入小说目录地址:\n"))

    server = 'https://www.biquge7.com/'
    book_name = 'download.txt'
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    chapters = chapter_bs.find('div', class_='listmain')
    chapters = chapters.find_all('a')
    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write(content)
            f.write('\n')