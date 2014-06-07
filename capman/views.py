from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

# Create your views here.

def index(request):
    context = RequestContext(request)
    return render_to_response('sbadmin/index.html', [], context)