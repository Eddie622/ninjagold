from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 1

    return render(request, 'index.html')

def process_money(request):
    options = ['Farm', 'House', 'Cave', 'Casino']

    for item in request.POST:
        if item in options: 
            coinRange = request.POST[item].split(',')
    
    request.session['gold'] += random.randint(int(coinRange[0]), int(coinRange[1]))

    return redirect('/')