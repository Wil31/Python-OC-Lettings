from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("oc_lettings_home.urls", namespace="home")),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
]
