from django.urls import path, include
from accounts.views import SignupPageView

urlpatterns = [path("signup/", SignupPageView.as_view(), name="signup")]