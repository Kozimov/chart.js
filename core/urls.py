
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('example/', example , name="example"),
    path('pieChart/', pieChart , name="pieChart"),
    path('sortedChart/', sortedChart , name="sortedChart"),
    path('boxPlotChart/', boxPlotChart , name="boxPlotChart"),
]
