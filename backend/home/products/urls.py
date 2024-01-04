from django.urls import path

from . import views

urlpatterns=[

    path('<int:pk>',views.productMixinView.as_view()),
    path('create',views.product_alt_vieW,name='create'),
    path('update/<int:pk>',views.productMixinView.as_view()),
    path('delete/<int:pk>',views.productMixinView.as_view()),
    path('',views.productMixinView.as_view())
]