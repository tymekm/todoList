from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('item.urls')),
    path('admin/', admin.site.urls),
    path('item/', include('item.urls'))
]
