from django.urls import path
from .import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name="home"),
    path("add/", views.AddRecipe, name="Add"),
    path("search/", views.serach, name="search"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
]
