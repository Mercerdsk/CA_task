from django.urls import path
from gridview.views import gridview

urlpatterns = [
    path('', gridview, name='gridview'),
]
