from django.shortcuts import render
import pandas as pd
from .models import StateWiseTesting
from django.shortcuts import HttpResponse 
import json

from django.views import View
from .models import StateWiseTesting 


# Create your views here.


def dashboard_home(request):    

    df = pd.read_csv('/home/chadura_tech/projects/vignesh_bharathi/Git_branch_study/jupyter_notebook/StatewiseTestingDetails.csv',sep=',')

    json_records = df.reset_index().to_json(orient = 'records')
    data = json.loads(json_records)

#    # dateWise sorting

    def sort_date(x):
        y = df.loc[df["Date"] == str(x)]
        json_records = y.reset_index().to_json(orient = 'records')
        data = json.loads(json_records)
        return data

    def sort_state(x):
        y = df.loc[df["State"] == str(x)]
        json_records = y.reset_index().to_json(orient = 'records')
        data = json.loads(json_records)
        return data

    if request.method == "POST":
        datef=request.POST.get('date')
        statef = request.POST.get('state')
        
        print(statef)
        if datef:
            data = sort_date(datef)
        if statef:
            data = sort_state(statef)


    
    return render(request, "download_home.html", {"df": data})


class dataView(View):
    template_name = 'data.html'
    model = StateWiseTesting
    