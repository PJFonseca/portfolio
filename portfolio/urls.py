
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name="home"),
    path('disciplines/', views.disciplines_view, name="disciplines"),
    path('changelog/', views.changelog_view, name="changelog"),
    path('disciplines/create/', views.discipline_create, name='discipline_create'),
    path('disciplines/<int:id>/edit/', views.discipline_edit, name='discipline_edit'),
    path('disciplines/<int:id>/delete/', views.discipline_delete, name='discipline_delete'),
]