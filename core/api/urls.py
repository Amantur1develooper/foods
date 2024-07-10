from django.urls import path
from .views import FoodsListCreateView, FoodsRetrieveUpdateDestroyView, clear_count_foods

urlpatterns = [
    path('foods/', FoodsListCreateView.as_view(), name='foods-list-create'),
    path('foods/<int:pk>/', FoodsRetrieveUpdateDestroyView.as_view(), name='foods-retrieve-update-destroy'),
    path('foods/clear_zero_count/', clear_count_foods, name='clear-zero-count-foods'),
]
