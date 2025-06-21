from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from dashboards.forms import CategoryForm, PostForm
from django.template.defaultfilters import slugify

# Create your views here.


def categories(request):
    return render(request, 'dashboard/categories.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_category.html', context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category
    }
    return render(request, 'dashboard/edit_category.html', context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')


def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'dashboard/posts.html', context)


def add_post(request):
    if request.method == 'POST':
        # estamos esperando imagenes
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # va tener los datos en memoria mas no en la base de datos aun
            post = form.save(commit=False)
            # obtenemos el autor
            post.author = request.user
            # guardamos ahora si los cambios en la base de datos
            post.save()
            # seteamos el slug + id
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            # volvemos a guardar
            post.save()
            return redirect('posts')

    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_post.html', context)


def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        # estamos esperando imagenes
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            # actualizar slug al actualizar title
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')

    form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html', context)


def delete_post(request, pk):
    category = get_object_or_404(Blog, pk=pk)
    category.delete()
    return redirect('posts')
