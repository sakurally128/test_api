# -*- coding: utf-8 -*-
# 开发团队   ：测试团队
# 开发人员   ：sakurally
# 开发时间   ：2019/9/3  11:52 
# 文件名称   ：login.PY
# 开发工具   ：PyCharm

import hashlib
import requests
import unittest

class Login(unittest.TestCase):
    def base_url(self):
        url = "https://wechat-test.changchangenglish.com"
        return url
    def parm_md5(self,data):
        m = hashlib.md5()
        m.update(data.encode(encoding='utf-8'))
        data_md5 = m.hexdigest()
        return data_md5

    def login(self):
        passwd = '123456'
        passwd_md5 = self.parm_md5(passwd)
        login_data = {
            'username': 'yuxia',
            'passwd': passwd_md5
        }
        r = requests.post(self.base_url() + '/api/admin/login', data=login_data)
        result = r.json()
        return result['data']['token']

if __name__ == '__main__':
    pass