from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from VR.views import hello_view
from django.conf.urls import url

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^file/', include('VR.urls')),
  url(r'^hello/', hello_view),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)