# Accounts related urls

from django.urls import path, include
from accounts.views import index, logout, login, registration, user_profile
from accounts import url_reset

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('profile/', user_profile, name="profile"),
    path('password-reset/', include(url_reset)),
    path('register/', registration, name="registration"),
]
