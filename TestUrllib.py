from urllib import request

# 导入urllib库的request模块 from urllib import request
# 请求URL req = request.Request(URL)
# 设置请求头 req.add_header(key,value)
# 使用响应对象输出数据print(resp.read().decode('utf-8'))

req = request.Request("https://www.baidu.com")

req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0")

resp = request.urlopen(req)

print(resp.read().decode("utf-8"))