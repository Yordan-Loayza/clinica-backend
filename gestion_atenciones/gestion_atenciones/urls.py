from django.contrib import admin
from django.urls import path
from agendas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('list/', views.agenda_list, name='list'),
    path('form/', views.agenda_form, name='form'),
    path('confirm-delete/', views.confirm_delete, name='confirm'),
    path('create/', views.agenda_create, name='create'),
]
