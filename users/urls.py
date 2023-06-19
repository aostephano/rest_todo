from django.urls import path

from users import views

urlpatterns = [
    path('', views.create_user),
    path('<int:user_id>', views.user_detail),
]
