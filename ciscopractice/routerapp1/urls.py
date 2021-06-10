from django.urls import path, include
from .views import RouterDetail, AddData, info

urlpatterns = [

    path('fetch_router/', RouterDetail.as_view()),

    path('', AddData.as_view()),
    path('ping', AddData.as_view()),

    path('info/', info),


]
