from django.urls import path
from .views import SignPage, LoginPage, LogoutPage, Captcha


urlpatterns = [
    path('login', LoginPage, name='login'),
    path('sign', SignPage, name='sign'),
    path('logout', LogoutPage, name='logout'),
    path('captcha', Captcha, name='captcha'),
    # path('resetpassword/', PasswordResetPage, name="password-reset"),
    # path('resetpassword/<slug:code>/', ResetPasswordConfirmPage, name="password-reset-confirm"),
]