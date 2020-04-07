from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<task_id>', views.delete, name='delete'),
    path('done/<task_id>', views.mark_done, name='done'),
    path('edit/<task_id>', views.edit, name='edit'),
]