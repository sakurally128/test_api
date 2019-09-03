# coding:utf-8
import unittest
import ddt
import os
import requests,json
from common.base_api import SWRequests
from common.login import Login
from common import readexcel
from common import writeexcel

# 获取demo_api.xlsx路径
curpath = os.path.dirname(os.path.realpath(__file__))
testxlsx = os.path.join(curpath, "demo_api.xlsx")

# 复制demo_api.xlsx文件到report下
report_path = os.path.join(os.path.dirname(curpath), "report")
reportxlsx = os.path.join(report_path, "result.xlsx")

testdata = readexcel.ExcelUtil(testxlsx).dict_data()
@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.s = requests.session()
        # 如果有登录的话，就在这里先登录了
        Login().login()
        writeexcel.copy_excel(testxlsx, reportxlsx) # 复制xlsx

    @ddt.data(*testdata)
    def test_login(self, data):
        # 先复制excel数据到report
        res = SWRequests().send_requests(self.s, data)
        SWRequests().wirte_result(res, filename=reportxlsx)
        # 检查点 checkpoint
        check = data["checkpoint"]
        print("检查点->：%s"%check)
        # 返回结果
        res_text = res["text"]
        res_json = json.loads(res_text)
        print("返回实际结果->：%s"%res_text)
        # 断言
        self.assertTrue(check in res_text)

if __name__ == "__main__":
    unittest.main()