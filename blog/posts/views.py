from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import (Post, Image)

class Index(View):
    # TODO: template_name = 404 # add it when to want get 404 if someone post to this page
    template_name = 'index.html'

    def get(self, request):
        all_posts = Post.objects.all().order_by('id').reverse()
        page = request.GET.get('page', 1)
        paginator = Paginator(all_posts, 6)

        try:
            this_page_posts = paginator.page(page)
        except PageNotAnInteger:
            this_page_posts = paginator.page(1)
        except EmptyPage:
            this_page_posts = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'posts': this_page_posts})

class PostView(View):
    template_name = 'post.html'
    
    def get(self, request, post_id=None):
        post = Post.objects.all().get(pk=post_id)
        return render(request, self.template_name, {'post': post})