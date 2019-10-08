from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index , name="index"),
    path('list/', views.viewlist , name="view_list"),
    path('detail/<int:question_id>', views.detailView , name="detail"),
]
