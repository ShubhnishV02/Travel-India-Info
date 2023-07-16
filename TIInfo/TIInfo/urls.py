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
    path('faqs/',views.FAQs,name="faqs"),
    path('termscondition/',views.TermsAndCondition,name="termscondition"),
    path('privacypolicy/',views.PRIVACYpolicy,name="privacypolicy"),
    path('customerreview/',views.CUSTOMERReviews,name="customerreview"),


    path('',include('authentication.urls')),
    path('search/',views.SEARCH,name="search"),
    

    path('book-a-guide/',views.BookGuide,name="book-a-guide"),
    path('savebookdetails/',views.saveBookingDetails,name="savebookdetails"),
    path('payment/',views.Payment,name="payment"),
    path('feedback/',views.FEEDback,name="feedback"),
    path('save-feedback/',views.saveFEEDback,name="save-feedback"),
    path('thank-you/',views.Thankyou,name="thank-you"),


    path('mountains/',views.Mountains,name="mountains"),
    path('monuments/',views.Monuments,name="monuments"),
    path('beaches/',views.Beaches,name="beaches"),

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

# Center Page Link
    path('newdelhi/',views.NEWDelhi,name="newdelhi"),


# extra pages
    path('manali/',views.MANALI,name="manali"),
    path('kasol/',views.KASOL,name="kasol"),
    path('shimla/',views.SHIMLA,name="shimla"),
    path('dalhousie/',views.DALHOUSIE,name="dalhousie"),

    path('gulmarg/',views.GULMARG,name="gulmarg"),
    path('srinagar/',views.SRINAGAR,name="srinagar"),
    path('pahalgam/',views.PAHALGAM,name="pahalgam"),
    path('anantnag/',views.ANANTNAG,name="anantnag"),

    path('amritsar/',views.AMRITSAR,name="amritsar"),
    path('pathankot/',views.PATHANKOT,name="pathankot"),

    path('agra/',views.AGRA,name="agra"),
    path('varanasi/',views.VARANASI,name="varanasi"),
    path('vrindavan/',views.VRINDAVAN,name="vrindavan"),
    path('lucknow/',views.LUCKNOW,name="lucknow"),
    path('mathura/',views.MATHURA,name="mathura"),
    path('allahabad/',views.ALLAHABAD,name="allahabad"),
    path('ayodhya/',views.AYODHYA,name="ayodhya"),
    path('meerut/',views.MEERUT,name="meerut"),

    path('rishikesh/',views.RISHIKESH,name="rishikesh"),
    path('auli/',views.AULI,name="auli"),
    path('nainital/',views.NAINITAL,name="nainital"),
    path('dehradun/',views.DEHRADUN,name="dehradun"),
    path('mussoorie/',views.MUSSOORIE,name="mussoorie"),
    path('haridwar/',views.HARIDWAR,name="haridwar"),

    path('majuli/',views.MAJULI,name="majuli"),
    path('guwahati/',views.GUWAHATI,name="guwahati"),

    path('gangtok/',views.GANGTOK,name="gangtok"),
    path('westsikkim/',views.WESTSIKKIM,name="westsikkim"),
    path('northsikkim/',views.NORTHSIKKIM,name="northsikkim"),

    path('shillong/',views.SHILLONG,name="shillong"),
    path('cherrapunji/',views.CHERRAPUNJI,name="cherrapunji"),
    path('williamnagar/',views.WILLIAMNAGAR,name="williamnagar"),

    path('tawang/',views.TAWANG,name="tawang"),
    path('itanagar/',views.ITANAGAR,name="itanagar"),

    path('kolkata/',views.KOLKATA,name="kolkata"),
    path('darjeeling/',views.DARJEELING,name="darjeeling"),
    path('sundarbans/',views.SUNDARBANS,name="sundarbans"),
    path('siliguri/',views.SILIGURI,name="siliguri"),

    path('arakuvalley/',views.ARAKUvalley,name="arakuvalley"),
    path('visakhapatnam/',views.VISAKHAPATNAM,name="visakhapatnam"),
    path('tirupati/',views.TIRUPATI,name="tirupati"),
    path('anantapur/',views.ANANTAPUR,name="anantapur"),
    path('kurnool/',views.KURNOOL,name="kurnool"),

    path('coorg/',views.COORG,name="coorg"),
    path('badami/',views.BADAMI,name="badami"),
    path('hampi/',views.HAMPI,name="hampi"),

    path('munnar/',views.MUNNAR,name="munnar"),
    path('kumarakom/',views.KUMARAKOM,name="kumarakom"),

    path('rameshwaram/',views.RAMESHWARAM,name="rameshwaram"),
    path('yercaud/',views.YERCAUD,name="yercaud"),
    path('kodaikanal/',views.KODAIKANAL,name="kodaikanal"),
    path('ooty/',views.OOTY,name="ooty"),
    path('chennai/',views.CHENNAI,name="chennai"),

    path('hyderabad/',views.HYDERABAD,name="hyderabad"),
    path('warangal/',views.WARANGAL,name="warangal"),

    path('ahmedabad/',views.AHMEDABAD,name="ahmedabad"),
    path('kutch/',views.KUTCH,name="kutch"),
    path('vadodara/',views.VADODARA,name="vadodara"),

    path('chandigarh/',views.CHANDIGARH,name="chandigarh"),

    path('jaipur/',views.JAIPUR,name="jaipur"),
    path('udaipur/',views.UDAIPUR,name="udaipur"),
    path('jaisalmer/',views.JAISALMER,name="jaisalmer"),
    path('jodhpur/',views.JODHPUR,name="jodhpur"),

    path('mahabaleshwar/',views.MAHABALESHWAR,name="mahabaleshwar"),
    path('mumbai/',views.MUMBAI,name="mumbai"),



    path("jammu-kashmir/", include("JammuAndKashmir.urls")),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
