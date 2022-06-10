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
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView, Response
from rest_framework.exceptions import APIException
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
        name = self.request.POST.get("name")
        pwd = self.request.POST.get("pwd")
        user = User.objects.get(username=name)
        if user is None:
            raise APIException("用户名不存在")
        is_correct = check_password(pwd, user.pwd)
        if not is_correct:
            raise APIException("密码错误...")
        resp = {
            "id": user.id,
            "user_name": user.username,
            "token": user.token
        }
        return Response(resp)
