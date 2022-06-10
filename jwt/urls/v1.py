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
from jwt.apis.v1.user import Login
from jwt.apis.v1.user import Register
from jwt.apis.v1.user import Order
from jwt.apis.v1.user import Goods

urlpatterns = [
    path('user/register/', Register.as_view()),
    path('user/login/', Login.as_view()),
    path('orders/', Order.as_view()),
    path('goods/', Goods.as_view()),
]
