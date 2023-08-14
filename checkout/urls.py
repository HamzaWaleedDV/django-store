from django.urls import path
from checkout import views


urlpatterns = [
    path('stripe/config', views.stripe_config, name='checkout.strip_config'),
    path('stripe', views.stripe_transaction, name='checkout.strip'),
    path('paypal', views.paypal_trasaction, name='checkout.paypal')
]
