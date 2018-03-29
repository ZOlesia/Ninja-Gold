# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import datetime
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'messages' not in request.session:
        request.session['messages'] = []
    if 'length' not in request.session:
		request.session['length'] = 0
    return render(request, 'golds/index.html')

def proccess(request):
    if request.method == "POST":
        newMessage = {}
        newMessage['building'] = str(request.POST['building'])
        newMessage['today'] = datetime.datetime.now().strftime("%I:%M %p, %b %m %Y")
        newMessage['play'] = 'Earned'
        newMessage['color'] = 'blue'
        if newMessage['building'] == 'farm':
            newMessage['number'] = random.randrange(10, 21)
        if newMessage['building'] == 'cave':
            newMessage['number'] = random.randint(5, 10)
        if newMessage['building'] == 'house':
            newMessage['number'] = random.randint(2, 5)
        if newMessage['building'] == 'casino':
            newMessage['number'] = random.randint(-50, 50)
            if newMessage['number'] >= 0:
                newMessage['msgs'] = 'YEAH!!!'
                newMessage['play'] = 'Won'
                newMessage['color'] = 'violet'
            elif newMessage['number'] < 0:
                newMessage['msgs'] = '...OUCH...'
                newMessage['play'] = 'Lost'
                newMessage['color'] = 'red'
        request.session['messages'].append(newMessage)
        request.session.modified = True
        request.session['gold'] = request.session['gold'] + newMessage['number']
        return redirect('/')
    else:
        return redirect('/')

def reset(request):
    del request.session['gold']
    del request.session['messages']
    return redirect(index)

    