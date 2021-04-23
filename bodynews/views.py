from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView, CreateView, 
                                    DetailView, View
                                    )

from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostDetailView(DetailView):

    model = Post
    template_name = 'bodynews/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_pk'

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=post.slug)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            obj = Comment()
            obj.body = comment_form.cleaned_data['body']
            obj.author = request.user
            obj.post = post
            obj.save()
            return redirect('post_list')
    else:
        comment_form = CommentForm()
    return render(request, 'bodynews/post_detail.html', locals())


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Post, pk=comment.post.pk)
    if request.method == "POST" and request.user == post.author:
        comment.delete()
        return redirect('post_list')
    return render(request, 'bodynews/delete_comment.html', locals())


class RulesView(View):

    def get(self, request):
        return render(request, 'rules.html', locals())


class PostListView(ListView):

    model = Post
    template_name = 'base.html'
    context_object_name = 'posts'


class PostCreateView(CreateView):

    model = Post
    template_name = 'bodynews/new_post.html'
    form_class = PostForm
    context_object_name = 'post'