from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users import views

urlpatterns = [
    path('', views.create_user),
    path('<int:user_id>', views.user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])

