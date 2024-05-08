from django.http.response import JsonResponse
from django.shortcuts import render
from random import randrange
from utils.sheets import read_google_sheet

def dashboard(request):
    data = read_google_sheet()
    return render(request, 'dashboard.html', {'data': data})

def actualizar_datos(request):
    data = read_google_sheet()
    return JsonResponse(data)

def index(request):
    return render(request, 'index.html')

def get_chart(request):
    
    serie = []
    counter=0
    while (counter<7):
        serie.append(randrange(100, 400))
        counter += 1
    chart = {
        'tooltip':{
            'show': True,
            'trigger': "axis",
            'trigerOn': "mousemove|click"
        },
        'xAxis':[
            {
                'type':"category",
                'data':["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
            }
        ],
        'yAxis':[
            {
                'type':'value'
            }
        ],
        'series':[
            {
                'data': serie,
                'type': "line"
            }
        ]
    }
    return JsonResponse(chart)
