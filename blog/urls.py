from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', IndexBlog, name='blog_index'),
    url(r'^new$', NewPost, name='blog_form_new'),
    url(r'^post/(?P<id>[0-9]+)/$', EditPost, name='blog_form_edit'),
    url(r'^profil$', AuthorBlog, name='blog_profil'),
    url(r'^profil/new$', AuthorNew, name='blog_profil_new'),
]
