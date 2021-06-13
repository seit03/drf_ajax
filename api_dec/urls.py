from django.urls import path

from api_dec import views

urlpatterns = [
    path('api/v1/list_jobs', views.get_jobs),
    path('', views.list_jobs, name='list_jobs'),
]


