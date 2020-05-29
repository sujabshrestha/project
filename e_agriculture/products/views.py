from django.shortcuts import render
from .models import products
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'products': products.objects.all()
    }
    return render(request,'products/home.html', context)

class ProductListView(ListView):
    model = products
    template_name = 'products/home.html'
    context_object_name = 'products'
    ordering = ['-date_posted']


class ProductDetailView(DetailView):
    model = products

class ProductCreateView(LoginRequiredMixin,CreateView):
    model = products
    fields = ['title','image','content','author']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = products
    fields = ['title','image','content','author']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        return False        


class ProductDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = products
    success_url = '/'
    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        return False        


def about(request):
    return render(request,'products/about.html',{'title':'About us'})

    