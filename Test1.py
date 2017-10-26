from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request('http://huochepiao.114piaowu.com/train/ydTrainZdz_searchAdapter.action')

postData = parse.urlencode({
    'fromStation':'上海',
    'godateStr':'2016-09-07',
    'searchType':0,
    'toStation':'广州'
}).encode('utf-8')

req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0")

resp = urlopen(req,data = postData)

print(resp.read().decode('utf-8'))