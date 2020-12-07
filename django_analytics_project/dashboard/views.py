from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import Order,Download
from django.core import serializers
from json import dumps
from django.db.models import Sum
# Create your views here.

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def combine_chart(request):
    queryset = Download.objects.values('date')
    queryset_downloads = Download.objects.values('daily_downloads')


    # labels and data will give labels and daily download count for the chart
    labels = []
    data = []
    for entry, entry_1 in zip(queryset, queryset_downloads):
        labels.append(str(entry['date']))
        data.append(entry_1['daily_downloads'])


    # This will give the total downloads
    daily = []
    total = []
    for x in data:
        daily.append(x)
        total.append(sum(daily))
    
    print('labels.......................................',labels)
    print('daily.......................................',daily)
    print('Total.......................................',total)
    
    
    dict_data={
        
        'labels': labels,
        'data': data,
        'total':total,
    }
    
    print(dict_data)
    dataJSON = dumps(dict_data)
    print("datajson",dataJSON)
    
    return render(request, 'combine_chart.html', {'data': dataJSON})


def pivot_data(request):
    dataset = Order.objects.all()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",dataset)
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def send_dictionary(request):
    # creating a data dictionary
    dataDictionary = {
        "hello" : "World",
        "vignesh" : "Bharathi",
        "ABC" : 123,
         456 : "abc",
         "list" : ['vignesh', 4, 'JS developer'],
         "dictionary" : {'you': 'can', 'send' : 'anything', 3:1}
    }

    #dump data
    dataJSON = dumps(dataDictionary)
    print(dataJSON)
    return render(request, 'landing.html', {'data': dataJSON})

def opposites(request): 
    # create data dictionary 
    data = [ 
        ["Laugh", "Cry"], 
        ["Even", "Odd"], 
        ["Hot", "Cold"], 
        ["Light", "Dark"], 
        ["Opposite", "Same"], 
        ["Far", "Near"], 
        ["Give", "Take"], 
        ["Night", "Day"], 
        ["Import", "Export"], 
        ["Hard", "Easy"], 
        ["Never", "Always"], 
        ["Late", "Early"], 
        ["Less", "More"], 
        ["Male", "Female"], 
        ["Happiness", "Sadness"], 
        ["Fast", "Slow"], 
        ["Old", "Young"], 
        ["Boy", "Girl"], 
        ["Up", "Down"], 
        ["Left", "Right"], 
        ["Rich", "Poor"], 
        ["Love", "Hate"], 
        ["Inside", "Outside"], 
        ["Bad", "Good"], 
        ["Short", "Tall"], 
    ] 
    data = dumps(data)
    print(data) 
    return render(request, "opposites.html", {"data2": data}) 

def download_chart_view(request):
    return render(request, 'download_chart.html')

def download_chart(request):
    
    queryset = Download.objects.values('date')
    queryset_downloads = Download.objects.values('daily_downloads')


    # labels and data will give labels and daily download count for the chart
    labels = []
    data = []
    for entry, entry_1 in zip(queryset, queryset_downloads):
        labels.append(str(entry['date']))
        data.append(entry_1['daily_downloads'])


    # This will give the total downloads
    daily = []
    total = []
    for x in data:
        daily.append(x)
        total.append(sum(daily))
    
    print('Total.......................................',total)
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
        'total':total,
    })


def all_object(request):
    download_json = serializers.serialize("json", Download.objects.all().order_by('daily_downloads'))

    print(download_json)
    return JsonResponse(download_json)




