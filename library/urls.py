from rest_framework_simplejwt import views as jwtviews
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('app.urls')),
    path('refreshtoken/', jwtviews.TokenRefreshView.as_view(), name='refreshmenttoken'),
    path('acesstoken/',jwtviews.TokenObtainPairView.as_view(),name='acesstoken')
]
