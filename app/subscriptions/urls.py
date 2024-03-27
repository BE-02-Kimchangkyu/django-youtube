from django.urls import path
from . import views

# Django -> Main API
# FAST API -> Sub API (Micro Service)

urlpatterns = [
    path('', views.SubscriptionList.as_view(), name='sub-list'),
    path('<int:pk>/', views.SubscriptionDetail.as_view(), name='sub-detail'),
]