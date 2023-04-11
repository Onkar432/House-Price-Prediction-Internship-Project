from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.Base),
    path('predict', views.predict),
    path('predict/result/', views.result),
]