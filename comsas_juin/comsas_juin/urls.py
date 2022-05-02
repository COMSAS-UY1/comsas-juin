from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('rosetta/', include('rosetta.urls'))
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
