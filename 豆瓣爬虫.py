 #-*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:26:10 2018

@author: TR
"""

import jieba
import requests
import pandas as pd
import time
import random
from lxml import html
from lxml import etree

def login_in(url):
    """
    UserAgent_List = [
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    ]
"""

    data = {'form_email': '305111795@qq.com', 
            'form_password': '225881110q',
            'redir':'https://movie.douban.com/subject/24773958/comments'}
    cookie = 'gr_user_id=acd7789f-e9e2-499d-8269-a6603a2055c9; bid=eZS8ji42cjg; ll="118283"; viewed="3354490_2305669_1938320_10944567_10944556_3948354_3394930_1927487"; __yadk_uid=jdNsWni0jvJCBa9LNvdWjy6bE3go8moq; douban-fav-remind=1; _ga=GA1.2.2113705092.1475933139; _vwo_uuid_v2=27D4F9A67E06CAB7CD2EDB3BB8FCE092|55293a7bf2ddf60509cd6b7876b082c9; ct=y; ap_v=0,6.0; __utma=30149280.2113705092.1475933139.1538821377.1539141093.86; __utmb=30149280.0.10.1539141093; __utmc=30149280; __utmz=30149280.1539141093.86.76.utmcsr=so.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; __utma=223695111.365424653.1531354488.1538821377.1539141093.28; __utmb=223695111.0.10.1539141093; __utmc=223695111; __utmz=223695111.1539141093.28.21.utmcsr=so.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1539141098%2C%22http%3A%2F%2Fwww.so.com%2Flink%3Fm%3Dadc14eL68YE4VCMbm7pl4p5DqiGKAy2lWVVQYRb1LN4PajJXgeBMZfro0D9%252BdH93SEMZ7klzS3bL01dEeZM%252BaUKvXy3M6gZE82SCeF2ZNAzhELF5nwjsEh4w2cUI%253D%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=3ec947240d51857a.1531354488.29.1539141575.1538821766'
    cookies = {}
    cookie = cookie.split(';')
    for line in cookie:
        key, value = line.split('=', 1)
        cookies[key] = value
    
    
    headers = {'User-agent':'"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                   'Host': 'www.douban.com'}
    response = requests.post(url, headers=headers, data=data, cookies=cookies)
    print("网页请求状态码：%s"%response.status_code)
    #print(response.text)
     #检索验证码   
    sel = html.fromstring(response.text)
    var_code_url = sel.xpath('//div[@class="item item-captcha"]/div/img[@id="captcha_image"]/@src')[0]
    captchaID = sel.xpath('//div[@class="item item-captcha"]/div/div/input[@name="captcha-id"]/@value')
    print(var_code_url)
    #print(captchaID)
    
    captcha = input('please input the captcha:')
    
    data['captcha-solution'] = captcha
    data['captcha-id'] = captchaID
    response = requests.post(url, headers=headers, data=data, cookies=cookies)
    print(response.status_code)
    #print(response.text)
    
    session = requests.Session()

    return session
    session.post(url,headers=login_in.headers,data=login_in.data)   
    
def start_spider():    
    base_url = 'https://movie.douban.com/subject/24773958/comments'
    start_url = base_url + '?start=0' 

    number = 1
    html = request_get(start_url) 

    while html.status_code == 200:
        # 获取下一页的 url
        selector = etree.HTML(html.text)
        nextpage = selector.xpath("//div[@id='paginator']/a[@class='next']/@href")
        nextpage = nextpage[0]
        next_url = base_url + nextpage
        # 获取评论
        comments = selector.xpath("//div[@class='comment']")
        marvelthree = []
        for each in comments:
            marvelthree.append(get_comments(each))

        data = pd.DataFrame(marvelthree)
        # 写入csv文件,'a+'是追加模式
        try:
            if number == 1:
                csv_headers = ['用户', '是否看过', '五星评分', '评论时间', '有用数', '评论内容']
                data.to_csv('./Marvel3_yingpping.csv', header=csv_headers, index=False, mode='a+', encoding='utf-8-sig')
            else:
                data.to_csv('./Marvel3_yingpping.csv', header=False, index=False, mode='a+', encoding='utf-8-sig')
        except UnicodeEncodeError:
            print("编码错误, 该数据无法写到文件中, 直接忽略该数据")

        data = []

        html = request_get(next_url)

def request_get(url):
    '''
    使用 Session 能够跨请求保持某些参数。
    它也会在同一个 Session 实例发出的所有请求之间保持 cookie
    '''
    timeout = 5
    
    
    header = {
        'User-agent': '"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/subject/24773958/?from=showing',
    }

    cookie = {
        'cookie': 'gr_user_id=acd7789f-e9e2-499d-8269-a6603a2055c9; bid=eZS8ji42cjg; ll="118283"; viewed="3354490_2305669_1938320_10944567_10944556_3948354_3394930_1927487"; __yadk_uid=jdNsWni0jvJCBa9LNvdWjy6bE3go8moq; douban-fav-remind=1; _ga=GA1.2.2113705092.1475933139; _vwo_uuid_v2=27D4F9A67E06CAB7CD2EDB3BB8FCE092|55293a7bf2ddf60509cd6b7876b082c9; ct=y; ap_v=0,6.0; __utma=30149280.2113705092.1475933139.1538821377.1539141093.86; __utmb=30149280.0.10.1539141093; __utmc=30149280; __utmz=30149280.1539141093.86.76.utmcsr=so.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; __utma=223695111.365424653.1531354488.1538821377.1539141093.28; __utmb=223695111.0.10.1539141093; __utmc=223695111; __utmz=223695111.1539141093.28.21.utmcsr=so.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1539141098%2C%22http%3A%2F%2Fwww.so.com%2Flink%3Fm%3Dadc14eL68YE4VCMbm7pl4p5DqiGKAy2lWVVQYRb1LN4PajJXgeBMZfro0D9%252BdH93SEMZ7klzS3bL01dEeZM%252BaUKvXy3M6gZE82SCeF2ZNAzhELF5nwjsEh4w2cUI%253D%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=3ec947240d51857a.1531354488.29.1539141575.1538821766',
    }

    time.sleep(random.randint(5, 15))  
    response = requests.get(url, headers=header, cookies=cookie, timeout = 5)
    if response.status_code != 200:
        print(response.status_code)
    return response




def get_comments(eachComment):
    commentlist = []
    user = eachComment.xpath("./h3/span[@class='comment-info']/a/text()")[0]  # 用户
    watched = eachComment.xpath("./h3/span[@class='comment-info']/span[1]/text()")[0]  # 是否看过
    rating = eachComment.xpath("./h3/span[@class='comment-info']/span[2]/@title")  # 五星评分
    if len(rating) > 0:
        rating = rating[0]

    comment_time = eachComment.xpath("./h3/span[@class='comment-info']/span[3]/@title")  # 评论时间
    if len(comment_time) > 0:
        comment_time = comment_time[0]
    else:
        # 有些评论是没有五星评分, 需赋空值
        comment_time = rating
        rating = ''

    votes = eachComment.xpath("./h3/span[@class='comment-vote']/span/text()")[0]  # "有用"数
    content = eachComment.xpath("./p/span/text()")[0]  # 评论内容
    print(content)
    commentlist.append(user)
    commentlist.append(watched)
    commentlist.append(rating)
    commentlist.append(comment_time)
    commentlist.append(votes)
    commentlist.append(content.strip())
    #print(commentlist)
    return commentlist

if __name__ == "__main__":
    url = 'https://www.douban.com/accounts/login'
    login_in(url)
    start_spider()