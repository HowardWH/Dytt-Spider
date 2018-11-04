'''
   @Author Ci Xin
   @E-mail sssrrr879@126.com
   @Phone 15849311404
   @Desc 这里是程序的入口
   @Date Create on 2018/11/4/004 20:24
'''

from multiprocessing.dummy import Pool as ThreadPool

from dytt.dytt_spider import dytt
from rules.dytt_rules import rules

if __name__ == '__main__':
    d = dytt()
    pool = ThreadPool(6)

    t = pool.map(d.find_all(), rules)
    pool.close()
    t.join()
