from django.shortcuts import render, redirect
import datetime
import random


def index(request):
    
    if not 'gold' in request.session:
        request.session['gold']=0
        request.session['message']=""
    return render(request,'app5/index.html')
def process(request):
    dictionary={'farm':[10,20],'cave':[5,20],'house':[0,50],'casino':[-50,50]}
    x=datetime.datetime.now()
    for key in dictionary:
        if key == request.POST['location']:
            
            temp=random.randint(dictionary[key][0], dictionary[key][1])
            request.session['gold']+= temp
            if temp>=0:
                request.session['message']+='<span class="gold">Earned '+str(temp)+'golds from the '+key+'! at '+x.strftime("%Y/%m/%d %I:%M %p")+'</span><br>'
            else:
                request.session['message'] +='<span class="red">Ouch!Take '+str(temp*-1)+'golds from the '+key+'! at '+x.strftime("%Y/%m/%d %I:%M %p")+'</span><br>'
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')