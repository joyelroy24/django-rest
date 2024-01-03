from django.urls import path

from . import views

urlpatterns=[

    path('<int:pk>',views.product_alt_vieW),
    path('create',views.product_alt_vieW,name='create'),
    path('update/<int:pk>',views.product_alt_vieW),
    path('delete/<int:pk>',views.product_alt_vieW),
]