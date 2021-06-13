from django.urls import path

from phone_numbers import views

urlpatterns = [
    path('api/v1/phone/', views.PhoneAPIView.as_view()),
]


