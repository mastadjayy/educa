from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static 
from django.conf import settings
from .views import index
from core.courses.views import CourseListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    
    path("course/", include("core.courses.urls")),

    path("", CourseListView.as_view(), name="course_list"),

    path('students/', include('core.students.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
