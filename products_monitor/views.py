from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django_filters.views import FilterView
from django_filters import rest_framework as filters
from django.utils import timezone
from .filters import ProductFilter
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Brand, Product, SavedProduct

class IndexView(generic.ListView):
    template_name = 'products_monitor/index.html'
    context_object_name = 'brand_list'

    def get_queryset(self):
        return Brand.objects.all().order_by('name')

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['product_list_new'] = Product.objects.all().order_by('-original_release_date')[:4]
        context['product_list_restock'] = Product.objects.filter(restock_date__lte=timezone.now()).order_by('-restock_date')[:4]
        return context

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProductView(FilterView):
    template_name = 'products_monitor/products.html'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
    context_object_name = 'product_list'
    ordering_fields = ('price', 'restock_date', 'original_release_date', 'watchers')
    ordering = 'release_date'

    def get_queryset(self):
        return Product.objects.all()

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products_monitor/product_detail.html'

    def get_queryset(self):
        return Product.objects.all()

class BrandView(generic.ListView):
    template_name = 'products_monitor/brands.html'
    context_object_name = 'brand_list'

    def get_queryset(self):
        return Brand.objects.all().order_by('name')

class UserProfileView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'next'
    template_name = 'products_monitor/userprofile.html'
    context_object_name = 'saved_product_list'

    def get_queryset(self):
        current_user = self.request.user
        return SavedProduct.objects.filter(user=current_user.id)
