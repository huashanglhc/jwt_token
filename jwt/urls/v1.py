#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：jwt_token 
@File    ：v1.py
@Author  ：WL
@Date    ：2022/6/10 19:59 
@Describe: 
"""
from django.urls import path
from jwt.apis.v1.user import Login, Register

urlpatterns = [
    path('user/register/', Register.as_view()),
    path('user/login/', Login.as_view())
]
