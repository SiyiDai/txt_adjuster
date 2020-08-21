# coding: utf-8

import sys
import os
import json

DEBUG = True
os.environ['DEBUG'] = str(DEBUG)


app_name_en = 'txt_image'
app_name_cn = 'Write Text To Image'
author_name = '高富帅'
author_org = '富甲一方科技公司'

font_size = [10, 30, 50]  # small / medium / large

base_dir = os.path.abspath(os.path.dirname(__file__))
home_dir = os.path.expanduser('~')
app_config_fp = os.path.join(home_dir, '.{}'.format(app_name_en))
