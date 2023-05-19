from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)