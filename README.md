# miniStock

命令行实时显示股票价格，让老板不知道你是在调Bug还是在 ... ...

![](https://shyboy.oss-cn-shenzhen.aliyuncs.com/readonly/miniStock.png)

## 添加自己关注的股票

	#添加要监控的股票，参数分别是：股票代码，行，列 显示位置
	executor.submit(value_get, ('sh000001'), 1, 0)
	
## 启动软件

	python miniStock.py