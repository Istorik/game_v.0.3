from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_list, name="list_news"),
    path('single/<int:pk>', views.new_single, name="new_single"),
    path('miner/<int:pk>/<int:qr_id>', views.miner, name="miner"),
]
