#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：jwt_token 
@File    ：user.py
@Author  ：WL
@Date    ：2022/6/10 20:02 
@Describe: 
"""
from rest_framework.views import APIView, Response


class Login(APIView):

    def post(self, request):
        return Response({"code": 200, "msg": "hello jwt token"})
