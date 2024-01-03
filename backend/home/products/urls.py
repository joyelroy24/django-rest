from django.urls import path

from . import views

urlpatterns=[

    path('<int:pk>',views.product_alt_vieW),
    path('create',views.product_alt_vieW,name='create'),
    path('update/<int:pk>',views.ProductUpdateAPIView.as_view()),
    path('delete/<int:pk>',views.ProductDeleteAPIView.as_view()),
]