from email import parser
import re
import requests
from . import headers
# import headers
import os
# from bs4 import BeautifulSoup

def amz():
    #构建链接
    keyWord = 'montessori toys for 3 years old'
    keyWord = keyWord.replace(' ', '+')
    url_Product = 'https://www.amazon.com/s?k=' + keyWord + '&ref=nb_sb_noss'

    amz_ladybug = requests.get(url_Product, headers = headers.Headers('amazon'))
    print(amz_ladybug) 

    html_Con = amz_ladybug.text

    '''
    baby monitor
    led headlight bulbs
    montessori toys for 3 years old
    tire inflator
    '''
    # 正则表达式
    re_Highly_Rated = r'<div\sdata-asin="(B.{9})"\sclass="sg-col.*?\s.*?\s.*?\s.*?\s.*?"><div.*?>\s+<div.*?>\s+<div.*?>\s+<div.*?><div.*?><span.*?><a.*?><div.*?><img.*?src="(.*?)"\s'

    re_AdHolder = r'<div\sdata-asin="(B.*?)"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{10})sg-col\s.+inner">\s+<.*?>\s+<.*?>\s+<.*?>\s+<div\sclass="s-card.*?><.+\ssrc="(.*?)"\s'

    re_Natural = r'<div\sdata-asin="(B.*?)"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{10})sg-col\s.+inner">\s+<div.*?>\s+<div\sclass="s-card.*?><.+\ssrc="(.*?)"\s'
    # r'<div\sdata-asin="(B.*?)"\sdata-index="(\d+)"\sdata-uuid=".*?".*?class=".*?(.{10})sg-col\s.+inner">\s+<.*?>\s+<.*?>\s+</a>.*?</div></div>(.{30})'

    # 匹配结果
    BestSeller = re.findall(re_Highly_Rated, html_Con)
    AdHolder = re.findall(re_AdHolder, html_Con)
    Natural = re.findall(re_Natural, html_Con)

    # with open("html.txt", mode="w", encoding="utf-8") as file:
    #     file.write(html_Con)

    hr_ = [BestSeller, len(BestSeller)]
    ad_ = [AdHolder, len(AdHolder)]
    na_ = [Natural, len(Natural)]

    return ad_, hr_, na_