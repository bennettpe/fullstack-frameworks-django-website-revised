# Reset Password

from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', PasswordResetView,
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    path('done/', PasswordResetDoneView, name='password_reset_done'),
    path('<uidb64>[0-9A-Za-z]+-<token>.+)/', PasswordResetConfirmView,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    path('complete/', PasswordResetCompleteView, name='password_reset_complete')
]
