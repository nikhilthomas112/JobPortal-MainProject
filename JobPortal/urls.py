"""JobPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from Account.urls import urlpatterns as accounts
from MetaData.urls import urlpatterns as metadata
from Employer.urls import urlpatterns as employer
from Employee.urls import urlpatterns as employee
from Admin.urls import urlpatterns as app_admin
from Reports.urls import urlpatterns as reports


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(accounts)),
    path('', include(metadata)),
    path('', include(employer)),
    path('', include(employee)),
    path('', include(app_admin)),
    path('', include(reports)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "MetaData.views.error_page_400"
handler500 = "MetaData.views.error_page_500"
handler403 = "MetaData.views.error_page_400"
handler400 = "MetaData.views.error_page_400"
