from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


class NewsDetailView(DetailView):
    '''Перегляд публікації'''
    model = Artiles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    '''Редагування публікації'''
    model = Artiles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    '''Видалення публікації'''
    model = Artiles
    success_url = '/news/'
    template_name = 'news/news_delete.html'


def news_home(request):
    news = Artiles.objects.order_by('-date')  # Сортування но даті (спочату нові)
    return render(request, 'news/news_index.html', {'news': news})


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма не була заповнена'

    form = ArticlesForm()

    data = {
        'title': 'Форма для створення запису',
        'form': form,
    }
    return render(request, 'news/create.html', data)
