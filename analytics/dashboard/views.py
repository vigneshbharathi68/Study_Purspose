from django.shortcuts import render
import pandas as pd
from .models import StateWiseTesting
from django.shortcuts import HttpResponse 
import json


# Create your views here.


def dashboard_home(request):    

    df = pd.read_csv('/home/chadura_tech/projects/vignesh_bharathi/Git_branch_study/jupyter_notebook/StatewiseTestingDetails.csv',sep=',')

#    # dateWise sorting

    def sort_date(q, x):
        if q is None:
            y = df.loc[df["Date"] == str(x)]
        else:
            y = df.loc[df[str(q)] == str(x)]

        json_records = y.reset_index().to_json(orient = 'records')
        data = json.loads(json_records)
        return data

    if request.method == "POST":
        datef=request.POST.get('date')
        statef = request.POST.get('state')
        data = sort_date(statef, datef)
        print(data)
         
    else:
        json_records = df.reset_index().to_json(orient = 'records')
        data = json.loads(json_records)
    
    

    #State wise sort

    # def state_sort(x):
    #     y = df.loc[df["State"]== str(x)]
    #     json_records = y.reset_index().to_json(orient = 'records')
    #     data = json.loads(json_records)
    #     return data

    # if request.method == "POST":
    #     statef = request.POST.get("state")
    #     data = state_sort(statef)

    # else:
    #     json_records = df.reset_index().to_json(orient = 'records')
    #     data = json.loads(json_records)




    
    return render(request, "download_home.html", {"df": data})