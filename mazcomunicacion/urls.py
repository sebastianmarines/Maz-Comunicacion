from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('web.urls', namespace="web")),
    path('', include('periodicos.urls', namespace="periodicos")),
    path('blog/', include('blog.urls', namespace='blog'))
]
