from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_playing/', views.add_playing, name='add_playing'),
    path('snacks/', views.SnackList.as_view(), name='snacks_index'),
    path('snacks/<int:pk>/', views.SnackDetail.as_view(), name='snacks_detail'),
    path('snacks/create/', views.SnackCreate.as_view(), name='snacks_create'),
    path('snacks/<int:pk>/update/', views.SnackUpdate.as_view(), name='snacks_update'),
    path('snacks/<int:pk>/delete/', views.SnackDelete.as_view(), name='snacks_delete'),
    path('finches/<int:finch_id>/add_playing/', views.add_playing, name='add_playing'),
    path('finches/<int:finch_id>/assoc_snack/<int:snack_id>/', views.assoc_snack, name='assoc_snack'),
]