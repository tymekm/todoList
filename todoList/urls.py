from django.urls import path, include

urlpatterns = [
    path('', include('item.urls')),
    path('item/', include('item.urls')),
    path('users/', include('users.urls'))
]
