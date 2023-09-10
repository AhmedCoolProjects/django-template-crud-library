from django.urls import path
from . import views
 
urlpatterns = [
    path('infos', views.ApiOverview, name='category'),
    path('add/', views.create_category, name='create-category'),
    path('id/<int:pk>', views.category_by_id, name='category-by-id'),
    path('', views.all_categories, name='all-categories'),
    path('update/<int:pk>', views.update_category, name='update-category'),
    path('delete/<int:pk>', views.delete_category, name='delete-category'),
    path('list/', views.create_category_from_list, name='create-category-from-list'),
]