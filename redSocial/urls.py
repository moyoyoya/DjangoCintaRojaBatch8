from django.conf.urls import url, include
from django.contrib import admin
from posts import views as views2

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^cuentas/',
    	include('cuentas.urls')),


    url(r'^posts/', 
    	include('posts.urls'))
    
]
