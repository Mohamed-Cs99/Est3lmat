from django.urls import path, include
from . import views


urlpatterns = [
    path('person', views.PersonView.as_view()),
    path('person/<int:pk>', views.SinglePersonView.as_view()),
    path('approval', views.ApprovalView.as_view()),
    path('approval/<int:pk>', views.SingleApprovalView.as_view()),
]
