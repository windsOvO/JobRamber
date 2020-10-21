'''
Use web crawler get job information in the Internet
'''
import requests
from bs4 import BeautifulSoup
import time
import random

# data
from info import *
# utilities
from utils import *


## 根据筛选条件获得URL
def getURL(keyword, city, page, salary=None, industry=None):
    '''
    keyword: 职业
    city: 城市
    page: 当前页数
    salary: 薪资
    industry: 行业
    '''
    page = str(page)
    url = 'https://www.liepin.com/zhaopin/?key=' + keyword \
            + '&dqs=' + city \
            + '&curPage=' + page
    if salary:
        url += '&salary=' + salary
    if industry:
        url += '' + industry
    return url


## 根据URL获取网页文本信息
def getHTMLText(url, headers=None, proxies = None):
    try:
        if proxies != None:
            # random choose proxy
            ip = random.choice(proxiesIP)
            r = requests.get(url, proxies={'http': ip},
                                  headers={"User-Agent": random.choice(User_Agent)})
            print('ip:', ip)
        else:
            r = requests.get(url, headers={"Cookie": Cookie,
                                           "User-Agent": random.choice(User_Agent),})
                                            # "Referer": Referer})
        r.raise_for_status() # 检查错误
        # r.encoding = r.apparent_encoding 防止编码问题
        return r.text
    except:
        print("Getting html error!")


## 爬取数据将结果存到文件
def getJobLinks(keyword, cities=None, salary=None, industry=None):
    
    # 详情页链接
    links = []

    # 爬取的信息数量
    infoCnt = 0
    # 该网址每次只筛选最多10页
    pageNum = 10
    # 处理单个城市还是全部城市
    if cities == None:
        cities = list(all_cities.values())
    else:
        cities = [str(all_cities[cities])]
    # print(cities)

    # 键转化为值
    if industry != None:
        industry = industries[industry]
    if salary != None:
        salary = salary_segment[salary]

    for city in cities:
    # 遍历所需要的每个页面
        for pageCnt in range(pageNum):
        
            print('Acquired info quantity: ' + str(infoCnt))
            # time.sleep(1)
        
            # 获得URL
            url = getURL(keyword, city, pageCnt, salary, industry)
            # print(url)
            
            # text = getHTMLText(url, proxies=True) # use agent ip
            text = getHTMLText(url, headers=True) # use cooike and user-agent
            soup = BeautifulSoup(text, "html.parser")
            # print(soup)

            # 被反爬虫检测
            # err = soup.find('li', class_='safe-code')
            # if err != None:
            #     print('crawler is limited!')
            #     break

            jobSoup = soup.find_all("h3")
            
            # 找到指向每个详情页的信息
            for js in jobSoup:
                if js.has_attr("title"):
                    # 找到href
                    href = js.find_all("a")[0]["href"]
                    # 判断链接类型，补充字符串
                    if not href.startswith(prefix):
                        href = prefix + href

                    links.append(href)
                    infoCnt += 1

    print('Notice: getJobLinks complete!')
    return links


## 获取详情页信息
def getJobInfos(links):

    # 语料list
    corpus = []
    cnt = 0
    for link in links:

        cnt += 1
        print('Now get info' + str(cnt) + ' from:' + link)
        sec = random.uniform(0,0.4)
        time.sleep(sec) # 随机数停止

        # text = getHTMLText(link, headers=True)
        text = getHTMLText(link, proxies=True)
        soup = BeautifulSoup(text, "html.parser")

        # 被反爬虫检测
        err = soup.find('li', class_='safe-code')
        if err != None:
            print('crawler is limited!')
            break
        
        # describe
        descSoup = soup.find("div", class_='job-item main-message job-description')
        # 两种网页结构
        if descSoup == None:
             descSoup = soup.find("div",class_='job-main job-description main-message')
        descSoup = descSoup.find("div",class_='content content-word').text     
        
        # 'sep'.join(seq),分隔符sep连接各个元素后生成的字符串
        # 避免python处理字符串生成的/xa0还有/r/n
        descSoup = ''.join(descSoup.split())

        # 加载分词器并分词
        lac_res = getLAC(descSoup)

        # 一个职位描述做一个子串
        string = ''
        for i, tag in enumerate(lac_res[1]):
            if tag == 'n' or tag == 'nz':
                string = string + lac_res[0][i] + ' '
                # print(lac_res[0][i], end=' ')

        corpus.append(string)

    # string的list转str
    text = ' '.join(corpus)
    print('Notice: getJobInfos complete!')   
    return text


if __name__=='__main__':

    keyword = '数据挖掘' # 职业
    cities = '北京' # 城市
    salary = None # 薪资
    industry = None # 行业

    links = getJobLinks(keyword, cities, salary, industry)
    text = getJobInfos(links)

    if len(text) == 0:
        print('none result')
    else:
        getCloud(text)