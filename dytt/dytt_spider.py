'''
   @Author Ci Xin
   @E-mail sssrrr879@126.com
   @Phone 15849311404
   @Desc 主要做电影天堂数据的抓取
   @Date Create on 2018/11/4/004 20:24
'''

import re

# 使用Xpath的
from lxml import etree

import rules.dytt_rules as rules
# dytt类
from dytt.dytt_class import dytt as dt
from httpreq import sendRequest
from mysqldat.spider_log import log


class dytt():
    ## 初始化变量
    def __init__(self):
        self.__log = log('dytt')

    def find_by_classic(self, classic):
        '''
        :param classic: 分类名称
        :return: 返回当前分类下的电影
        '''
        send = sendRequest.send()
        if ''.__ne__(classic) and classic != None:
            for mrules in rules.rules:
                if classic.__eq__(mrules['classic']):

                    ### 开始抓取列表页的地址，获取列表页的信息
                    for lurl in mrules['url']:
                        ldata = send.send_req(url=lurl, method='GET', data='', clickurl='http://www.dytt8.net')
                        # print(ldata.text)
                        ltree = etree.HTML(ldata.text)
                        list_url = ltree.xpath(mrules['listurl'])
                        ltime = ltree.xpath(mrules['time'])

                        ### 处理列表的URL地址
                        # ulist = self.deal_url(url=str(ldata.url),urllist=list_url,start='http://s.ygdy8.com',result='http://s.ygdy8.com')
                        murl = str(ldata.url)
                        # print(murl)
                        for x in range(len(list_url)):
                            if mrules['classic'].__eq__('日韩电影'):  # http://www.dytt8.net
                                if murl.startswith('http://www.dytt8.net'):
                                    list_url[x] = 'http://www.dytt8.net' + list_url[x]
                            else:
                                if murl.startswith('http://www.ygdy8.net'):
                                    list_url[x] = 'http://www.ygdy8.net' + list_url[x]

                        ldata.close()

                        ### 处理时间
                        hot = list()  # 热度列表
                        for x in range(len(ltime)):
                            hot.append(re.findall('点击：(\d+)', ltime[x])[0])
                            ltime[x] = str(ltime[x]).replace('日期：', '', 1).replace('点击：0', '', 1)
                            # print(ltime[x])

                        ## 进入页面详情页，获取详情页内容
                        for x, purl in enumerate(list_url):
                            pdata = send.send_req(url=purl, method='GET', data='', clickurl=lurl)
                            # print(ldata.text)
                            ptree = etree.HTML(pdata.text)
                            ptit = ptree.xpath(mrules['page']['title'])
                            pdesc = ptree.xpath(mrules['page']['desc'])
                            pdownload = ptree.xpath(mrules['page']['download'])
                            if len(pdownload) > 0 and pdownload != None:
                                desc = ''.join(pdesc).replace(r'\u3000', '').replace(r'\xa0', '').replace(r'\r\n',
                                                                                                          '').strip()
                                # print('classic：%s,home: %s,time: %s,hot：%s,title: %s,desc: %s,down: %s'%(classic,mrules['main'],ltime[x],hot[x],ptit[0],desc,pdownload))
                                d = dt(classic=classic, home=mrules['main'], m_time=ltime[x], title=ptit[0], desc=desc,
                                       downloadurl=pdownload, hot=hot[x])
                                self.__log.print_log(home=mrules['main'], sql='',errorinfo='{0}——准备数据中，开始存入数据库'.format(ptit[0]))
                                d.save()

    ## 处理网址拼接的函数，（不一定留）
    def deal_url(self, url, urllist, start, result):
        '''
        :param url: 欲拼接的URL地址
        :param urllist: URL地址所属的列表
        :param start: 与URL地址拼接的字符串
        :param result: 完整的地址列表
        :return:
        '''
        ulist = list()
        for x in range(len(urllist)):
            if url.startswith(start):
                ulist[x] = result + urllist[x]
        return ulist

    ### 查找所有子模块下的视频
    def find_all(self):
        for rule in rules.rules:
            # print(rule['classic'])
            self.find_by_classic(rule['classic'])


if __name__ == '__main__':
    d = dytt()
    d.find_by_classic(classic='国内电影')
