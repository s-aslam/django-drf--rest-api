from django.urls import path, include
from rest_api import user,product
from rest_framework.documentation import include_docs_urls

urlpatterns = [
	path('docs/', include_docs_urls(title='API')),
    # admin api
    path('user/login', user.Loginview.as_view(), name="user_login"),
    path('user/logout', user.LogoutView.as_view(), name="user_logout"),
    path('product', product.ProductListApi.as_view(), name="ProductListView"),
    path('product/<int:pk>', product.ProductDetailApi.as_view(), name="ProductDetailView"),
]
