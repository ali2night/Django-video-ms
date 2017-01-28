from django.conf.urls import url
from . import views

app_name = 'movies'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^login/$',views.login_user,name='login_user'),
    url(r'^logout/$',views.logout_user,name='logout_user'),
    url(r'^movies_list/$', views.movies_list, name='movies_list'),
    url(r'^search/$',views.search_video_form,name='search_video'),
    url(r'^dosearch/$',views.do_search_video_form,name='do_search_video'),
    url(r'^movies_list/random_movie/$',views.random_movie,name="random_movie"),
    url(r'^movies_list/comments/$',views.comment_view,name='comment_view'),
    url(r'^movies_list/movies_selected/(?P<movie_id>\d)/$', views.movies_selected, name='movies_selected'),
    url(r'^movies_list/movies_selected/comment/(?P<movie_id>\d)/', views.comment, name='selected_movie_comment'),

]
