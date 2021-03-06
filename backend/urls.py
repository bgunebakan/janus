from django.conf.urls import url, include
from django.contrib.auth.views import login, logout_then_login
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings

from .views import app, index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('users.urls')),
    url(r'^api/', include('identifiers.urls')),
    url(r'^api/', include('doors.urls')),
    url(r'^api/', include('permissions.urls')),
    url(r'^api/', include('controllers.urls')),
    url(r'^app/', app, name='app'),
    url('^auth/login/$', login, name='login'),
    url('^auth/logout/$', logout_then_login, name='logout'),
    url('^$', index, name='index'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
