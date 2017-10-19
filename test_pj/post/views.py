from django.http import HttpResponse
from django.shortcuts import render, redirect

from post.forms import PostCreateForm
from post.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post = Post.objects.create(title=title, content=content)
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'post/post_create.html', context)


def post_delete(request, pk):
    if request.method == 'POST':
        Post.objects.get(pk=pk).delete()
        url = request.META['HTTP_REFERER']
        return redirect('main')
    return HttpResponse('Permission denied', status=403)
