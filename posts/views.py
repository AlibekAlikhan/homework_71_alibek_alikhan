from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, FormView, TemplateView, DetailView

from accounts.models import Account
from posts.forms import SearchForm, PostForm, CommentForm
from posts.models import Post, Comment


class PostsView(ListView):
    template_name = "posts.html"
    model = Post
    context_object_name = "posts_view"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        context['favorit_form'] = CommentForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(username__icontains=self.search_value) | Q(first_name__icontains=self.search_value) | Q(
                email__icontains=self.search_value)
            queryset = Account.objects.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class PostsCreateView(LoginRequiredMixin, CreateView):
    template_name = "post_create.html"
    model = Post
    form_class = PostForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            description = form.cleaned_data.get('description')
            image = form.cleaned_data.get('image')
            user = request.user
            print(image)
            Post.objects.create(description=description, image=image, author=user)
        return redirect('index')


class PostsProfileView(ListView):
    template_name = "partial/article_list.html"
    model = Post
    context_object_name = "articles"


class CommentView(LoginRequiredMixin, CreateView):
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            user = request.user
            Comment.objects.create(author=user, text=text, post=post)
            user.commented_posts.add(post)
        return redirect('index')







class LikeView(TemplateView):

    def get(self, request, *args, **kwargs):
        user = request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        if post not in user.liked_posts.all():
            user.liked_posts.add(post)
            post.plus()
        else:
            user.liked_posts.remove(post)
            post.minus()
        return redirect('index')


class SubscriptionsView(TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        post = Account.objects.get(pk=self.kwargs['pk'])
        if post not in user.subscriptions.all():
            user.subscriptions.add(post)
        else:
            user.subscriptions.remove(post)
        return redirect('index')
