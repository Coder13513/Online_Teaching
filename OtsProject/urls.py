"""OtsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('authApi/',include('authentication.urls')),     
    path('studentApi/',include('student.urls')),
    path('teacherApi/',include('teacher.urls')),
    path('subjectApi/',include('subject.urls')),  
    path('chapterApi/',include('chapter.urls')),  
    path('lectureApi/',include('lecture.urls')),
    path('classApi/',include('classes.urls')),  
    # path('assignApi/',include('assignment.urls')),
  ]
#   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

