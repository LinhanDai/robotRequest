# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import websocket

import json

#Post 请求demo,还没写完，  功能是设置一个导航路径  其他和real_time_data/views的请求一样
#就是组合数据发送过去得到返回，然后解析，组成json发送回去
#127.0.0.1:8000/fl_robot/cmd/navigate   地址请求
#发送{
#   "destination":{
#     "angle":100,
#     "gridPosition":{
#       "x":100,
#       "y":100
#     }
#   }
# }
def setNavigateGoal(request):

    try:
        if request.method == 'POST':
            postBody = request.body
            json_data = json.loads(postBody)
            angle = json_data['destination']['angle']
            x = json_data['destination']['gridPosition']['x']
            y = json_data['destination']['gridPosition']['y']
            dic = {"op": "public", "id": "geometry_msgs/PoseStamped", "topic": "/move_base/current_goal"}
    except:
        pass

    return JsonResponse(dic)