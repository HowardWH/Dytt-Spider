'''
   @Author Ci Xin
   @E-mail sssrrr879@126.com
   @Phone 15849311404
   @Desc 数据库的日志类
   @Date Create on 2018/11/4/004 20:24
'''

import datetime as date

import pymysql

from mysqldat.pre_sql import sql as psql
from rules.database import database as ds


class log:
    # 初始化变量
    def __init__(self, source):
        self.__source = source

    def __get_conn__(self):
        '''
        获得数据库连接
        :return:
        '''

        for src in ds:
            if 'dytt'.__eq__(src[self.__source]):
                db = pymysql.connect(src[self.__source]['address'], src[self.__source]['acc'],
                                     src[self.__source]['pwd'], src[self.__source]['name'], charset='utf8')

                cursor = db.cursor()
                cursor.execute('SET NAMES utf8;')
                cursor.execute('SET CHARACTER SET utf8;')
                cursor.execute('SET character_set_connection=utf8;')
                return db, cursor

    def print_log(self, home, sql, errorinfo):
        '''
        :param home: 抓取的网站
        :param sql: 出错的SQL语句，没有可以为''
        :param errorinfo: 错误信息
        :return:
        '''
        home1 = 'other'
        if 'dytt'.__eq__(home) or '电影天堂'.__eq__(home):
            home1 = '电影天堂'
        db, cursor = self.__get_conn__()
        lsql = psql['c_dytt_log'].format(home1, sql, errorinfo, date.datetime.now())

        try:
            cursor.execute(lsql)
            db.commit()
            print('【爬虫抓取日志:{0}】：日志插入执行成功，SQL是：{1},信息是：{2}'.format(date.datetime.now(), sql, errorinfo))
        except Exception as e:
            db.rollback()
            print('【爬虫抓取日志:{0}】：日志插入失败,SQL是：{1}错误信息：{2}'.format(date.datetime.now(),sql,repr(e)))
