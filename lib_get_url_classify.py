# coding=utf-8
import urllib, urllib2, re, sys, urlparse, hashlib, datetime, string, time, socket
from bs4 import BeautifulSoup

socket.setdefaulttimeout(20)
debug = 1

global_map = {
'未分类':0, 
'优惠券' : 1, 
'家用电器':2,
'百货办公':3,
'服装鞋包':4,
'汽车用品':5,
'海淘专区':6,
'玩具母婴':7,
'电脑数码':8,
'经验分享':9,
'运动户外':10,
'食品保健':11,
'个护化妆':12, 
'礼品钟表':13, 
'图书音像':14, 
'家居家装':15, 
}

#key = domain ,elem = rules of htmlparser
classify_rules = {
'www.smzdm.com': ['div', ['class','crumbsCate']], 
'www.mgpyh.com':['ol', ['class', 'breadcrumb']], 
}

#key = domain ;  first elements = tag in site ; snd elem = map in global
classify_map = {
'www.smzdm.com': [
['电脑数码', '电脑数码'], ['家用电器', '家用电器'], ['运动户外', '运动户外'], ['服饰鞋包', '服装鞋包'], ['个护化妆', '个护化妆'], 
['母婴用品', '玩具母婴'], ['日用百货', '百货办公'], ['食品保健', '食品保健'], ['礼品钟表', '礼品钟表'], ['图书音像', '图书音像'], 
['玩模乐器', '玩具母婴'], ['家居家装', '家居家装'], ['办公设备','百货办公'],['汽车用品', '汽车用品'], ['其他', '未分类'] 
], 
'www.mgpyh.com':[
['相机、数码配件', '电脑数码'], 
], 
}

def get_url_classify(page_html, domain):
    #parse mypos
    mypos_block = page_html.find_all(name=classify_rules[domain][0], attrs ={classify_rules[domain][1][0] : classify_rules[domain][1][1]})
    mypos_str = str(mypos_block)
    for classify_name in classify_map[domain]:
        if mypos_str.find(classify_name[0])!= -1:
            return global_map[classify_name[1]]
    return -1
