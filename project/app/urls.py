
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create_view, name='createview'),
    path('list', views.list_view, name='listview'),
    path('<id>', views.detail_view, name='detailview'),
    path('<id>/update', views.update_view, name='updateview'),
    path('<id>/delete', views.delete_view, name='updateview'),
    
]