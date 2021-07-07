from django.conf.urls import url
from rest_framework import urlpatterns
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/noticias/$',views.NoticiasViewSet.as_view()),
    url(r'^api/noticias_crear/$',views.NoticiasCreateViewSet.as_view()),
    url(r'^api/noticia/(?P<autor>.+)/$',views.NoticiaBuscarViewSet.as_view()),
    url(r'^api/categorias/$', views.CategoriaViewSet.as_view()),
]
urlpatterns= format_suffix_patterns(urlpatterns)