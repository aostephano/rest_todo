from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users import views

app_name = 'users'

urlpatterns = [
    # Class Based Views
    path('register', views.UserCreate.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),

    path('my_protected_view', views.MyProtectView.as_view(), name='my_protected_view'),

    # Func Based Views
    # path('get_user/<int:pk>', views.get_user, name='get_user'),
    # path('update_user/<int:pk>', views.update_user, name='update_user'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
