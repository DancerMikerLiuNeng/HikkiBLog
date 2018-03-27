from django.shortcuts import render,render_to_response,RequestContext
# Create your views here.
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from blog.models import Post
from .search import *
import datetime


def tagpage(request,tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html",{"posts":posts,"tag":tag})

def index(request):
    #pagination
    limit = 3
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts,limit)
    
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
        
    #archives display    
    posts_by_date = Post.objects.all().order_by("-created")
    now = datetime.datetime.now()
    
    post_dict = {}
    for i in range(posts_by_date[0].created.year,posts_by_date[len(posts_by_date)-1].created.year-1,-1):
        post_dict[i] = {}
        for month in range(1,13):
            post_dict[i][month] = []
    for post_by_date in posts_by_date:
        post_dict[post_by_date.created.year][post_by_date.created.month].append(post_by_date)
        
    post_sorted_keys = list(reversed(post_dict.keys()))
    list_posts = []
    for key in post_sorted_keys:
        adict = {key:post_dict[key]}
        list_posts.append(adict)
        
    
        
    return render_to_response('index.html',{'posts':posts,'now':now,'list_posts':list_posts})
    
def archives(request):
    #archives display    
    posts_by_date = Post.objects.all().order_by("-created")
    now = datetime.datetime.now()
    
    post_dict = {}
    for i in range(posts_by_date[0].created.year,posts_by_date[len(posts_by_date)-1].created.year-1,-1):
        post_dict[i] = {}
        for month in range(1,13):
            post_dict[i][month] = []
    for post_by_date in posts_by_date:
        post_dict[post_by_date.created.year][post_by_date.created.month].append(post_by_date)
        
    post_sorted_keys = list(reversed(post_dict.keys()))
    list_posts = []
    for key in post_sorted_keys:
        adict = {key:post_dict[key]}
        list_posts.append(adict)
    return render_to_response('archives.html',{'list_posts':list_posts})

def search(request):
    
    query_string = ''
    found_entries = None
   
       
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        print query_string
        entry_query = get_query(query_string, ['title', 'body',])
        
        found_entries = Post.objects.filter(entry_query).order_by('-created')
   
    return render_to_response('search_results.html',{ 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))
    