from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Backend API",
        default_version='v1',
        description="Backend For HABIB ILM MARKAZI",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="habibilmmarkazi@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/', include('apps.metsenat.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
