from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UpdateFormView, email_verification, UserPasswordResetView, UserListView, \
    UserDetailView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path("", LoginView.as_view(template_name='users/login.html'), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("user_form/", UpdateFormView.as_view(), name="user_form"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path('recovery_form/', UserPasswordResetView.as_view(), name='recovery_form'),
    path("mailing_list/users", UserListView.as_view(), name="user_list"),
    path("user_detail/users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("user_update/users/<int:pk>/", UserUpdateView.as_view(), name="user_update"),

    ]
