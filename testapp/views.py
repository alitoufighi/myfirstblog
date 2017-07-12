# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# from django.http import HttpResponse
# Create your views here.

# def hello(request):
# 	text = "<b>Hello</b>"
# 	return HttpResponse(text)

def post_list(request):
	return render(request, 'testapp/post_list.html', {})