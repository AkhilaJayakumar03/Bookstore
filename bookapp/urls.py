from django.urls import path
from .views import *

urlpatterns=[
    path('register/',register.as_view(),name='register'),
    path('login/',login.as_view(),name='login'),
    path('index/',index,name='index'),
    path('userprofile/',userprofile),
    path('home/', home.as_view(), name='home'),
    path('bookupload/',bookupload.as_view(),name='bookupload'),
    path('bookdelete/<pk>',bookdelete.as_view(), name='bookdelete'),
    path('bookupdate/<pk>',bookupdate.as_view(), name='bookupdate'),
    path('bookdownload/',bookdownload.as_view(), name='bookdownload'),
    path('logout/',lgview.as_view(),name='lgview'),

]
