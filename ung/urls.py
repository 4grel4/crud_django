"""
URL configuration for ung project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from product.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, ProdutoDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path('', ProdutoListView.as_view(), name='produto_list'),
    path('produto/add/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produto/<int:pk>/update/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('produto/<int:pk>/delete/', ProdutoDeleteView.as_view(), name='produto_delete'),
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),

]