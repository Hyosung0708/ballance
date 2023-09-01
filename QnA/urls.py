from django.urls import path
from . import views


app_name = 'QnA'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:q_id>/', views.question, name='question'),
]