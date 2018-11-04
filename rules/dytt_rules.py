'''
   @Author Ci Xin
   @E-mail sssrrr879@126.com
   @Phone 15849311404
   @Desc 爬虫的抓取规则
   @Date Create on 2018/11/4/004 20:24
'''

rules = [
    {
        'classic': '最新影片',
        'url': ['http://www.ygdy8.net/html/gndy/dyzz/list_23_' + str(x) + '.html' for x in range(1, 184)],
        'main': '电影天堂',
        'listurl': '//a[not(contains(@href,"index"))and@class="ulink"]/@href',
        'time': '//table[@class="tbspan"]//font/text()',
        'page': {
            'title': '//div[@class="title_all"]/h1/font/text()',
            'desc': '//div[@id="Zoom"]//p/text()',
            'download': '//td[@bgcolor="#fdfddf"]/a/@href|//p/a/@href',
        }
    },
    {
        'classic': '国内电影',
        'url': ['http://www.ygdy8.net/html/gndy/china/list_4_' + str(x) + '.html' for x in range(1, 111)],
        'main': '电影天堂',
        'listurl': '//a[not(contains(@href,"index"))and@class="ulink"]/@href',
        'time': '//table[@class="tbspan"]//font/text()',
        'page': {
            'title': '//div[@class="title_all"]/h1/font/text()',
            'desc': '//div[@id="Zoom"]//p/text()',
            'download': '//td[@bgcolor="#fdfddf"]/a/@href|//p/a/@href',
        }
    },
    {
        'classic': '欧美电影',
        'url': ['http://www.ygdy8.net/html/gndy/oumei/list_7_' + str(x) + '.html' for x in range(1, 204)],
        'main': '电影天堂',
        'listurl': '//a[not(contains(@href,"index"))and@class="ulink"]/@href',
        'time': '//table[@class="tbspan"]//font/text()',
        'page': {
            'title': '//div[@class="title_all"]/h1/font/text()',
            'desc': '//div[@id="Zoom"]//p/text()',
            'download': '//td[@bgcolor="#fdfddf"]/a/@href|//p/a/@href',
        }
    },
    {
        'classic': '日韩电影',
        'url': ['http://www.dytt8.net/html/gndy/rihan/list_6_' + str(x) + '.html' for x in range(1, 35)],
        'main': '电影天堂',
        'listurl': '//a[not(contains(@href,"index"))and@class="ulink"]/@href',
        'time': '//table[@class="tbspan"]//font/text()',
        'page': {
            'title': '//div[@class="title_all"]/h1/font/text()',
            'desc': '//div[@id="Zoom"]//p/text()',
            'download': '//td[@bgcolor="#fdfddf"]/a/@href|//p/a/@href',
        }
    },
    {
        'classic': '日韩电视',
        'url': ['http://www.ygdy8.net/html/tv/rihantv/list_8_' + str(x) + '.html' for x in range(1, 40)],
        'main': '电影天堂',
        'listurl': '//a[not(contains(@href,"index"))and@class="ulink"]/@href',
        'time': '//table[@class="tbspan"]//font/text()',
        'page': {
            'title': '//div[@class="title_all"]/h1/font/text()',
            'desc': '//font[@color="#0000ff"]/strong/text()|//font[@color="#0000ff"]/text()',
            'download': '//td[@bgcolor="#fdfddf"]/a/@href|//p/a/@href',
        }
    },
    {
        'classic': '华语电视',
        'url': ['http://www.ygdy8.net/html/tv/hytv/list_71_' + str(x) + '.html' for x in range(1, 22)],
        'main': '电影天堂',
        'listurl': '//a[not(contains(@href,"index"))and@class="ulink"]/@href',
        'time': '//table[@class="tbspan"]//font/text()',
        'page': {
            'title': '//div[@class="title_all"]/h1/font/text()',
            'desc': '//div[@id="Zoom"]//p/text()',
            'download': '//td[@bgcolor="#fdfddf"]/a/@href|//p/a/@href',
        }
    },
    {
        'classic': '欧美电视',
        'url': ['http://www.ygdy8.net/html/tv/oumeitv/list_9_' + str(x) + '.html' for x in range(1, 16)],
        'main': '电影天堂',
        'listurl': '//a[not(contains(@href,"index"))and@class="ulink"]/@href',
        'time': '//table[@class="tbspan"]//font/text()',
        'page': {
            'title': '//div[@class="title_all"]/h1/font/text()',
            'desc': '//div[@id="Zoom"]/span/td/p/text()|//div[@id="Zoom"]/span/td/text()',
            'download': '//td[@bgcolor="#fdfddf"]/a/@href|//p/a/@href',
        }
    },
    {
        'classic': '最新综艺',
        'url': ['http://www.ygdy8.net/html/zongyi2013/list_99_' + str(x) + '.html' for x in range(1, 151)],
        'main': '电影天堂',
        'listurl': '//a[not(contains(@href,"index"))and@class="ulink"]/@href',
        'time': '//table[@class="tbspan"]//font/text()',
        'page': {
            'title': '//div[@class="title_all"]/h1/font/text()',
            'desc': '//div[@id="Zoom"]//p/text()',
            'download': '//td[@bgcolor="#fdfddf"]/a/@href|//p/a/@href',
        }
    },
    {
        'classic': '旧版综艺',
        'url': ['http://www.ygdy8.net/html/2009zongyi/list_89_' + str(x) + '.html' for x in range(1, 70)],
        'main': '电影天堂',
        'listurl': '//a[not(contains(@href,"index"))and@class="ulink"]/@href',
        'time': '//table[@class="tbspan"]//font/text()',
        'page': {
            'title': '//div[@class="title_all"]/h1/font/text()',
            'desc': '//div[@id="Zoom"]//p/text()',
            'download': '//td[@bgcolor="#fdfddf"]/a/@href|//p/a/@href',
        }
    },
    {
        'classic': '动漫资源',
        'url': ['http://www.ygdy8.net/html/dongman/list_16_' + str(x) + '.html' for x in range(1, 8)],
        'main': '电影天堂',
        'listurl': '//a[not(contains(@href,"index"))and@class="ulink"]/@href',
        'time': '//table[@class="tbspan"]//font/text()',
        'page': {
            'title': '//div[@class="title_all"]/h1/font/text()',
            'desc': '//div[@id="Zoom"]//p/text()',
            'download': '//td[@bgcolor="#fdfddf"]/a/@href|//p/a/@href',
        }
    }
]
