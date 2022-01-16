import debug_toolbar
from django.contrib import admin
from django.urls import include, path

from mysite import settings

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
