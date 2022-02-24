
from django.urls import path
from .views import TaskDetail, TaskList

app_name = 'tasks'

urlpatterns = [
    path('<int:pk>/', TaskDetail.as_view(), name='detailcreate'),
    path('', TaskList.as_view(), name='listcreate'),
]