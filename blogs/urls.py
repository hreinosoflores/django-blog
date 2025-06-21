from django.urls import path
from . import views

# http://127.0.0.1:8000/category/100
urlpatterns = [
    path('<int:category_id>/', views.post_by_category, name='posts_by_category')
]
