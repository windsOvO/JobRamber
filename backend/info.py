'''
info.py: 存储url加载的筛选条件信息，和其他一些信息如代理IP，headers
'''

# 网站前缀
prefix = 'https://www.liepin.com'

# 爬取的职位列表
jobs = ['数据挖掘', '图像算法工程师', 'java后端', '互联网产品经理']

# 工作地区: 编号
all_cities = {'北京':'010', '上海':'020', '深圳':'050090', '广州':'050020', '武汉':'170020', '杭州':'070020'}

# 行业
industries = {
    '互联网/电商':'&industryType=industry_01&industries=040',
    '游戏产业': '&industryType=industry_01&industries=420',
    '计算机软件': '&industryType=industry_01&industries=010',
    'IT服务': '&industryType=industry_01&industries=030',
    '电子/芯片/半导体': '&industryType=industry_02&industries=050',
    '通信业': '&industryType=industry_02&industries=060',
    # '计算机/网络设备': '&industryType=industry_02&industries=020',
}

# 薪资, [10-15, 15-20, 20-30, 30-50, 50-100, 100-], 单位w
salary_segment = {'10-15':'10%2415', '15-20':'15%2420', '20-30':'20%2430', '30-50':'30%2450', '50-100':'50%24100', '100-':'100%24999'}

'''
反反爬虫
'''

# setting headers
Cookie = 'Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1602765614; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1602644098; __session_seq=75; __uv_seq=8; bad1b2d9162fab1f80dde1897f7a2972_gr_cs1=1b02acfb641ace891a667e00ad0d9493; bad1b2d9162fab1f80dde1897f7a2972_gr_last_sent_cs1=1b02acfb641ace891a667e00ad0d9493; bad1b2d9162fab1f80dde1897f7a2972_gr_last_sent_sid_with_cs1=9226d208-84f4-4598-a4fc-cfa1e7d7654a; bad1b2d9162fab1f80dde1897f7a2972_gr_session_id=9226d208-84f4-4598-a4fc-cfa1e7d7654a; bad1b2d9162fab1f80dde1897f7a2972_gr_session_id_9226d208-84f4-4598-a4fc-cfa1e7d7654a=true; gr_user_id=b747b322-7e79-4418-b864-a3b5b0efa549; imClientId=1f9e7521c1e2d88f70c5cdd4c6549f7f; imClientId_0=1f9e7521c1e2d88f70c5cdd4c6549f7f; imId=1f9e7521c1e2d88fa77c18111a6bff96; imId_0=1f9e7521c1e2d88fa77c18111a6bff96; user_name=%E6%9B%B9%E6%B5%AA; user_photo=5d5513d34ebeb1284dfc774b07u.png; UniqueKey=1b02acfb641ace891a667e00ad0d9493; access_system=C; lt_auth=s%2B8CMicHyw37sHPfgGAK4K8biNyuU2zMpSgOhRFU1de%2BXfPl4PbnRwyHp7cCxAMhlxJ8f8ULN7D8Mu77zHpL7UUUwGqnn4CxtPyk0HsCUeVkHuyflMXuqs7QQJslrXg6ykpgn2si; JSESSIONID=431844E6ABCE85DD09549927B47C8702; fe_im_socketSequence_0=4_4_4; imApp_0=1; __tlog=1602644097413.20%7C00000000%7CR000000075%7C00000000%7C00000000; grwng_uid=2a452016-38f3-4d61-8d89-bfb47db20379; inited_user=371b1c5fc5745aa8981bb9c4f71a5b6c; user_roles=0; fe_se=-1602646644354; __uuid=1602644097412.43; vas_userc_exixt=371b1c5fc5745aa8981bb9c4f71a5b6c; new_user=false; c_flag=e37e8475577a39656b7a8d7d72964014; need_bind_tel=false; __s_bid=eb9baa7fa228d53ebfd609d3ec9894963b85'
User_Agent = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60', 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0', 'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)']
Referer = 'https://www.c.liepin.com/'

# setting proxies
'''
全网代理IP：http://www.goubanjia.com/
快代理：https://www.kuaidaili.com/?utm_source=bdtg&utm_campaign=a10a1&utm_medium=a10
西祠代理：https://www.xicidaili.com/nn/

查看ip：http://icanhazip.com
'''

proxiesIP = [
    '161.117.14.162',
    '161.117.33.11',
    '113.57.237.18',
    '198.11.172.83',
    '198.13.32.127',
    '198.11.172.171',
    '3.34.51.207',
    '47.57.83.141',
    '47.240.245.139',
    '47.240.167.159',
    '95.179.167.117',
    '161.117.196.186',
    '47.57.88.80',
    '47.90.49.173',
    '8.210.11.1',
    '47.57.17.163',
]