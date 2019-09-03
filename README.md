```

# test_api

##环境准备：
  python3.7、requests、xlrd、openpyxl、HTMLTestRunner_ap  
  
##目前实现功能
  1.封装requests请求方法
  2.在excel填写接口请求参数
  3.运行完后，重新生成一个excel报告，结果写入excel
  4.用unittest+ddt数据驱动模式执行
  5.HTMLTestRunner生成可视化的html报告
  6.对于没有关联的单个接口请求是可以批量执行的，需要登录的话写到setUpclass里的session里保持cookies
  
##目前已知的缺陷
  1.接口请求参数名有重复的，目前未处理，如key1=value1&key1=value2,两个key都一样，这种需要用元组存储，目前暂时未判断
  2.生成的excel样式未处理，后期慢慢优化样式
```

