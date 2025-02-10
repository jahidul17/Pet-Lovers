from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views


router=DefaultRouter()

router.register('type',views.CategoryViewSet)
router.register('origin',views.OriginViewSet)

urlpatterns = [
    
    path('',include(router.urls)),
    
]


