from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # portfolioのurls.pyを読み込み
    path('', include('portfolio.urls')),
    #上記のinclude内を、変えることでどのフォルダのurl.pyを読み込みdjangoに伝えるかを設定できる。
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#上記の部分は、jsやcssを読み込む際のstaticをsetting.pyで設定した、どのファイルを読み込むかを伝える。