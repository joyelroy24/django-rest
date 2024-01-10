from django.urls import path

from . import views
from . import viewset

urlpatterns=[

    path('<int:pk>',views.ProductDeleteAPIView.as_view()),
    path('create',views.product_alt_vieW,name='create'),
    path('update/<int:pk>',views.productMixinView.as_view(),name='product-detail'),
    path('delete/<int:pk>',views.productMixinView.as_view()),
    path('',views.ProductlistCreateAPIView.as_view(),name='product-list'),
    path('list_viewset',viewset.produt_list_view)
]