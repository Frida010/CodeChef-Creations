from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post, Category, SavedPost
from .forms import CommentForm


@login_required
def toggle_saved(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user

    # Kolla om användaren redan har sparad posten
    saved_post, created = SavedPost.objects.get_or_create(user=user, post=post)

    if not created:
        # Om posten redan är sparad, ta bort den
        saved_post.delete()

    return redirect('post_detail', pk=post_id)


class CategoryListView(ListView):
    model = Post
    template_name = 'category_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Post.objects.filter(categories__name=category_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs['category_name']
        context['categories'] = Category.objects.all()
        context['selected_category'] = category_name
        return context


class CategoryDetailView(ListView):
    model = Post
    template_name = 'category_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = get_object_or_404(Category, name=category_name)
        return Post.objects.filter(categories=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs['category_name']
        context['selected_category'] = category_name
        return context


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    template_name = "post_detail.html"

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True

        return render(
            request,
            self.template_name,
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            self.template_name,
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
