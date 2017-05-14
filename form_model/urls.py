from django.conf.urls import url
from .views import coba

urlpatterns = [
    url(r'^$', coba, name='form_index')
]
