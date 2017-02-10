from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from .models import video,comment_for_movie
from django.shortcuts import render,get_object_or_404
from .forms import video_form,comment_form
import random
random.seed(100)
# Create your views here.
def index(request):
    latest_movies_list = video.objects.order_by('upload_time')[:5]
    context = {'latest_movies_list': latest_movies_list}
    return render(request,'movies/index.html',context)
def movies_list(request):
    latest_movies_list = video.objects.order_by('upload_time')[:5]
    context = {'latest_movies_list': latest_movies_list}
    return render(request,'movies/movies_list.html',context)
def movies_selected(request,movie_id):
   # request.session.set_expiry(10)
    if request.user.is_authenticated():
        movie_selected =video.objects.get(pk=movie_id)
        Comment_Form=comment_form(request.POST)
        context = {'movie_selected':movie_selected,'comment_form':Comment_Form}
        return render(request,'movies/movies_selected.html',context)
    else:
        return HttpResponseRedirect(reverse('movies:login_user'))
def comment(request,movie_id):
    name=request.POST.get('user_name')
    subject=request.POST.get('user_subject')
    comment_user=request.POST.get('user_comment')
    email=request.POST.get('user_mail')
    movie_name=request.POST.get('movie_name')
    ##############################################################
    comment_movie=comment_for_movie()
    comment_movie.user_name=name
    comment_movie.user_subject=subject
    comment_movie.movie_name=movie_name
    comment_movie.user_comment=comment_user
    comment_movie.user_mail=email
    comment_movie.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def login_user(request):
    return HttpResponseRedirect('/admin')
def logout_user(request):
    logout(request)
    request.session.flush()
    return HttpResponseRedirect(reverse('movies:index'))
def random_movie(request):
    '''
    movie_selected =video.objects.get('?')
    Comment_Form=comment_form(request.POST)
    context = {'movie_selected':movie_selected,'comment_form':Comment_Form}
    return render(request,'movies/movies_selected.html',context)
    '''
    import random
    mlen=video.objects.count()
    random = random.randint(1,mlen)
    url="/movies/movies_list/movies_selected/"+str(random)+"/"
    return HttpResponseRedirect(url)
def comment_view(request):
    name_of_movie=request.POST.get('movie_name')
    comments=comment_for_movie.objects.filter(movie_name=name_of_movie)
    context={'comments':comments,'video_name':name_of_movie}
    return render(request,'movies/view_comment.html',context)
def search_video_form(request):
    return render(request,'movies/search.html')
def do_search_video_form(request):
    name_video = request.POST.get('video_name')
    type_video = request.POST.get('video_type')
    year_video = request.POST.get('video_year')

    if name_video == "" and type_video == "":
        movie = video.objects.filter(video_year=year_video)
        return render(request,'movies/search_view.html',{'movie':movie})
    elif name_video == "" and year_video == "":
        movie = video.objects.filter(video_type=type_video)
        return render(request,'movies/search_view.html',{'movie':movie})
    elif type_video == "" and year_video == "":
        movie = video.objects.filter(video_name=name_video)
        return render(request,'movies/search_view.html',{'movie':movie})
    elif name_video == "":
        movie = video.objects.filter(video_type=type_video,video_year=year_video)
        return render(request,'movies/search_view.html',{'movie':movie})
    elif type_video == "":
        movie = video.objects.filter(video_name=name_video,video_year=year_video)
        return render(request,'movies/search_view.html',{'movie':movie})
    elif year_video == "":
        movie = video.objects.filter(video_name=name_video,video_type=type_video)
        return render(request,'movies/search_view.html',{'movie':movie})

    movie = video.objects.filter(video_name=name_video,video_type=type_video,video_year=year_video)
    return render(request,'movies/search_view.html',{'movie':movie})
