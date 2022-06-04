'''
本文件负责输出图片列表，提供给views.py使用
图片列表包括在线Url、本地Path、
1）获取在线图片Url，构建列表并输出；（生产在线图片列表）
2）判断文件夹是否存在，通过在线图片Url列表下载图片（download.py）；
3）构建本地图片Path列表并输出；（生产本地图片列表）
'''

import re
import requests
from . import headers
import os
# import download

#生产在线图片#
class CreatOnlineImage:
    pass

#生产本地图片#
class CreatBaseImages:
    pass

#构建在线图片url列表#
def Pic_list():
    #构建回答页面链接#
    api_url = 'https://www.zhihu.com/api/v4/questions/'
    req_url = '/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit='
    limit = 10
    url_ = api_url + str(282148029) + req_url + str(limit)

    #爬取数据#
    #获取数据文本#
    get_pic_data = requests.get(url_, headers = headers.Headers('zhihu'))
    pic_data_text = get_pic_data.text
    #正则匹配图片地址#
    re_pic_src = r'\ssrc=."(https:.*?)\?'
    re_content = r'content":"(.*?)\\u003'
    #抽取图片文本#
    pic_src_list = re.findall(re_pic_src, pic_data_text)

    return pic_src_list
# print(Pic_list())

#构建本地图片文件路径列表#
def creatImagesPath(x):
    #图片文件夹名称#
    fileNameList = ['marketing', 'newRelease', 'mainTenance']
    #相对路径符号#
    fuhao = '.'
    #基础路径#
    __basePath__ = '/static/image/trenovkr/img/'
    #文件路径#
    __filesPath__ = fuhao + __basePath__ + fileNameList[x]
    #图片名列表#
    imageNameList = os.listdir(__filesPath__)
    #重构图片文件路径并创建路径列表#
    imagePathList = []
    for i in range(len(imageNameList)):
        imagePath = __basePath__ + fileNameList[x] + '/' + imageNameList[i]
        imagePathList.append(imagePath)

    #返回文件名列表#
    return imagePathList

def testIns():
    fuhao = '.'
    #基础路径#
    __basePath__ = '/static/image/ins/222172028796'
    #文件路径#
    __filesPath__ = fuhao + __basePath__
    #图片名列表#
    imageNameList = os.listdir(__filesPath__)
    #重构图片文件路径并创建路径列表#
    insList = []
    for i in range(len(imageNameList)):
        imagePath = __basePath__ + '/' + imageNameList[i]
        insList.append(imagePath)
    return insList
    # file_name = "D:\MySite\static\image\ins\\" + '123'
    # if not os.path.exists(file_name):
    #     os.mkdir(file_name)
    # else:
    #     print('已经有了哈')


import re
# from textwrap import wrap
import requests
# from headers import Headers
def amazon():
    amazon_headers = {
                'authority': 'www.amazon.com',
                'method': 'GET',
                'path': '/s?k=led+outdoor&ref=nb_sb_noss_2',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': 'session-id-time=2082787201l; i18n-prefs=USD; ubid-main=135-2420930-0181523; session-id=140-8709027-1314032; lc-main=en_US; skin=noskin; session-token=lOfdw48RqSHeYG8PYDxg1Lv+KKQe9QdLyUOGqkQcnh/9YlweITHyLqANcAqqUUSg2dPXqiugQoHDEN4kpchrnA3OjmpZGY3OcuH++gxYoo3DoY6Mlz7mDWNjqWQfYvhG3d6GMNUfnu1np8BtYVWFtHOrZq5GeLj4Ow/OfBlF1BJ0qR+dG9JfQz3en8CVt2Eb; csm-hit=adb:adblk_no&t:1645369701791&tb:s-1PRH87NW7219NW85MCN8|1645369701790',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
            }


    # #适合获取亚马逊BestSellers页面产品信息
    url_BestSellers = 'https://www.amazon.com/s?k=led+lights+for+car+headlights&sprefix=led+lights%2Caps%2C790&ref=nb_sb_ss_ts-doa-p_8_10'
    # try:

    amz_BestSellers = requests.get(url_BestSellers, headers=amazon_headers)
    print(amz_BestSellers) #r.status_code   200

    html_Con = amz_BestSellers.text
    # print(amz_BestSellers.content)

    get_Asin = r'<div\sdata-asin="(.*?)"'
    get_Img = r'<img\sclass="s-image"\ssrc="(.*?)"'
    get_Title = r'<span class="a-size-base-plus a-color-base a-text-normal">(.*?)</span>'

    asin = re.findall(get_Asin, html_Con)
    img = re.findall(get_Img, html_Con)

    # for i in range(len(box)):
    #     print(box[i])
    # print(len(box))
    return asin,img