from django.shortcuts import render, get_object_or_404, redirect, Http404
from .models import Post
from .forms import PostForm, CommentForm
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



def posts(request):

    posts_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        posts_list = posts_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name=query) |
            Q(user__last_login=query)
        ).distinct()

    paginator = Paginator(posts_list, 3)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "post/post.html", { "posts": posts, })



def posts_detail(request, slug):

    posts = get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = posts
        comment.save()

    return render(request, "post/detail.html", { "post": posts, "form": form, })



def posts_create(request):

    if not request.user.is_authenticated:
        return Http404()

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        Post = form.save(commit=False)
        Post.slug = slugify(Post.title.replace("ı", "i"))
        Post.user = request.user
        Post.save()
        return redirect("post:posts")

    return render(request, "post/form.html", {"form": form, "title": "Paylaş"})



def posts_update(request, slug):

    if not request.user.is_authenticated:
        return Http404()

    posts = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=posts)

    if form.is_valid():
        form.save()
        return redirect("post:posts")

    return render(request, "post/form.html", {"form": form, "title": "Güncelle"})



def posts_delete(request, slug):

    if not request.user.is_authenticated:
        return Http404()

    posts = get_object_or_404(Post, slug=slug)
    posts.delete()

    return redirect("post:posts")