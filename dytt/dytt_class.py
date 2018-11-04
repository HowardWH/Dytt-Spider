'''
   @Author Ci Xin
   @E-mail sssrrr879@126.com
   @Phone 15849311404
   @Desc 主要做电影天堂数据的准备
   @Date Create on 2018/11/4/004 20:24
'''

import datetime

import mysqldat.save_to_mysql as ms
from mysqldat.pre_sql import sql as psql


class dytt:
    # 初始化变量
    def __init__(self, classic, home, m_time, title, desc, hot, downloadurl):
        self.__classic = classic
        self.__home = home
        self.__movie_time = m_time
        self.__title = title
        self.__desc = desc
        self.__hot = hot
        self.__download = downloadurl

    def save(self):
        '''
        保存数据到数据库
        :return:
        '''
        d = datetime.datetime.now().strftime('%Y-%m-%d')  # '%Y-%m-%d %H:%M:%S'
        t = datetime.datetime.now().strftime('%H:%M:%S')
        savesql = psql['c_dytt_movies'].format(self.__home, self.__classic, self.__title, self.__desc,
                                               self.__movie_time, self.__hot, d, t, d, t)

        downsql = psql['c_dytt_download'].format('lastid', '{durl}', d, t, d, t)

        ## 这里的参数 'dytt ' 是获取连接数据库需要的参数
        mo = ms.Mysqlopertion('dytt')

        ## 这里做存在性校验
        if mo.check_exists(self.__title) == False:

            ##  开始保存视频
            mo.save_movie(sql=savesql, download=self.__download, dsql=downsql)
            # print('视频：{0}，插入成功'.format(self.__title))
        else:
            print('【爬虫抓取日志:{0}】：视频：{1}已存在，不需插入！'.format(datetime.datetime.now(), self.__title))
