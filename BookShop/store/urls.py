from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='store'), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    
	
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    
]