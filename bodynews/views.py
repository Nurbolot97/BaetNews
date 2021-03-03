from django.shortcuts import render, get_object_or_404, redirect
from . models import Post, PublishedManager, Comment
from .forms import PostForm, CommentForm


def post_list(request):
    posts = Post.published.all()
    return render(request, 'bodynews/posts_list.html', locals())

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
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

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'bodynews/new_post.html', locals())

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Post, pk=comment.post.pk)
    if request.method == "POST" and request.user == post.author:
        comment.delete()
        return redirect('post_list')
    return render(request, 'bodynews/delete_comment.html', locals())