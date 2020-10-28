from django.contrib import admin
from django.conf.urls import include, url
from document_uploader.views import UploadFile

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^files/?', UploadFile.as_view()),
]
