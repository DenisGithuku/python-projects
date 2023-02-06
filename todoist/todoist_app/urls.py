from django.urls import include, path
from .views import home_view, add_view, edit_view, delete_view, sort_view

urlpatterns = [
    path('', home_view, name = 'home'),
    path('edit', edit_view, name = 'edit'),
    path('add', add_view, name = 'add'),
    path('delete/<int:id>', delete_view, name = 'delete'),
    path('edit/<int:id>', edit_view, name = 'edit'),
    path('sort/<int:id>', sort_view, name = 'sort')
]