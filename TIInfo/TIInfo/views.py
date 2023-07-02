from django.http import HttpResponse
from django.shortcuts import render



from JammuAndKashmir.models import JammuAndKashmir
from HimachalPradesh.models import Himachal
from Punjab.models import Punjab
from Uttar_Pradesh.models import UttarPradesh
from Uttarakhand.models import Uttarakhand

from Assam.models import Assam
from Sikkim.models import Sikkim
from Meghalaya.models import Meghalaya
from Arunachal_Pradesh.models import ArunachalPradesh
from West_Bengal.models import WestBengal

from Andhra_Pradesh.models import AndhraPradesh
from Karnataka.models import Karnataka
from Kerala.models import Kerala
from Tamil_Nadu.models import TamilNadu
from Telangana.models import Telangana

from Gujarat.models import Gujarat
from Haryana.models import Haryana
from Rajasthan.models import Rajasthan
from Goa.models import Goa
from Maharashtra.models import Maharashtra

from New_Delhi.models import NewDelhi




def Homepage(request):
    return render(request, "index.html")

def AboutUs(request):
    return render(request, "aboutus.html")

def ContactUs(request):
    return render(request, "ContactUs.html")

def Explore(request):
    return render(request, "explore.html")

def FAQs(request):
    return render(request, "FAQ.html")

def TermsAndCondition(request):
    return render(request, "TermsAndCondition.html")

def PRIVACYpolicy(request):
    return render(request, "PrivacyPolicy.html")


# Explore page sidebar link
def BookGuide(request):
    return render(request, "BookGuide.html")

def Feedback(request):
    return render(request, "Feedback.html")

def Payment(request):
    return render(request, "Payment.html")



# NORTH places pages
def JammuKashmir(request):
    JandKdata = JammuAndKashmir.objects.all()

    data = {"JandKdata" : JandKdata}
    return render(request, "JammuKashmir.html", data)

def Himachalpradesh(request):
    himachaldata = Himachal.objects.all()

    data = {"himachaldata" : himachaldata}
    return render(request, "HimachalPradesh.html", data)

def UTTARPRADESH(request):
    uttarpradeshdata = UttarPradesh.objects.all()

    data = {"uttarpradeshdata" : uttarpradeshdata}
    return render(request, "UttarPradesh.html" , data)

def PUNJAB(request):
    punjabdata = Punjab.objects.all()

    data = {"punjabdata" : punjabdata}
    return render(request, "PUNJAB.html", data)

def UTTARAKHAND(request):
    uttarakhanddata = Uttarakhand.objects.all()

    data = {"uttarakhanddata" : uttarakhanddata}
    return render(request, "UTTARAKHAND.html" , data)


# EAST places pages
def ASSAM(request):
    assamdata = Assam.objects.all()

    data = {"assamdata" : assamdata}
    return render(request, "ASSAM.html" , data)

def SIKKIM(request):
    sikkimdata = Sikkim.objects.all()

    data = {"sikkimdata" : sikkimdata}
    return render(request, "SIKKIM.html" , data)

def MEGHALAYA(request):
    meghalayadata = Meghalaya.objects.all()

    data = {"meghalayadata" : meghalayadata}
    return render(request, "MEGHALAYA.html" , data)

def ARUNACHAL(request):
    arunachaldata = ArunachalPradesh.objects.all()

    data = {"arunachaldata" : arunachaldata}
    return render(request, "ArunachalPradesh.html" , data)

def WESTBengal(request):
    westbengaldata = WestBengal.objects.all()

    data = {"westbengaldata" : westbengaldata}
    return render(request, "WestBengal.html" , data)


# SOUTH places pages
def ANDHRAPRADESH(request):
    andhradata = AndhraPradesh.objects.all()

    data = {"andhradata" : andhradata}
    return render(request, "ANDHRAPRADESH.html" , data)

def KARNATAKA(request):
    karnatakadata = Karnataka.objects.all()

    data = {"karnatakadata" : karnatakadata}
    return render(request, "KARNATAKA.html" , data)

def KERALA(request):
    keraladata = Kerala.objects.all()

    data = {"keraladata" : keraladata}
    return render(request, "KERALA.html" , data)

def TAMILNADU(request):
    tamildata = TamilNadu.objects.all()

    data = {"tamildata" : tamildata}
    return render(request, "TAMILNADU.html" , data)

def TELANGANA(request):
    telanganadata = Telangana.objects.all()

    data = {"telanganadata" : telanganadata}
    return render(request, "TELANGANA.html" , data)


# WEST places pages
def GUJARAT(request):
    gujaratdata = Gujarat.objects.all()

    data = {"gujaratdata" : gujaratdata}
    return render(request, "GUJARAT.html" , data)

def HARYANA(request):
    haryanadata = Haryana.objects.all()

    data = {"haryanadata" : haryanadata}
    return render(request, "HARYANA.html" , data)

def RAJASTHAN(request):
    rajasthandata = Rajasthan.objects.all()

    data = {"rajasthandata" : rajasthandata}
    return render(request, "RAJASTHAN.html" , data)

def GOA(request):
    goadata = Goa.objects.all()

    data = {"goadata" : goadata}
    return render(request, "GOA.html" , data)

def MAHARASHTRA(request):
    maharashtradata = Maharashtra.objects.all()

    data = {"maharashtradata" : maharashtradata}
    return render(request, "MAHARASHTRA.html" , data)

# Center pages
def NEWDelhi(request):
    newdelhidata = NewDelhi.objects.all()

    data = {"newdelhidata" : newdelhidata}
    return render(request, "NewDelhi.html" , data)
