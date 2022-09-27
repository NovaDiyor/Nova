from django.urls import path
from .views import *

urlpatterns = [
    path('post-table/', post_table),
    path('get-menu/', get_menu),
    path('get-bill/<int:pk>/', get_bill),
    path('get-table/<int:pk>/', get_table)
]
