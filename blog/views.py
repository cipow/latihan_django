from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Author
from .forms import PostForm, AuthorForm

def IndexBlog(request):
    post = Post.objects.all()
    return render(request, 'blog/konten.html', {'posts':post})

def NewPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_index')
    else:
        form = PostForm()
    return render(request, 'blog/form.html', {'form':form})

def EditPost(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_index')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/form.html', {'form':form})

def AuthorBlog(request):
    profil = Author.objects.all()
    return render(request, 'blog/profil.html', {'profils':profil})

def AuthorNew(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_profil')
        else:
            return redirect('blog_profil_new')

    else:
        form = AuthorForm()
        return render(request, 'blog/profilnew.html',{'form':form})
