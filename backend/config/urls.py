from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("", include("pages.urls")),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("api/", include("api.urls")),
    path("__reload__/", include("django_browser_reload.urls"))
]
