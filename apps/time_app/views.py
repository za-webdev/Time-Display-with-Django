# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from time import gmtime,strftime
from django.contrib import messages
from django.utils.crypto import get_random_string

def index(request):
	context={

		'date':strftime("%b %d %Y",gmtime()),
		'time':strftime(" %I:%M %p",gmtime())
	}


	return render(request,"time_app/index.html",context)
