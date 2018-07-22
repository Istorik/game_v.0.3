from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_list, name="list_news"),
    path('single/<int:pk>', views.new_single, name="new_single"),
    path('miner_add', views.miner_add, name="miner_add"),
    path('miner/<int:pk>', views.miner, name="miner"),

]
