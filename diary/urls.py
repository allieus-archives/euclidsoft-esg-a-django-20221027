from django.urls import path
from diary import views

urlpatterns = [
    path("", views.memory_list),
    path("<int:pk>/", views.memory_detail),
    path("new/", views.memory_new),
]
