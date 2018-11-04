'''
   @Author Ci Xin
   @E-mail sssrrr879@126.com
   @Phone 15849311404
   @Desc 网页操作类
   @Date Create on 2018/11/4/004 20:24
'''

import random
import time

import requests as req

# 获取User-Agent的包
from ualib.pyua import ua


class send():
    # 发送GET请求
    def send_req(self, url, method, data, clickurl):
        '''

        :param url: 欲发送请求的URL地址
        :param method: 发送请求的方式
        :param data: 发送的数据
        :param clickurl: 可不填，给值为''即可
        :return:
        '''
        rua = ua[random.randint(0, len(ua) - 1)]
        header = {
            'User-Agent': rua,
            'Referer': clickurl
        }
        # print(header)

        sleep = random.randint(1, 3)
        time.sleep(sleep)
        sdata = ''
        if 'GET'.__eq__(method):
            try:
                sdata = req.get(url=url, headers=header)
            except Exception as e:
                self.send_req(url, method, data, clickurl)
        elif 'POST'.__eq__(method):
            try:
                sdata = req.post(url=url, headers=header, data=data)
            except Exception as e:
                self.send_req(url, method, data, clickurl)
        sdata.encoding = req.utils.get_encodings_from_content(str(sdata.content))[0]
        # print(sdata.encoding)
        if sdata.status_code != 200:
            self.send_req(url, method, data, clickurl)
        return sdata
