# coding=utf-8
import urllib, urllib2, re, sys, urlparse, hashlib, datetime, string, time, socket
from bs4 import BeautifulSoup
import lib_get_url_classify

socket.setdefaulttimeout(20)
debug = 1

#reload(sys)
#sys.setdefaultencoding('utf-8')


#parse_page
#each_url = "http://www.smzdm.com/youhui/483995"
each_url = "http://www.mgpyh.com/recommend/6134047/"
domain = urlparse.urlparse(each_url).hostname

request = urllib2.Request(each_url)
request.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729)")
request.add_header('Referer', domain)
response = urllib2.urlopen(request)
page_html = BeautifulSoup(response.read())

print lib_get_url_classify.get_url_classify(page_html, domain)



