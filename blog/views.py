from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils import timezone
from .models import Comment
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def blogpost(request):
    return render(request,'blog/post.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/post.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


def del_com(request, com_id):
    comment = get_object_or_404(Comment, pk=com_id)
    print(comment.author)
   # cur_user = request.user
   # user_info = get_object_or_404(User,)
   # if comment.author == request.user:
    comment.delete()
    product_id = comment.pp
    post = get_object_or_404(Post, pk=product_id)
    print(post)
    comm = Comment.objects.filter(pp=product_id).order_by('-date_posted')
    cur_user = request.user
    return render(request, 'blog/postdet.html', {'post': post, 'comments': comm, 'cur_user': cur_user})
    ### return redirect('blog-home')


def detail(request, post_id):
    if request.method == 'POST':
        print("HELLO")
        print(post_id)
        com = Comment()
        com.content = request.POST['comm']
        com.author = request.user
        com.pp = post_id
        com.date_posted = timezone.datetime.now()
        com.save()
        post = get_object_or_404(Post, pk=post_id)
        print(post)
        comm = Comment.objects.filter(pp=post_id).order_by('-date_posted')
        cur_user = request.user
        return render(request, 'blog/postdet.html', {'post': post, 'comments': comm, 'cur_user': cur_user})

    else:
        post = get_object_or_404(Post, pk=post_id)
        print(post)
        comm = Comment.objects.filter(pp=post_id).order_by('-date_posted')
        cur_user = request.user
        return render(request, 'blog/postdet.html', {'post': post, 'comments': comm, 'cur_user': cur_user})

    #if request.method == 'POST':
     #   post = get_object_or_404(Post, pk=post_id)
      #  return render(request, 'blog/post_detail.html', {'post': post})
    #else:
     #   post = Post.objects.filter(pk=post_id)
      #  return render(request, 'blog/post_detail.html', {'post': post})


class PostDetailView(DetailView):
    model = Post



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
   # template_name = 'blog/home.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def search(request):
    template = 'blog/post_list.html'
    query = request.GET.get('q', None)
    if query:
        results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return render(request, template, {'results': results})
    else:
        return render(request, template)


def send(request):
    print("Hello")
    send_mail('hello',
              'Hello there everyone',
              'iayush.srivastava1999@gmail.com',
              ['iayush.srivastava1999@gmail.com'],
              fail_silently=False)
    return render(request, 'blog/send.html')



@login_required
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Post, pk=product_id)
        product.votes_total += 1
        product.save()
        post = get_object_or_404(Post, pk=product_id)
        print(post)
        comm = Comment.objects.filter(pp=product_id).order_by('-date_posted')
        cur_user = request.user
        return render(request, 'blog/postdet.html', {'post': post, 'comments': comm, 'cur_user': cur_user})


