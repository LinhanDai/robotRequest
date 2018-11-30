# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import websocket

import json
#Get request with no param
#127.0.0.1:8000/fl_robot/real_time_data/cmd_vel

def getCmdVel(request):
    # import logging
    # logging.basicConfig(level=logging.DEBUG, format='[%(thread)03d] %(asctime)-15s [%(levelname)s] %(message)s')
    # LOGGER = logging.getLogger('test')
    try:
        websocket.enableTrace(True)
        ws = websocket.create_connection("ws://192.168.1.94:9090/")
        dic = {"op": "subscribe", "id": "msgs/Odometry", "topic": "/odom"}
        json_dic = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ': '),
                               ensure_ascii=True)
        ws.send(json_dic)
        rev = ws.recv()
        ws.close()
        result = json.loads(rev)
        linear = result['msg']['twist']['twist']['linear']
        angular = result['msg']['twist']['twist']['angular']
        data = {"linear": linear, "angular": angular}
        errorCode = ""
        msg = "successed"
        successed = "true"
        cmd_vel = {"data": data, "errorCode": errorCode, "msg": msg, "successed": successed}
    except:
        data = {"angular":{
            "x":0,
            "y":0,
            "z":0
        },
        "linear":{
            "x":0,
            "y":0,
            "z":0
        }}
        errorCode = "error"
        msg = "failure send request"
        successed = "false"
        cmd_vel = {"data": data, "errorCode": errorCode, "msg": msg, "successed": successed}

    return JsonResponse(cmd_vel)














