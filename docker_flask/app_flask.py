# -*- coding: utf-8 -*-
from flask import Flask,request
import json

app=Flask(__name__)

# 只接受POST方法访问
@app.route("/test",methods=["POST"])
def check():
    # 默认返回内容
    return_dict= {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断传入的json数据是否为空
    if request.get_data() is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的参数
    # get_Data=request.get_data()
    # 传入的参数为bytes类型，需要转化成json
    # get_Data=json.loads(get_Data)
    # with open("format_json.json", 'a') as write_f:
    #         write_f.write(json.dumps(get_Data, indent=4, ensure_ascii=False))

    # 对参数进行操作
    # return_dict['result']=get_Data
    # print(type(return_dict['result']))
    # return (get_Data)
    return json.dumps(return_dict, ensure_ascii=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)