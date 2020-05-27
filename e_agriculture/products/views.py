from django.shortcuts import render
from .models import products
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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



def about(request):
    return render(request,'products/about.html',{'title':'About us'})