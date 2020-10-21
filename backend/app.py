from flask import Flask
from flask import render_template, jsonify, request
from flask_cors import CORS

from crawler import *

app = Flask(__name__,
            static_folder = "../frontend/dist/static",
            template_folder = "../frontend/dist")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# 获得词云的接口
@app.route('/api/cloud/', methods=['GET'])
def cloud():
    '''
    /api/cloud/?keyword=&city=&salary=&industry=
    e.g.:
        http://127.0.0.1:5000/api/cloud/?keyword=数据挖掘&city=010&salary=&industry=
    '''
    keyword = request.args.get('keyword') # 职业
    city = request.args.get('city') # 城市
    cities = None if city == '不限城市' else city
    salary = request.args.get('salary')  # 薪资
    salary = None if salary == '不限工资' else salary
    industry = request.args.get('industry') # 行业
    industry = None if industry == '不限行业' else industry

    links = getJobLinks(keyword, cities, salary, industry)
    text = getJobInfos(links)
    if len(text) == 0:
        return jsonify({'info':'none result'})
    else:
        tm = getCloud(text) # 时间文件名前缀
    return jsonify({'info':'success', 'prefix':tm})

# 所有路径重定向到主页
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run()