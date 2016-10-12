# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import os,binascii
import sys

# 2016-10-04 新增備註
# CSRF = Cross-site Request Forgery
# Add @csrf_exempt to allow cross-site-request
# 跨域阻擋不只發生於post，get也會有相同問題

@csrf_exempt
def even(request):
	r1=json.loads(request.body)
	r2=r1["test"]
	r3=int(r2)
	if r3%2==0:
		return HttpResponse("是偶數喔")
	else:
		return HttpResponse("是奇數喔")
