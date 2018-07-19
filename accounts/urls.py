# core django
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordChangeView, PasswordChangeDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# project
from .views import register


urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='accounts/login.html',
        redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('accounts:login')), name='logout'),
    path('register/', register, name='register'),

    path('change-password/',
         PasswordChangeView.as_view(template_name='accounts/change_password_form.html',
                                    success_url=reverse_lazy('accounts:change_password_done')),
         name='change_password'),

    path('change-password/done/',
         PasswordChangeDoneView.as_view(
             template_name='accounts/change_password_done.html'),
         name='change_password_done'),
]
