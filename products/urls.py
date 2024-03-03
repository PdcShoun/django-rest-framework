from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProductListCreate, ProductRetrieveUpdateDestroy

urlpatterns = [
    path('', ProductListCreate.as_view()),
    path('<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
