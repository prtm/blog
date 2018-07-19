# core django
from django.urls import path, reverse_lazy, re_path
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

    path('reset-password/',
         PasswordResetView.as_view(template_name='accounts/reset_password_form.html',
        email_template_name='accounts/reset_password_email.html',
        subject_template_name='accounts/reset_password_subject.txt',
                                   success_url=reverse_lazy('accounts:reset_password_done')),
         name='reset_password'),

    path('reset-password/done/',
         PasswordResetDoneView.as_view(
             template_name='accounts/reset_password_done.html'),
         name='reset_password_done'),

    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         PasswordResetConfirmView.as_view(
             template_name='accounts/reset_password_confirm.html',
             success_url=reverse_lazy('accounts:reset_password_complete')),
         name='reset_password_confirm'),

    path('reset/done/',
         PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'),
         name='reset_password_complete'),
]
