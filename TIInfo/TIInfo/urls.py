"""
URL configuration for TIInfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path , include
from TIInfo import views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homepage,name="homepage"),
    path('aboutus/',views.AboutUs,name="aboutus"),
    path('explore/',views.Explore,name="explore"),
    path('contactus/',views.ContactUs,name="contactus"),

    path('book-a-guide/',views.BookGuide,name="book-a-guide"),
    path('payment/',views.Payment,name="payment"),
    path('feedback/',views.Feedback,name="feedback"),

# North Page Link
    path('jammukashmir/',views.JammuKashmir,name="jammukashmir"),
    path('himachal-pradesh/',views.Himachalpradesh,name="himachalpradesh"),
    path('punjab/',views.PUNJAB,name="punjab"),
    path('uttar-pradesh/',views.UTTARPRADESH,name="uttarpradesh"),
    path('uttarakhand/',views.UTTARAKHAND,name="uttarakhand"),

# East Page Link
    path('assam/',views.ASSAM,name="assam"),
    path('sikkim/',views.SIKKIM,name="sikkim"),
    path('meghalaya/',views.MEGHALAYA,name="meghalaya"),
    path('arunachalpradesh/',views.ARUNACHAL,name="arunachalpradesh"),
    path('westbengal/',views.WESTBengal,name="westbengal"),

# South Page Link
    path('andhrapradesh/',views.ANDHRAPRADESH,name="andhrapradesh"),
    path('karnataka/',views.KARNATAKA,name="karnataka"),
    path('kerala/',views.KERALA,name="kerala"),
    path('tamilnadu/',views.TAMILNADU,name="tamilnadu"),
    path('telangana/',views.TELANGANA,name="telangana"),
    
# West Page Link
    path('gujarat/',views.GUJARAT,name="gujarat"),
    path('haryana/',views.HARYANA,name="haryana"),
    path('rajasthan/',views.RAJASTHAN,name="rajasthan"),
    path('goa/',views.GOA,name="goa"),
    path('maharashtra/',views.MAHARASHTRA,name="maharashtra"),


    path('newdelhi/',views.NEWDelhi,name="newdelhi"),



    path("jammu-kashmir/", include("JammuAndKashmir.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
