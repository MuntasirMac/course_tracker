from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('kurstrack/', include('kurstrack.urls')),
    path('admin/', admin.site.urls),
]