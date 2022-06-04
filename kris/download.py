import os
import requests
import headers

#构建INS图片列表
def getImageURL():
    url = 'https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables=%7B%22id%22%3A%2210907972097%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFBRXo4b0JrOGpkeHNiZEd1RW1yTWlxcldVM3JGSDNDenJycW9BSkxOVmpTNnZvZUVrUXp4U2VzSHJLQnFXQU9CQW11YnltcGpRdVBWblFJYmN0TVc5Vw%3D%3D%22%7D'
    html = requests.get(url,headers=headers.Headers('ins'))
    data = html.json()
    img_data_info = data['data']['user']['edge_owner_to_timeline_media']['edges']
    #构建图片url列表
    img_url_list = []
    for i in img_data_info:
        img_url = i['node']['display_url']
        img_url_list.append(img_url)
    #构建图片名称列表
    xxx = []
    id = '2210907972097'
    for img_url in img_url_list:
        img_data = requests.get(img_url).content
        img_name = img_url.split('?')[0].split('/')[-1].split('_')[0] + ".jpg"
        xxx.append(img_name)

        file_name = "D:\MySite\static\image\ins\\" + id
        #判断文件夹是否存在，不存在便新建一个
        if not os.path.exists(file_name):
            os.mkdir(file_name)
            with open(file_name+"\\" + img_name,"wb") as f:
                print('正在下载：' + img_name)
                f.write(img_data)
        else:
            pass

            
    # return insList