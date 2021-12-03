from django.urls import path
from .views import UserDetail
app_name = 'users'

urlpatterns = [
path('<int:pk>/', UserDetail.as_view()),
]