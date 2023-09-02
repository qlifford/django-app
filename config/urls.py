from django.contrib import admin
from django.urls import path, include
from Users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name="Users/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="Users/logout.html"), name="logout"),
]