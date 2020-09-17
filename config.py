# coding: utf-8

import sys
import os
import json

app_name_en = "txt_image"
app_name_cn = "Write Text To Image"
author_name = "Daniel Heimman(29405) and Siyi Dai(29245)"
author_org = "Hochschule Ravensburg Weingatyen"

base_dir = os.path.abspath(os.path.dirname(__file__))
home_dir = os.path.expanduser("~")
app_config_fp = os.path.join(home_dir, ".{}".format(app_name_en))
