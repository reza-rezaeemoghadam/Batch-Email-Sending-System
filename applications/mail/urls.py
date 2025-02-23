from django.urls import path
from .views import EmailAPIView

urlpatterns = [
    path('send-emails/', EmailAPIView.as_view(), name='send_email'),
]