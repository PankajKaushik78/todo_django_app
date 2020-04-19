from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_view, name="create"),
    path('', views.list_view, name="list"),
    path('<int:id>', views.update_view, name="update"),
    path('<int:id>/delete', views.delete_view, name="delete")
]
