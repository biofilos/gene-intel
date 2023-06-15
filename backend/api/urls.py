from django.urls import path
from django.urls.conf import include
from .views import current_user
from .views import Greeting, Ensembl
urlpatterns = [
    path("greeting/", Greeting.as_view(), name="greeting"),
    path("current_user/", current_user, name="current_user"),
    path("ensembl/<ensid>", Ensembl.as_view(), name="ensembl")
    ]