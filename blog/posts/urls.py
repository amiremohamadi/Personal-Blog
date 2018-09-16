from django.urls import re_path
from .views import (Index, PostView)
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', Index.as_view()),
    re_path(r'^about-me$', TemplateView.as_view(template_name='about-me.html')),
    re_path(r'^post/(?P<post_id>\d+)$', PostView.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)