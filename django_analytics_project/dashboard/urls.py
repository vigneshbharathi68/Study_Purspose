from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data/', views.pivot_data, name="pivot_data"),
    path('js-view/', views.send_dictionary, name='send_dictionary'),
    path('js-opp/', views.opposites, name='opposites'),
    path('download_chart/', views.download_chart, name='downloads_chart'),
    path('download_chart_view/', views.download_chart_view, name='download_chart_view'),
    path('combine_chart', views.combine_chart, name='combine_chart'),
    path('all_object/', views.all_object, name='all_object')
]   