from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('fasto.urls', namespace='fasto')),
]

admin.site.site_header  =  "Fasto Dashboard"  
admin.site.site_title  =  "Dashboard"
admin.site.index_title  =  "Dashboard"