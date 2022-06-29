from django.urls import path
from rest_framework import routers
from library import views

urlpatterns = []

urlpatterns += [
    path('category-list/', views.BookCategoryListView.as_view()),
    path('category-create/', views.BookCategoryCreateView.as_view()),
    path('category-list-create/', views.BookCategoryListCreateView.as_view()),
    path('category-retrive/<int:pk>', views.BookCategoryRetriveView.as_view()),
    path('category-update/<int:pk>', views.BookCategoryUpdateView.as_view()),
    path('category-retrive-update/<int:pk>', views.BookCategoryRetriveUpdateView.as_view()),
    path('category-delete/<int:pk>', views.BookCategoryDestroyView.as_view()),
    path('category-update-delete/<int:pk>', views.BookCategoryRetriveUpdateDestroyView.as_view()),
]
