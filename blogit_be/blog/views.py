from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Post,Category,Comment
from .form import PostForm,EditForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
# from user.models import 

# Create your views here.

def index(request):
    return render(request, 'index.html')


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
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
    def get_queryset(self):
        return Post.objects.filter(is_published=True) 

class DraftView(ListView):
    model = Post
    template_name = 'draft.html'  # Thay 'drafts.html' bằng template bạn muốn sử dụng cho trang drafts

    def get_queryset(self):
        return Post.objects.filter(is_published=False, author=self.request.user) 


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})


def CategoryView(request,cats):
    category_post =Post.objects.filter(category = cats.replace('-',' '))
    return render(request,'categories.html',{'cats':cats.title().replace('-',' '),'category_post':category_post})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)

        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False 
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True 

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

    success_url = reverse_lazy('index')
    # fields = '__all__'
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')

