from ast import keyword
from itertools import count
from django.test import TestCase

# Create your tests here.
import re

keyword = 'helloworld kris'

# cunt = keyword.index(' ')

# if cunt == True:
#     keyword = '+'
# elif cunt == False:
#     pass
keyword = keyword.replace(' ', '+')

url = 'www.amzon.com/' + keyword

print(keyword)