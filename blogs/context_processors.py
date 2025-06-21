from .models import Category


def get_categories(request):
    categorias = Category.objects.all()
    return dict(categorias=categorias)
