# !usr/bin/env python
# coding=utf-8
from concurrent.futures import ThreadPoolExecutor
import time
import requests
import sys

col_whith = 40 #每列宽度
keep_work = True

def value_get(code, row, col):

    while keep_work:
        r = requests.get("http://hq.sinajs.cn/list=s_%s" % (code,))
        res = r.text.split(',')
        if len(res) > 1:
            print("\033[" + str(row) +";" + str(col * col_whith) + "H" , end = '') #将光标移动到行列位置
            print(code + ": " + res[1] , end = '')

            if float(res[2]) < 0:
                print("\033[3;32m" , end= '') # 绿色
            else:
                print("\033[3;31m" , end= '') # 红色
	    
            if len(res[1]) < 6 :
                 print("\t", end = '')

            print("\t" + res[2] + "\033[0m", end = '   ')
			
            sys.stdout.flush()

        time.sleep(1)


print("\033c\033[?25l-") #清屏,隐藏光标
sys.stdout.flush()

#最多监控十支股票，可根据自己的数量更改
executor = ThreadPoolExecutor(max_workers=10) 

#添加要监控的股票，参数分别是股票代码，行，列 显示位置
executor.submit(value_get, ('sh000001'), 1, 0)
executor.submit(value_get, ('sz399001'), 1, 1)

executor.submit(value_get, ('sz002456'), 2, 0)
executor.submit(value_get, ('sz000009'), 2, 1)

executor.submit(value_get, ('sh600009'), 3, 0)

input()

keep_work = False

executor.shutdown(wait=False)

print("\033[?25h") # 显示光标
sys.stdout.flush()
