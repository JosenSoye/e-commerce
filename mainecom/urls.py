from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('register',views.register,name='signup'),
    path('login',views.loginpage,name='login'),
    path('logout',views.logoutpage,name='logout'),
    path('staffpage',views.staffpage),
    path('editpage1',views.editpage,name='editproduct'),
    path('editpage2/<id>',views.edit,name='edit'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('productpage',views.productpage, name='productpage'),
    path('search/',views.search,name='search'),
    path('cartpage/<id>',views.detailpage,name='cartpage'),
    path('paymentpage',views.paymentpage,name='buyingpage'),
    path('confirmationpage',views.confirmationpage,name='confirmation')
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)