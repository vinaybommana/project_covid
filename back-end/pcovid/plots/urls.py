from django.urls import path

from .views import DetailDataObject, ListDataObject

urlpatterns = [
    path("<int:pk>/", DetailDataObject.as_view()),
    path("", ListDataObject.as_view()),
]
