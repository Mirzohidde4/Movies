from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts, Comments
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator

# Create your views here.
def PostView(request):
    object_list = Posts.objects.all()
    kinolar = []
    for kino in object_list:
        kinolar.insert(0, kino)    
    paginator = Paginator(kinolar, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/posts.html', {'page_obj': page_obj})


# class PostView(ListView):
#     model = Posts
#     queryset = Posts.objects.all()
#     context_object_name = 'paginator'
#     paginate_by = 2
#     template_name = 'posts/posts.html'


# class PostDetail(DetailView):
#     model = Posts
#     template_name = 'posts/post_detail.html'


def PostDetail(request, id):
    post = get_object_or_404(Posts, id=id)
    komentariya = Comments.objects.filter(post=post)

    if request.method == "POST":
        username = request.user
        if User.objects.filter(username=username).exists():
            comment = request.POST.get('comment')
            if comment and len(comment.strip()) != 0:
                Comments.objects.create(post=post, user=username, comment=comment)
            return redirect('post_detail', id=id)
        return redirect("login")
    return render(request, 'posts/post_detail.html', {'post': post, 'komentariya': komentariya})


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ('title', 'description', 'body', 'photo')
    template_name = 'posts/post_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def test_func(self):
        return self.request.user.is_superuser
    

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
    def test_func(self):
        return self.request.user.is_superuser


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Posts
    template_name = 'posts/post_new.html'
    fields = ('title', 'description', 'body', 'photo')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
    def test_func(self):
        return self.request.user.is_superuser


# def PostCreate(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         category = request.POST.get('category')
#         description = request.POST.get('description')
#         body = request.POST.get('body')
#         photo = request.POST.get('photo')
#         Posts.objects.create(title=title, category=category, description=description, body=body, photo=photo, author=request.user)
#         return redirect('posts')
#     return render(request, 'posts/post_new.html')


def CategoryPost(request, slug):
    posts = Posts.objects.filter(category__slug=slug)
    kinolar = []
    for kino in posts:
        kinolar.insert(0, kino)
    paginator = Paginator(kinolar, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/category_post.html', {'page_obj': page_obj})


def SearchPage(request):
    name = request.GET.get('poisk')
    if name:
        filter = Posts.objects.filter(title__icontains=name)
        kinolar = []
        for kino in filter:
            kinolar.insert(0, kino)
        paginator = Paginator(kinolar, 2)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'posts/search.html', {'page_obj': page_obj})
    else:
        return redirect('posts')

