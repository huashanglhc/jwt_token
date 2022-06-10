#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：jwt_token 
@File    ：user.py
@Author  ：WL
@Date    ：2022/6/10 20:02 
@Describe: 
"""
import uuid
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView, Response
from jwt.models import User


class Register(APIView):

    def post(self, request):
        user_name = self.request.POST.get("name")
        pwd = self.request.POST.get("pwd")
        pwd = make_password(pwd)
        user = User.objects.create(
            username=user_name,
            pwd=pwd,
            token=str(uuid.uuid4())
        )

        resp = {
            "user_id": user.id,
            "token": user.token,
            "user_name": user.username
        }
        return Response(resp)


class Login(APIView):

    def post(self, request):
        name = self.request.DATA.get("name")
        pwd = self.request.DATA.get("pwd")

        return Response({"code": 200, "msg": "hello jwt token"})
