from csk.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('jadeja/',jadeja,name='jadeja'),
    path('raina/',raina,name='raina'),
]