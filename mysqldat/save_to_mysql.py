'''
   @Author Ci Xin
   @E-mail sssrrr879@126.com
   @Phone 15849311404
   @Desc 操作数据库的类
   @Date Create on 2018/11/4/004 20:24
'''

import datetime

import pymysql

from mysqldat.pre_sql import sql as psql
from mysqldat.spider_log import log
from rules.database import database as ds


class Mysqlopertion:
    def __init__(self, source):
        self.__source = source
        self.__log = log(self.__source)

    def __get_conn__(self):

        for src in ds:
            if 'dytt'.__eq__(src[self.__source]):
                db = pymysql.connect(src[self.__source]['address'], src[self.__source]['acc'],
                                     src[self.__source]['pwd'], src[self.__source]['name'], charset='utf8')

                cursor = db.cursor()
                cursor.execute('SET NAMES utf8;')
                cursor.execute('SET CHARACTER SET utf8;')
                cursor.execute('SET character_set_connection=utf8;')
                return db, cursor

    def save_movie(self, sql, download, dsql):
        db, cursor = self.__get_conn__()

        if db != None:
            try:
                cursor.execute(sql)
                db.commit()
                self.__log.print_log(home=self.__source, sql=sql, errorinfo='')

                # 视频信息插入完成后，查找LAST_ID
                cursor.execute(psql['s_dytt_movies_lastid'])
                last_id = cursor.fetchone()[0]
                if last_id != 0:
                    for url in download:
                        downsql = str(dsql).replace('lastid', str(last_id)).replace('{durl}', str(url))
                        try:
                            cursor.execute(downsql)
                            db.commit()
                            self.__log.print_log(home=self.__source, sql=downsql, errorinfo='')

                            # # 下载地址插入完成后，查找LAST_ID（）,并修改视频信息中的下载地址ID
                            # cursor.execute(psql['s_dytt_download_lastid'])
                            # did = cursor.fetchone()[0]
                            # # usql = 'UPDATE `moviespider`.`dytt_movies` SET downloadid = %s WHERE mid = %s;' % (did, last_id)
                            # usql = psql['u_dytt_movies'].format(did, last_id)
                            # try:
                            #     cursor.execute(usql)
                            #     db.commit()
                            #     self.__log.print_log(home=self.__log,sql=usql,errorinfo='')
                            # except Exception as e:
                            #     db.rollback()
                            #     self.__log.print_log(home=self.__log, sql=usql, errorinfo=repr(e))
                        except Exception as e:
                            db.rollback()
                            self.__log.print_log(home=self.__source, sql=downsql, errorinfo=repr(e))
            except Exception as e:
                db.rollback()
                self.__log.print_log(home=self.__source, sql=sql, errorinfo=repr(e))

    def check_exists(self, tit):
        db, cursor = self.__get_conn__()
        e_sql = psql['s_dytt_movies_exits'].format(tit)

        try:
            cursor.execute(e_sql)
        except Exception as e:
            log.print_log(home=self.__source, sql=e_sql, errorinfo=repr(e))

        data = cursor.fetchone()
        if data[0] > 0:
            return True
        else:
            return False
