from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views


router=DefaultRouter()

#when use router here register
router.register('image-contact-update',views.ImageUploadViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('login/',views.UserLoginApiView.as_view(), name='login'),
    path('logout/',views.UserLogOutView.as_view(), name='logout'),
    path('signup/',views.SignupAPIView.as_view(), name='signup'),
    path('changepassword/',views.ChangePasswordView.as_view(), name='changepassword'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
]