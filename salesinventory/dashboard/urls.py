from django.urls import path
from . import views
from . import views as user_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', user_view.register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    # path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/category/', views.category, name="category"),
    path('dashboard/addcategory/', views.addcategory, name="addcategory"),
    path('dashboard/products/', views.products, name="products"),
    path('dashboard/addproduct/', views.addproduct, name="addproduct"),
    path('dashboard/category_data/', views.category_data, name="category_data"),
    path('dashboard/editproduct/<int:id>', views.editproduct, name="editproduct"),
    path('dashboard/updateproduct/<int:id>', views.updateproduct, name="updateproduct"),
    path('dashboard/deleteproduct/<int:id>', views.deleteproduct, name="deleteproduct"),
    path('dashboard/stocks/', views.stocks, name="stocks"),
    path('dashboard/addstocks/<int:id>', views.addstocks, name="addstocks"),
    path('dashboard/add_stocks/<int:id>', views.add_stocks, name="add_stocks"),
    path('dashboard/minusstocks/<int:id>', views.minusstocks, name="minusstocks"),
    path('dashboard/minus_stocks/<int:id>', views.minus_stocks, name="minus_stocks"),
    path('dashboard/sales/', views.sales, name="sales"),
    path('dashboard/addsales/<int:id>', views.addsales, name="addsales"),
    path('dashboard/add_sales/<int:id>', views.add_sales, name="add_sales"),
    path('dashboard/salesreport/', views.salesreport, name="salesreport"),

]
