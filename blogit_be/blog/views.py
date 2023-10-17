from typing import Any
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Post,Category,Comment,Profile
from .form import PostForm,EditForm,CommentForm,AdminEditForm,ProfileForm
from django.urls import reverse_lazy,reverse
from django.db.models import F
from django.http import HttpResponseRedirect
# from user.models import 

# Create your views here.

def index(request):
    return render(request, 'index.html')

def search_posts(request):
    query = request.GET.get('search')
    results = Post.objects.filter(title__icontains=query)  # Tìm kiếm bài viết theo tiêu đề
    return render(request, 'search_results.html', {'results': results, 'query': query})

def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked =  True
    else:
        post.likes.add(request.user)
        liked =  False        

    return HttpResponseRedirect(reverse('article_details',args= [str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-post_date']
    # ordering = ['-id']
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        
        # Lấy 5 bài viết mới nhất
        latest_posts = Post.objects.filter(is_published=True).order_by('-post_date')[:5]
        print(cat_menu)
        # Lấy 5 bài viết có số lượt comment và like nhiều nhất
        # popular_posts = Post.objects.filter(is_published=True).annotate(total_interactions=F('likes') + F('comments__count')).order_by('-total_interactions')[:5]
        # F để tham chiếu đến các trường của mô hình trong câu truy vấn
        
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        context["latest_posts"] = latest_posts
        # context["popular_posts"] = popular_posts
        return context
    def get_queryset(self):
        return Post.objects.filter(is_published=True) 

class DraftView(ListView):
    model = Post
    template_name = 'draft.html'  # Thay 'drafts.html' bằng template bạn muốn sử dụng cho trang drafts

    def get_queryset(self):
        return Post.objects.filter(is_published=False, author=self.request.user) 

class AdminView(ListView):
    model = Post
    template_name = 'admin.html'  # Thay 'drafts.html' bằng template bạn muốn sử dụng cho trang drafts

    def get_queryset(self):
        return Post.objects.filter(is_published=False) 
    
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        
        # Lấy 5 bài viết mới nhất
        latest_posts = Post.objects.filter(is_published=True).order_by('-post_date')[:5]
        
        context = super(AdminView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        context["latest_posts"] = latest_posts
        # context["popular_posts"] = popular_posts
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})


def CategoryView(request,cats):
    cat_menu_list = Category.objects.all()
    category_post =Post.objects.filter(category = cats.replace('-',' '))
    latest_posts = Post.objects.filter(is_published=True).order_by('-post_date')[:5]
    print(category_post)
    return render(request,'categories.html',{'cats':cats.title().replace('-',' '),'category_post':category_post,'cat_menu':cat_menu_list,'latest_posts':latest_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)

        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        latest_posts = Post.objects.filter(is_published=True).order_by('-post_date')[:5]

        liked = False 
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True 

        context["latest_posts"] = latest_posts
        context['total_likes'] = total_likes
        context["cat_menu"] = cat_menu
        context["liked"] = liked
        
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title','body')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    # fields = '__all__'
    # success_url = reverse_lazy('index')
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.parent_id = self.kwargs.get('parent_id')
        return super().form_valid(form)
    
    def get_success_url(self):
        # Sử dụng reverse_lazy để tạo URL cho trang article_details với 'pk' là self.kwargs['pk']
        return reverse_lazy('article_details', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['post_id'] = self.kwargs['pk']
            context['parent_id'] = self.kwargs.get('parent_id')
            return context      

class AddReplyView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.parent_id = self.kwargs['parent_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article_details', kwargs={'pk': self.kwargs['pk']})


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title','body']

class AdminUpdatePostView(UpdateView):
    model = Post
    form_class = AdminEditForm
    template_name = 'update_post.html'
    # fields = ['title','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')

class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('article_details', kwargs={'pk': self.kwargs['post_pk']})
    

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_update.html'

    def get_object(self, queryset=None):
        return self.request.user.profile
