from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import BlogPost
from .forms import CommentForm
from django.contrib import messages

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

#replace with proper "blog_list.html"

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()  # Get all comments for the post

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Save the comment but do not commit to database yet
            comment = form.save(commit=False)
            comment.blog_post = post  # Associate comment with the current blog post
            comment.save()
            messages.success(request, 'Your comment has been submitted successfully.')
            return redirect('blog_detail', post_id=post.id)
    else:
        messages.error(request, "You haven't Commented yet")
        form = CommentForm()

    return render(request, 'blog/blog_detail.html', {'post': post, 'comments': comments, 'form': form})

