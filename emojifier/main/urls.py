from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name = 'main'
urlpatterns = [
  path('', views.Index.as_view(), name='index')
]