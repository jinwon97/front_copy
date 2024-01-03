from django.urls import path
from . import views

urlpatterns = [
    path("getCSRF", views.GetCSRFToken.as_view()),
    path("signin/", views.SignInView.as_view()),
    path("login/", views.LoginView.as_view()),
    # path("findid/", views.FindIDView.as_view()),
    # path("findpw/", views.FindPasswordView.as_view()),
    # path("updateuser/", views.UpdateUserView.as_view()),
    # path("deleteuser/", views.DeleteUserView.as_view()),
    # path("checkpassword/", views.PWCheckView.as_view()),
    # path('login/', views.LoginView.as_view(), name='login'),
    #path('logout/', views.LogoutView.as_view(), name='logout'),
]
