from . import views
from django.urls import path

urlpatterns = [
    path("", views.getAPIData, name="air_quality_api")
]
