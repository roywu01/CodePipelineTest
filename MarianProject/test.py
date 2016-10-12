# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import os,binascii
import sys
import base64
import hashlib
import datetime
import ujson as json
from Crypto import Random
from Crypto.Cipher import AES


@csrf_exempt
def test(request):
    _jsonob = {}
    _params = {
        'RETURNVALUE': 'N',
        'RETURNMSG': 'Unknown formation data.'
    }
    _params = json.dumps(_params)
    return HttpResponse(_params, content_type="application/json; charset=utf-8")