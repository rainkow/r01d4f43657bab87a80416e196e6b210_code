# coding=utf-8
import MySQLdb, urllib, urllib2, re, sys, urlparse, hashlib, datetime, string, time, socket
import socket

socket.setdefaulttimeout(30)

#get increased content
def get_increased_contents(cur_jp, cur_local, conn_jp, conn_local):
    cur_jp.execute("select * from dxb_contents where status=1")
    for row in cur_jp.fetchall():
        #if url in yun_db , status = 2 ;else status = 0
        url_hash = row["url_hash"]
        cur_local.execute('select * from dxb_contents where url_hash = \'' + url_hash +'\'')
        cnt = 0
        for each_cur in cur_local.fetchall():
            cnt = cnt+1
        if cnt == 0:
            #cnt = 0 means first in yun_db
            cur_local.execute("replace into dxb_contents (url_hash, url	, title	,content,category,ht,quan,b2c,target_img,target_url,status) values('%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')" % (row["url_hash"], row["url"],row["title"],row["content"],row["category"],row["ht"],row["quan"],row["b2c"],row["target_img"],row["target_url"], row["status"]))
        else:
            cur_local.execute("replace into dxb_contents (url_hash, url	, title	,content,category,ht,quan,b2c,target_img,target_url,status) values('%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')" % (row["url_hash"], row["url"],row["title"],row["content"],row["category"],row["ht"],row["quan"],row["b2c"],row["target_img"],row["target_url"], 2))
        conn_local.commit()
        cur_jp.execute("update dxb_contents set status = 1 where url_hash = '%s'" % (row["url_hash"]))
        conn_jp.commit()
    return

#DB connection
conn_jp=MySQLdb.connect(host='106.186.24.246',user='root',passwd='eysXpFxw0iH01hyhyTLY',db='fangyuan',port=3306, charset='utf8')
#for aliyun
conn_local=MySQLdb.connect(host='rdsr3ivajr3ivaj.mysql.rds.aliyuncs.com',user='dbczp8tc8ls7pj28',passwd='8848yangmao_hao',db='diaoxb',port=3306, charset='utf8')

#for my computer
#conn_local=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='fangyuan',port=3306, charset='utf8')

cur_jp = conn_jp.cursor(MySQLdb.cursors.DictCursor)
cur_local = conn_local.cursor(MySQLdb.cursors.DictCursor)

get_increased_contents(cur_jp, cur_local, conn_jp, conn_local)


#close DB connection
cur_jp.close()
conn_jp.close()
cur_local.close()
conn_local.close()
