from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleFrom
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Article.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news' : news})

# Article.objects.order_by('title') - сортировка по алфавиту
# Article.objects.order_by('-title') - сортировка NO по алфавиту
# Article.objects.all() - все (вроде по дате)
# Article.objects.order_by('date')[:4] - последние 4 новости

class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details_view.html'
    context_object_name = 'article' # по-сути ключ словара (как в обычных запросах)

class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = ArticleFrom

class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/' # переадресация после удаления
    template_name = 'news/news_delete.html'

def create(request):
    error = ''
    if request.method == "POST":
        form = ArticleFrom(request.POST) # Получение данных ведённых пользователем
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была не верной'
    form = ArticleFrom()
    data = { 'form' : form, 'error' : error }
    return render(request, 'news/create.html', data)