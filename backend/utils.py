'''
utils.py: 工具类，包括分词，生成词云
'''

# baidu-lac分词: Lexical Analysis of Chinese
# https://github.com/baidu/lac
from LAC import LAC
from wordcloud import WordCloud
import time

## 获得分词结果
def getLAC(descSoup):

    lac = LAC(mode='lac')
    # lac.load_customization('./custom_lac.txt', sep=None)
    lac_res= lac.run(descSoup)
    return lac_res


## 获得词云
def getCloud(text):
    font_path = './font/msyh.ttf'

    wc = WordCloud(background_color="white",
                max_words=100,
    #                mask=alice_mask,    
    #                stopwords=stopwords,
                font_path=font_path) # 兼容中文字体，不然中文会显示乱码

    wc.generate(text)
    # 浏览器首次读取服务端的图片之后，再次读取同名图片，会直接从临时文件中读取，不再请求服务端。如果清除浏览器缓存，则图片更新
    # 用时间戳做名字解决
    prefix_cloud = str(int(time.time()))
    cloud_path = '../frontend/dist/static/' + prefix_cloud + 'wordcloud.png'
    wc.to_file(cloud_path)
    # 返回当前时间戳
    return prefix_cloud