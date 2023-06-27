from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users import views

app_name = 'users'

urlpatterns = [
    path('create_user', views.create_user, name='create_user'),
    path('get_user/<int:pk>', views.get_user, name='get_user'),
    path('update_user/<int:pk>', views.update_user, name='update_user'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])

