from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('products/',views.list_products, name='list_products'),
    path('product_detail/<pk>',views.detail_products, name='product_detail'),
   
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)