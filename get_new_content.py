# coding=utf-8
import MySQLdb, urllib, urllib2, re, sys, urlparse, hashlib, datetime, string, time, socket
import socket
from bs4 import BeautifulSoup

socket.setdefaulttimeout(30)

#get increased content
def get_increased_contents(cur_jp, cur_local, conn_jp, conn_local):
    cur_jp.execute("select * from dxb_contents where status=0")
    for row in cur_jp.fetchall():
        cur_local.execute("replace into dxb_contents (url_hash, url	, title	,content,category,ht,quan,b2c,target_img,target_url,status) values('%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')" % (row["url_hash"], row["url"],row["title"],row["content"],row["category"],row["ht"],row["quan"],row["b2c"],row["target_img"],row["target_url"], row["status"]))
        conn_local.commit()
        cur_jp.execute("update dxb_contents set status = 1 where url_hash = '%s'" % (row["url_hash"]))
        conn_jp.commit()
    return

#DB connection
conn_jp=MySQLdb.connect(host='106.186.24.246',user='root',passwd='eysXpFxw0iH01hyhyTLY',db='fangyuan',port=3306, charset='utf8')
#for aliyun
conn_local=MySQLdb.connect(host='127.0.0.1',user='root',passwd='dbczp8tc8ls7pj28/8848yangmao_hao',db='fangyuan',port=3306, charset='utf8')

#for my computer
#conn_local=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='fangyuan',port=3306, charset='utf8')

#获取连接上的字典cursor，注意获取的方法，使用字典cursor取得结果集
cur_jp = conn_jp.cursor(MySQLdb.cursors.DictCursor)
cur_local = conn_local.cursor(MySQLdb.cursors.DictCursor)

get_increased_contents(cur_jp, cur_local, conn_jp, conn_local)


#close DB connection
cur_jp.close()
conn_jp.close()
cur_local.close()
conn_local.close()
