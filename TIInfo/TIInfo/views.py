from django.http import HttpResponse
from django.shortcuts import render
from GuideBooking.models import Guide_Booking
from django.contrib import messages


from JammuAndKashmir.models import JammuAndKashmir, Gulmarg , Srinagar, Pahalgam, Anantnag
from HimachalPradesh.models import Himachal, Manali, Kasol, Shimla, Dalhousie
from Punjab.models import Punjab, Amritsar, Pathankot
from Uttar_Pradesh.models import UttarPradesh , Agra, Varanasi, Vrindavan, Lucknow, Mathura, Allahabad, Ayodhya, Meerut
from Uttarakhand.models import Uttarakhand, Rishikesh, Auli, Nainital, Dehradun,  Mussoorie, Haridwar

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
    data = {'title' : 'Travel India Info | Homepage'
        
    }
    return render(request, "index.html", data)

def AboutUs(request):
    data = {'title' : 'Travel India Info | About Us'
        
    }
    return render(request, "aboutus.html", data)

def ContactUs(request):
    data = {'title' : 'Travel India Info | Contact Us'
        
    }
    return render(request, "ContactUs.html", data)

def Explore(request):
    data = {'title' : 'Travel India Info | Explore'
        
    }
    return render(request, "explore.html", data)

def FAQs(request):
    data = {'title' : 'Travel India Info | FAQs'
        
    }
    return render(request, "FAQ.html", data)

def TermsAndCondition(request):
    data = {'title' : 'Travel India Info | Terms & Conditions'
        
    }
    return render(request, "TermsAndCondition.html", data)

def PRIVACYpolicy(request):
    data = {'title' : 'Travel India Info | Privacy Policy'
        
    }
    return render(request, "PrivacyPolicy.html", data)

def CUSTOMERReviews(request):
    data = {'title' : 'Travel India Info | Customers Review'
        
    }
    return render(request, "CustomerReviews.html", data)


# index services
def Mountains(request):
    data = {'title' : 'Travel India Info | Mountains'
        
    }
    return render(request, "Mountains.html", data)

def Monuments(request):
    data = {'title' : 'Travel India Info | Monuments'
        
    }
    return render(request, "Monuments.html", data)

def Beaches(request):
    data = {'title' : 'Travel India Info | Beaches'
        
    }
    return render(request, "Beaches.html", data)




# Explore page sidebar link

def saveBookingDetails(request):
    if request.method=="POST":
        if request.POST.get('firstname')=="":
            return render(request,"BookGuide.html",{'error':True})
        elif request.POST.get('lastname')=="":
            return render(request,"BookGuide.html",{'error':True})
        elif request.POST.get('inlineRadioOptions')=="":
            return render(request,"BookGuide.html",{'error':True})
        elif request.POST.get('email')=="":
            return render(request,"BookGuide.html",{'error':True})
        elif request.POST.get('phone')=="":
            return render(request,"BookGuide.html",{'error':True})
        elif request.POST.get('addressline1')=="":
            return render(request,"BookGuide.html",{'error':True})
        elif request.POST.get('Country')=="":
            return render(request,"BookGuide.html",{'error':True})
        elif request.POST.get('City')=="":
            return render(request,"BookGuide.html",{'error':True})
        elif request.POST.get('State')=="":
            return render(request,"BookGuide.html",{'error':True})
        elif request.POST.get('guideplace')=="":
            return render(request,"BookGuide.html",{'error':True})
        elif request.POST.get('guidelanguage')=="":
            return render(request,"BookGuide.html",{'error':True})
        elif request.POST.get('date')=="":
            return render(request,"BookGuide.html",{'error':True})
        
    else:
        print("invalid method")


    if request.method == "POST" :
        f_name = request.POST.get("firstname")
        l_name = request.POST.get("lastname")
        g_radio_option = request.POST.get("inlineRadioOptions")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        addressline1 = request.POST.get("addressline1")
        addressline2 = request.POST.get("addressline2")
        country = request.POST.get("Country")
        city = request.POST.get("City")
        state = request.POST.get("State")

        guide_place = request.POST.get("guideplace")
        guide_language = request.POST.get("guidelanguage")
        avail_date = request.POST.get("date")

        if not g_radio_option:
            return render(request, "BookGuide.html", {'error': True})
        
        booking_details = Guide_Booking(First_name=f_name, Last_name=l_name, Gender_identity=g_radio_option, Email=email, Phone=phone, Address1=addressline1,
                                        Address2=addressline2, Country=country, City=city, State=state, Guide_Place=guide_place, Guide_Language=guide_language, Availability_Date=avail_date)
        booking_details.save()

        # Add success message
        messages.success(request, "Form submitted successfully!")


        return render(request, "Payment.html")
    
    return render(request, "BookGuide.html")


def BookGuide(request):
    data = {'title' : 'Travel India Info | Enter Details to Book a Guide'
        
    }
    return render(request, "BookGuide.html" , data)
    
def Feedback(request):
    data = {'title' : 'Travel India Info | Feedback'
        
    }
    return render(request, "Feedback.html" , data)

def Payment(request):
    data = {'title' : 'Travel India Info | Payment Page'
        
    }
    return render(request, "Payment.html" , data)



# NORTH places pages
def JammuKashmir(request):
    JandKdata = JammuAndKashmir.objects.all()

    data = {'title' : 'Travel India Info | Jammu & Kashmir',
        "JandKdata" : JandKdata}
    return render(request, "JammuKashmir.html", data)

def GULMARG(request):
    gulmargdata = Gulmarg.objects.all()

    data = {'title' : 'Travel India Info | Gulmarg',
        "gulmargdata" : gulmargdata}
    return render(request, "GULMARG.html", data)

def SRINAGAR(request):
    srinagardata = Srinagar.objects.all()

    data = {'title' : 'Travel India Info | Srinagar',
        "srinagardata" : srinagardata}
    return render(request, "SRINAGAR.html", data)

def PAHALGAM(request):
    pahalgamdata = Pahalgam.objects.all()

    data = {'title' : 'Travel India Info | Pahalgam',
        "pahalgamdata" : pahalgamdata}
    return render(request, "PAHALGAM.html", data)

def ANANTNAG(request):
    anantnagdata = Anantnag.objects.all()

    data = {'title' : 'Travel India Info | Anantnag',
        "anantnagdata" : anantnagdata}
    return render(request, "ANANTNAG.html", data)





def Himachalpradesh(request):
    himachaldata = Himachal.objects.all()

    data = {'title' : 'Travel India Info | Himachal Pradesh',
        "himachaldata" : himachaldata}
    return render(request, "HimachalPradesh.html", data)

def MANALI(request):
    manalidata = Manali.objects.all()

    data = {'title' : 'Travel India Info | Manali',
        "manalidata" : manalidata}
    return render(request, "MANALI.html", data)

def KASOL(request):
    kasoldata = Kasol.objects.all()

    data = {'title' : 'Travel India Info | Kasol',
        "kasoldata" : kasoldata}
    return render(request, "KASOL.html", data)

def SHIMLA(request):
    shimladata = Shimla.objects.all()

    data = {'title' : 'Travel India Info | Shimla',
        "shimladata" : shimladata}
    return render(request, "SHIMLA.html", data)

def DALHOUSIE(request):
    dalhousiedata = Dalhousie.objects.all()

    data = {'title' : 'Travel India Info | Dalhousie',
        "dalhousiedata" : dalhousiedata}
    return render(request, "DALHOUSIE.html", data)





def UTTARPRADESH(request):
    uttarpradeshdata = UttarPradesh.objects.all()

    data = {'title' : 'Travel India Info | Uttar Pradesh',
        "uttarpradeshdata" : uttarpradeshdata}
    return render(request, "UttarPradesh.html" , data)

def AGRA(request):
    agradata = Agra.objects.all()

    data = {'title' : 'Travel India Info | AGRA',
        "agradata" : agradata}
    return render(request, "AGRA.html" , data)

def VARANASI(request):
    varanasidata = Varanasi.objects.all()

    data = {'title' : 'Travel India Info | Varanasi',
        "varanasidata" : varanasidata}
    return render(request, "VARANASI.html" , data)

def VRINDAVAN(request):
    vrindavandata = Vrindavan.objects.all()

    data = {'title' : 'Travel India Info | Vrindavan',
        "vrindavandata" : vrindavandata}
    return render(request, "VRINDAVAN.html" , data)

def LUCKNOW(request):
    lucknowdata = Lucknow.objects.all()

    data = {'title' : 'Travel India Info | Lucknow',
        "lucknowdata" : lucknowdata}
    return render(request, "LUCKNOW.html" , data)

def ALLAHABAD(request):
    allahabaddata = Allahabad.objects.all()

    data = {'title' : 'Travel India Info | Allahabad',
        "allahabaddata" : allahabaddata}
    return render(request, "ALLAHABAD.html" , data)

def MATHURA(request):
    mathuradata = Mathura.objects.all()

    data = {'title' : 'Travel India Info | Mathura',
        "mathuradata" : mathuradata}
    return render(request, "MATHURA.html" , data)

def AYODHYA(request):
    ayodhyadata = Ayodhya.objects.all()

    data = {'title' : 'Travel India Info | Ayodhya',
        "ayodhyadata" : ayodhyadata}
    return render(request, "AYODHYA.html" , data)

def MEERUT(request):
    meerutdata = Meerut.objects.all()

    data = {'title' : 'Travel India Info | Meerut',
        "meerutdata" : meerutdata}
    return render(request, "MEERUT.html" , data)




def PUNJAB(request):
    punjabdata = Punjab.objects.all()

    data = {'title' : 'Travel India Info | Punjab',
        "punjabdata" : punjabdata}
    return render(request, "PUNJAB.html", data)

def AMRITSAR(request):
    amritsardata = Amritsar.objects.all()

    data = {'title' : 'Travel India Info | Amritsar',
        "amritsardata" : amritsardata}
    return render(request, "AMRITSAR.html", data)

def PATHANKOT(request):
    pathankotdata = Pathankot.objects.all()

    data = {'title' : 'Travel India Info | Pathankot',
        "pathankotdata" : pathankotdata}
    return render(request, "PATHANKOT.html", data)




def UTTARAKHAND(request):
    uttarakhanddata = Uttarakhand.objects.all()

    data = {'title' : 'Travel India Info | Uttarakhand',
        "uttarakhanddata" : uttarakhanddata}
    return render(request, "UTTARAKHAND.html" , data)


def RISHIKESH(request):
    rishikeshdata = Rishikesh.objects.all()

    data = {'title' : 'Travel India Info | Rishikesh',
        "rishikeshdata" : rishikeshdata}
    return render(request, "RISHIKESH.html" , data)

def AULI(request):
    aulidata = Auli.objects.all()

    data = {'title' : 'Travel India Info | Auli',
        "aulidata" : aulidata}
    return render(request, "AULI.html" , data)

def NAINITAL(request):
    nainitaldata = Nainital.objects.all()

    data = {'title' : 'Travel India Info | Nainital',
        "nainitaldata" : nainitaldata}
    return render(request, "NAINITAL.html" , data)

def DEHRADUN(request):
    dehradundata = Dehradun.objects.all()

    data = {'title' : 'Travel India Info | Dehradun',
        "dehradundata" : dehradundata}
    return render(request, "DEHRADUN.html" , data)

def MUSSOORIE(request):
    mussooriedata = Mussoorie.objects.all()

    data = {'title' : 'Travel India Info | Mussoorie',
        "mussooriedata" : mussooriedata}
    return render(request, "MUSSOORIE.html" , data)

def HARIDWAR(request):
    haridwardata = Haridwar.objects.all()

    data = {'title' : 'Travel India Info | Haridwar',
        "haridwardata" : haridwardata}
    return render(request, "HARIDWAR.html" , data)





# EAST places pages
def ASSAM(request):
    assamdata = Assam.objects.all()

    data = {'title' : 'Travel India Info | Assam',
        "assamdata" : assamdata}
    return render(request, "ASSAM.html" , data)

def SIKKIM(request):

    sikkimdata = Sikkim.objects.all()

    data = { 'title' : 'Travel India Info | Sikkim',
            "sikkimdata" : sikkimdata}
    return render(request, "SIKKIM.html" , data)

def MEGHALAYA(request):
    meghalayadata = Meghalaya.objects.all()

    data = {'title' : 'Travel India Info | Meghalaya',
        "meghalayadata" : meghalayadata}
    return render(request, "MEGHALAYA.html" , data)

def ARUNACHAL(request):
    arunachaldata = ArunachalPradesh.objects.all()

    data = {'title' : 'Travel India Info | Arunachal Pradesh',
        "arunachaldata" : arunachaldata}
    return render(request, "ArunachalPradesh.html" , data)

def WESTBengal(request):
    westbengaldata = WestBengal.objects.all()

    data = {'title' : 'Travel India Info | West Bengal',
        "westbengaldata" : westbengaldata}
    return render(request, "WestBengal.html" , data)


# SOUTH places pages
def ANDHRAPRADESH(request):
    andhradata = AndhraPradesh.objects.all()

    data = {'title' : 'Travel India Info | Andhra Pradesh',
        "andhradata" : andhradata}
    return render(request, "ANDHRAPRADESH.html" , data)

def KARNATAKA(request):
    karnatakadata = Karnataka.objects.all()

    data = {'title' : 'Travel India Info | Karnataka',
        "karnatakadata" : karnatakadata}
    return render(request, "KARNATAKA.html" , data)

def KERALA(request):
    keraladata = Kerala.objects.all()

    data = {'title' : 'Travel India Info | Kerala',
        "keraladata" : keraladata}
    return render(request, "KERALA.html" , data)

def TAMILNADU(request):
    tamildata = TamilNadu.objects.all()

    data = {'title' : 'Travel India Info | Tamil Nadu',
        "tamildata" : tamildata}
    return render(request, "TAMILNADU.html" , data)

def TELANGANA(request):
    telanganadata = Telangana.objects.all()

    data = {'title' : 'Travel India Info | Telangana',
        "telanganadata" : telanganadata}
    return render(request, "TELANGANA.html" , data)


# WEST places pages
def GUJARAT(request):
    gujaratdata = Gujarat.objects.all()

    data = {'title' : 'Travel India Info | Gujarat',
        "gujaratdata" : gujaratdata}
    return render(request, "GUJARAT.html" , data)

def HARYANA(request):
    haryanadata = Haryana.objects.all()

    data = {'title' : 'Travel India Info | Haryana',
        "haryanadata" : haryanadata}
    return render(request, "HARYANA.html" , data)

def RAJASTHAN(request):
    rajasthandata = Rajasthan.objects.all()

    data = {'title' : 'Travel India Info | Rajasthan',
        "rajasthandata" : rajasthandata}
    return render(request, "RAJASTHAN.html" , data)

def GOA(request):
    goadata = Goa.objects.all()

    data = {'title' : 'Travel India Info | Goa',
        "goadata" : goadata}
    return render(request, "GOA.html" , data)

def MAHARASHTRA(request):
    maharashtradata = Maharashtra.objects.all()

    data = {'title' : 'Travel India Info | Maharashtra',
        "maharashtradata" : maharashtradata}
    return render(request, "MAHARASHTRA.html" , data)

# Center pages
def NEWDelhi(request):
    newdelhidata = NewDelhi.objects.all()

    data = {'title' : 'Travel India Info | New Delhi',
        "newdelhidata" : newdelhidata}
    return render(request, "NewDelhi.html" , data)
