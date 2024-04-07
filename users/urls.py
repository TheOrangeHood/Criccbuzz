from django.urls import path
from .views import *

# BASE URL = api/admin/

urlpatterns = [
    path("signup", CreateAdminUserView.as_view(), name="signup"),
    path("login", LoginAdminUserView.as_view(), name="login"),
]