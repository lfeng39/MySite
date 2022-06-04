from django.shortcuts import get_object_or_404, render
from . import images
from . import ladyBug
# from django.template.defaulttags import register

# Create your views here.
# @register.filter('list')
# def range(value):
#     return range(value)

def nav(type):
    url = ['about', 'http://127.0.0.1:8888/JAL', 'img', 'lib', 'toys',]
    appTitle = ['About', 'Product', 'Img', 'Lib', 'Toys',]
    if type == 'url':
        return url
    elif type == 'appTitle':
        return appTitle
    else:
        pass

def index(request):
    
    imagesName = []
    for i in range(3):
        imagesName.append(images.creatImagesPath(i))

    indexApi = {
        'url': nav('url'),
        'appTitle': nav('appTitle'),
        'imagesName': imagesName,
        'num': ['0','1',2,3],
        
    }

    return render(request, 'index.html', indexApi)


def detail(request):

    detailApi = {
        'url': nav('url'),
        'appTitle': nav('appTitle'),

        }

    return render(request, '', detailApi)

def img(request):

    detailApi = {
        'url': nav('url'),
        'appTitle': nav('appTitle'),
        'pic': images.Pic_list(),
        'ins': images.testIns(),
        # 'amz_asin': images.amazon()[0],
        # 'amz_img': images.amazon()[1],
        }

    return render(request, 'img.html', detailApi)

def lib(request):
    page = 'index'
    title = 'lfeng'
    link = '<a style="color: black;" href="' + page + '">' + title + '</a>'

    sum_ = ladyBug.amz()

    lis_ad = sum_[0][0]
    len_ad = sum_[0][1]

    lis_hr = sum_[1][0]
    len_hr = sum_[1][1]

    lis_na = sum_[2][0]
    len_na = sum_[2][1]

    detailApi = {
        'url': nav('url'),
        'appTitle': nav('appTitle'),
        'pic': images.Pic_list(),
        'amz_ad': lis_ad,
        'amz_ad_count': len_ad,
        'amz_na': lis_na,
        'amz_na_count': len_na
        }

    return render(request, 'lib.html', detailApi)

def toys(request):
    toysApi = {
        '1': '2',
    }
    return render(request, 'toys.html', toysApi)

