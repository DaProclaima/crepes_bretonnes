from django.urls import path, re_path
from . import views

urlpatterns = [
    path('accueil', views.home),
    # re_path(r'^article/(?P<id_article>.+)', views.view_article),
    path('article/<int:id_article>$', views.view_article, name='afficher_article'),
    # re_path(r'^articles/(?P<tag>.+)', views.list_articles_by_tag),
    re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.list_articles),

    path('redirection', views.view_redirection),
]
# urlpatterns = [
#     path('accueil', views.home),
#     path('article/<id_article>', views.view_article),
#     path('articles/<str:tag>', views.list_articles_by_tag),
#     path('articles/<int:year>/<int:month>', views.list_articles),
# ]
