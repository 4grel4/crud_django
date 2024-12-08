from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_list.html'

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')

class ProdutoUpdateView (UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = reverse_lazy('produto_list')