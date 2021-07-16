from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import hello_world, AccountCreateView, AccountDetailView

app_name = 'accountapp'
urlpatterns = [
    # name은 route의 이름
    path('hello_world/', hello_world, name='hello_world'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # 클래스에는 .as_view 필요
    path('create/', AccountCreateView.as_view(), name='create'),
    path('datail/<int:pk>', AccountDetailView.as_view(), name='detail'),

]
