from turtle import home
from django.views.generic import ListView , DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from home.models import Home,Publisher


# Create your views here.
class HomeListView(ListView):
    model = Home
    template_name = 'homepage.html'
    # context_object_name = 'home_list'

    def get_context_data(self, **kwargs):
        q = Home.objects.all()

        url_dict = self.request.GET
        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(name__icontains=text) | Q(category__name__icontains=text) | Q(description__icontains=text))
        
        if 'from-price' in url_dict and url_dict['from-price']:
            from_price = int(url_dict['from-price'])
            q = q.filter(price__gte=from_price)
        
        if 'to-price' in url_dict and url_dict['to-price']:
            to_price = int(url_dict['to-price'])
            q = q.filter(price__lte=to_price)

        context = {'home_list': q}
        return context



class PublisherDetailView(DetailView):

    model = Publisher
    template_name = 'homedetail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['book_list'] = Home.objects.all()
    #     return context

class HomeDetailView(DetailView):
    model = Home
    template_name = 'homedetail.html'
    success_url = '/'


class HomeCreateView(CreateView):
    model = Home
    fields = ['name', 'description',
              'price','category', 'pub_date','publisher', 'city', 'image']
    template_name = 'edithome.html'
    context_object_name = 'form'
    success_url = '/'   

class HomeUpdateView(UpdateView):
    model = Home
    fields = ['name', 'description',
              'price', 'publisher', 'city', 'category','image']
    template_name = 'edithome.html'
    context_object_name = 'form'
    success_url = '/'


class HomeDeleteView(DeleteView):
    model = Home
    success_url = '/'
    template_name = 'homedelete.html'


# class HomeListView(ListView):
#     model = Home
#     template_name = 'index.html'
    # context_object_name = 'books'
    # queryset = Book.objects.filter(title__icontains = 'j')

    