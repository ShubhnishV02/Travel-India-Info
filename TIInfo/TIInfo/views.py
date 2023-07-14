from django.http import HttpResponse
from django.shortcuts import render
from GuideBooking.models import Guide_Booking
from django.contrib import messages


from JammuAndKashmir.models import JammuAndKashmir, Gulmarg , Srinagar, Pahalgam, Anantnag
from HimachalPradesh.models import Himachal, Manali, Kasol, Shimla, Dalhousie
from Punjab.models import Punjab, Amritsar, Pathankot
from Uttar_Pradesh.models import UttarPradesh , Agra, Varanasi, Vrindavan, Lucknow, Mathura, Allahabad, Ayodhya, Meerut
from Uttarakhand.models import Uttarakhand, Rishikesh, Auli, Nainital, Dehradun,  Mussoorie, Haridwar

from Assam.models import Assam , Majuli, Guwahati
from Sikkim.models import Sikkim, Gangtok, WestSikkim, NorthSikkim
from Meghalaya.models import Meghalaya, Shillong, Cherrapunji, Williamnagar
from Arunachal_Pradesh.models import ArunachalPradesh, Tawang, Itanagar
from West_Bengal.models import WestBengal, Kolkata, Darjeeling, Sundarbans, Siliguri

from Andhra_Pradesh.models import AndhraPradesh, ArakuValley, Visakhapatnam, Tirupati, Anantapur,Kurnool
from Karnataka.models import Karnataka, Coorg, Badami, Hampi
from Kerala.models import Kerala, Munnar, Kumarakom
from Tamil_Nadu.models import TamilNadu, Rameshwaram, Yercaud, Kodaikanal, Ooty, Chennai
from Telangana.models import Telangana, Hyderabad, Warangal

from Gujarat.models import Gujarat, Ahmedabad, Kutch, Vadodara
from Haryana.models import Haryana, Chandigarh
from Rajasthan.models import Rajasthan, Jaipur, Udaipur, Jaisalmer, Jodhpur
from Goa.models import Goa
from Maharashtra.models import Maharashtra, Mahabaleshwar, Mumbai

from New_Delhi.models import NewDelhi
from Customer.models import Feedback




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
    
def saveFEEDback(request):
    data = {'title' : 'Travel India Info | Feedback'
    }

    if request.method=="POST":
        if request.POST.get('name')=="":
            return render(request,"FEEDback.html",{'error':True})
        elif request.POST.get('email')=="":
            return render(request,"FEEDback.html",{'error':True})
        elif request.POST.get('Country')=="":
            return render(request,"FEEDback.html",{'error':True})   
        elif request.POST.get('comment')=="":
            return render(request,"FEEDback.html",{'error':True})      
    else:
        print("invalid method")

    
    if request.method == "POST" :
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        country = request.POST.get("Country")
        message = request.POST.get("comment")

        feedback_details = Feedback(customer_name=name, customer_email=email, customer_phone=phone, customer_country=country, customer_message=message)
        feedback_details.save()
        return render(request, "Thankyou.html" , data)
    return render(request, "Thankyou.html" , data)


def FEEDback(request):
    data = {'title' : 'Travel India Info | Feedback'
    }
    return render(request, "FEEDback.html", data)

def Thankyou(request):
    data = {'title' : 'Travel India Info | Feedback'
    }
    return render(request, "Thankyou.html", data)



def Payment(request):
    data = {'title' : 'Travel India Info | Payment Page'
        
    }
    return render(request, "Payment.html" , data)



# NORTH places pages
def JammuKashmir(request):
    JandKdata = JammuAndKashmir.objects.all()

    data = {'title' : 'Travel India Info | Jammu & Kashmir',
        "JandKdata" : JandKdata}
    return render(request, "Jammu-Kashmir/JammuKashmir.html", data)

def GULMARG(request):
    gulmargdata = Gulmarg.objects.all()

    data = {'title' : 'Travel India Info | Gulmarg',
        "gulmargdata" : gulmargdata}
    return render(request, "Jammu-Kashmir/GULMARG.html", data)

def SRINAGAR(request):
    srinagardata = Srinagar.objects.all()

    data = {'title' : 'Travel India Info | Srinagar',
        "srinagardata" : srinagardata}
    return render(request, "Jammu-Kashmir/SRINAGAR.html", data)

def PAHALGAM(request):
    pahalgamdata = Pahalgam.objects.all()

    data = {'title' : 'Travel India Info | Pahalgam',
        "pahalgamdata" : pahalgamdata}
    return render(request, "Jammu-Kashmir/PAHALGAM.html", data)

def ANANTNAG(request):
    anantnagdata = Anantnag.objects.all()

    data = {'title' : 'Travel India Info | Anantnag',
        "anantnagdata" : anantnagdata}
    return render(request, "Jammu-Kashmir/ANANTNAG.html", data)





def Himachalpradesh(request):
    himachaldata = Himachal.objects.all()

    data = {'title' : 'Travel India Info | Himachal Pradesh',
        "himachaldata" : himachaldata}
    return render(request, "Himachal-Pradesh/HimachalPradesh.html", data)

def MANALI(request):
    manalidata = Manali.objects.all()

    data = {'title' : 'Travel India Info | Manali',
        "manalidata" : manalidata}
    return render(request, "Himachal-Pradesh/MANALI.html", data)

def KASOL(request):
    kasoldata = Kasol.objects.all()

    data = {'title' : 'Travel India Info | Kasol',
        "kasoldata" : kasoldata}
    return render(request, "Himachal-Pradesh/KASOL.html", data)

def SHIMLA(request):
    shimladata = Shimla.objects.all()

    data = {'title' : 'Travel India Info | Shimla',
        "shimladata" : shimladata}
    return render(request, "Himachal-Pradesh/SHIMLA.html", data)

def DALHOUSIE(request):
    dalhousiedata = Dalhousie.objects.all()

    data = {'title' : 'Travel India Info | Dalhousie',
        "dalhousiedata" : dalhousiedata}
    return render(request, "Himachal-Pradesh/DALHOUSIE.html", data)





def UTTARPRADESH(request):
    uttarpradeshdata = UttarPradesh.objects.all()

    data = {'title' : 'Travel India Info | Uttar Pradesh',
        "uttarpradeshdata" : uttarpradeshdata}
    return render(request, "Uttar-Pradesh/UttarPradesh.html" , data)

def AGRA(request):
    agradata = Agra.objects.all()

    data = {'title' : 'Travel India Info | AGRA',
        "agradata" : agradata}
    return render(request, "Uttar-Pradesh/AGRA.html" , data)

def VARANASI(request):
    varanasidata = Varanasi.objects.all()

    data = {'title' : 'Travel India Info | Varanasi',
        "varanasidata" : varanasidata}
    return render(request, "Uttar-Pradesh/VARANASI.html" , data)

def VRINDAVAN(request):
    vrindavandata = Vrindavan.objects.all()

    data = {'title' : 'Travel India Info | Vrindavan',
        "vrindavandata" : vrindavandata}
    return render(request, "Uttar-Pradesh/VRINDAVAN.html" , data)

def LUCKNOW(request):
    lucknowdata = Lucknow.objects.all()

    data = {'title' : 'Travel India Info | Lucknow',
        "lucknowdata" : lucknowdata}
    return render(request, "Uttar-Pradesh/LUCKNOW.html" , data)

def ALLAHABAD(request):
    allahabaddata = Allahabad.objects.all()

    data = {'title' : 'Travel India Info | Allahabad',
        "allahabaddata" : allahabaddata}
    return render(request, "Uttar-Pradesh/ALLAHABAD.html" , data)

def MATHURA(request):
    mathuradata = Mathura.objects.all()

    data = {'title' : 'Travel India Info | Mathura',
        "mathuradata" : mathuradata}
    return render(request, "Uttar-Pradesh/MATHURA.html" , data)

def AYODHYA(request):
    ayodhyadata = Ayodhya.objects.all()

    data = {'title' : 'Travel India Info | Ayodhya',
        "ayodhyadata" : ayodhyadata}
    return render(request, "Uttar-Pradesh/AYODHYA.html" , data)

def MEERUT(request):
    meerutdata = Meerut.objects.all()

    data = {'title' : 'Travel India Info | Meerut',
        "meerutdata" : meerutdata}
    return render(request, "Uttar-Pradesh/MEERUT.html" , data)




def PUNJAB(request):
    punjabdata = Punjab.objects.all()

    data = {'title' : 'Travel India Info | Punjab',
        "punjabdata" : punjabdata}
    return render(request, "Punjab/PUNJAB.html", data)

def AMRITSAR(request):
    amritsardata = Amritsar.objects.all()

    data = {'title' : 'Travel India Info | Amritsar',
        "amritsardata" : amritsardata}
    return render(request, "Punjab/AMRITSAR.html", data)

def PATHANKOT(request):
    pathankotdata = Pathankot.objects.all()

    data = {'title' : 'Travel India Info | Pathankot',
        "pathankotdata" : pathankotdata}
    return render(request, "Punjab/PATHANKOT.html", data)




def UTTARAKHAND(request):
    uttarakhanddata = Uttarakhand.objects.all()

    data = {'title' : 'Travel India Info | Uttarakhand',
        "uttarakhanddata" : uttarakhanddata}
    return render(request, "Uttarakhand/UTTARAKHAND.html" , data)


def RISHIKESH(request):
    rishikeshdata = Rishikesh.objects.all()

    data = {'title' : 'Travel India Info | Rishikesh',
        "rishikeshdata" : rishikeshdata}
    return render(request, "Uttarakhand/RISHIKESH.html" , data)

def AULI(request):
    aulidata = Auli.objects.all()

    data = {'title' : 'Travel India Info | Auli',
        "aulidata" : aulidata}
    return render(request, "Uttarakhand/AULI.html" , data)

def NAINITAL(request):
    nainitaldata = Nainital.objects.all()

    data = {'title' : 'Travel India Info | Nainital',
        "nainitaldata" : nainitaldata}
    return render(request, "Uttarakhand/NAINITAL.html" , data)

def DEHRADUN(request):
    dehradundata = Dehradun.objects.all()

    data = {'title' : 'Travel India Info | Dehradun',
        "dehradundata" : dehradundata}
    return render(request, "Uttarakhand/DEHRADUN.html" , data)

def MUSSOORIE(request):
    mussooriedata = Mussoorie.objects.all()

    data = {'title' : 'Travel India Info | Mussoorie',
        "mussooriedata" : mussooriedata}
    return render(request, "Uttarakhand/MUSSOORIE.html" , data)

def HARIDWAR(request):
    haridwardata = Haridwar.objects.all()

    data = {'title' : 'Travel India Info | Haridwar',
        "haridwardata" : haridwardata}
    return render(request, "Uttarakhand/HARIDWAR.html" , data)





# EAST places pages
def ASSAM(request):
    assamdata = Assam.objects.all()

    data = {'title' : 'Travel India Info | Assam',
        "assamdata" : assamdata}
    return render(request, "Assam/ASSAM.html" , data)


def MAJULI(request):
    majulidata = Majuli.objects.all()

    data = {'title' : 'Travel India Info | Majuli',
        "majulidata" : majulidata}
    return render(request, "Assam/MAJULI.html" , data)

def GUWAHATI(request):
    guwahatidata = Guwahati.objects.all()

    data = {'title' : 'Travel India Info | Guwahati',
        "guwahatidata" : guwahatidata}
    return render(request, "Assam/GUWAHATI.html" , data)





def SIKKIM(request):

    sikkimdata = Sikkim.objects.all()

    data = { 'title' : 'Travel India Info | Sikkim',
            "sikkimdata" : sikkimdata}
    return render(request, "Sikkim/SIKKIM.html" , data)


def GANGTOK(request):

    gangtokdata = Gangtok.objects.all()

    data = { 'title' : 'Travel India Info | Gangtok',
            "gangtokdata" : gangtokdata}
    return render(request, "Sikkim/GANGTOK.html" , data)

def WESTSIKKIM(request):

    westsikkimdata = WestSikkim.objects.all()

    data = { 'title' : 'Travel India Info | West Sikkim',
            "westsikkimdata" : westsikkimdata}
    return render(request, "Sikkim/WESTSIKKIM.html" , data)

def NORTHSIKKIM(request):

    northsikkimdata = NorthSikkim.objects.all()

    data = { 'title' : 'Travel India Info | North Sikkim',
            "northsikkimdata" : northsikkimdata}
    return render(request, "Sikkim/NORTHSIKKIM.html" , data)





def MEGHALAYA(request):
    meghalayadata = Meghalaya.objects.all()

    data = {'title' : 'Travel India Info | Meghalaya',
        "meghalayadata" : meghalayadata}
    return render(request, "Meghalaya/MEGHALAYA.html" , data)


def SHILLONG(request):
    shillongdata = Shillong.objects.all()

    data = {'title' : 'Travel India Info | Shillong',
        "shillongdata" : shillongdata}
    return render(request, "Meghalaya/SHILLONG.html" , data)

def CHERRAPUNJI(request):
    cherrapunjidata = Cherrapunji.objects.all()

    data = {'title' : 'Travel India Info | Cherrapunji',
        "cherrapunjidata" : cherrapunjidata}
    return render(request, "Meghalaya/CHERRAPUNJI.html" , data)

def WILLIAMNAGAR(request):
    williamnagardata = Williamnagar.objects.all()

    data = {'title' : 'Travel India Info | Williamnagar',
        "williamnagardata" : williamnagardata}
    return render(request, "Meghalaya/WILLIAMNAGAR.html" , data)





def ARUNACHAL(request):
    arunachaldata = ArunachalPradesh.objects.all()

    data = {'title' : 'Travel India Info | Arunachal Pradesh',
        "arunachaldata" : arunachaldata}
    return render(request, "Arunachal-Pradesh/ArunachalPradesh.html" , data)

def TAWANG(request):
    tawangdata = Tawang.objects.all()

    data = {'title' : 'Travel India Info | Tawang',
        "tawangdata" : tawangdata}
    return render(request, "Arunachal-Pradesh/TAWANG.html" , data)

def ITANAGAR(request):
    itanagardata = Itanagar.objects.all()

    data = {'title' : 'Travel India Info | Itanagar',
        "itanagardata" : itanagardata}
    return render(request, "Arunachal-Pradesh/ITANAGAR.html" , data)




def WESTBengal(request):
    westbengaldata = WestBengal.objects.all()

    data = {'title' : 'Travel India Info | West Bengal',
        "westbengaldata" : westbengaldata}
    return render(request, "West-Bengal/WESTBENGAL.html" , data)

def KOLKATA(request):
    kolkatadata = Kolkata.objects.all()

    data = {'title' : 'Travel India Info | Kolkata',
        "kolkatadata" : kolkatadata}
    return render(request, "West-Bengal/KOLKATA.html" , data)

def DARJEELING(request):
    darjeelingdata = Darjeeling.objects.all()

    data = {'title' : 'Travel India Info | Darjeeling',
        "darjeelingdata" : darjeelingdata}
    return render(request, "West-Bengal/DARJEELING.html" , data)

def SUNDARBANS(request):
    sundarbansdata = Sundarbans.objects.all()

    data = {'title' : 'Travel India Info | Sundarbans',
        "sundarbansdata" : sundarbansdata}
    return render(request, "West-Bengal/SUNDARBANS.html" , data)

def SILIGURI(request):
    siliguridata = Siliguri.objects.all()

    data = {'title' : 'Travel India Info | Siliguri',
        "siliguridata" : siliguridata}
    return render(request, "West-Bengal/SILIGURI.html" , data)




# SOUTH places pages
def ANDHRAPRADESH(request):
    andhradata = AndhraPradesh.objects.all()

    data = {'title' : 'Travel India Info | Andhra Pradesh',
        "andhradata" : andhradata}
    return render(request, "Andhra-Pradesh/ANDHRAPRADESH.html" , data)


def ARAKUvalley(request):
    arakuvalleydata = ArakuValley.objects.all()

    data = {'title' : 'Travel India Info | Araku Valley',
        "arakuvalleydata" : arakuvalleydata}
    return render(request, "Andhra-Pradesh/ARAKUvalley.html" , data)

def VISAKHAPATNAM(request):
    visakhapatnamdata = Visakhapatnam.objects.all()

    data = {'title' : 'Travel India Info | Visakhapatnam',
        "visakhapatnamdata" : visakhapatnamdata}
    return render(request, "Andhra-Pradesh/VISAKHAPATNAM.html" , data)


def TIRUPATI(request):
    tirupatidata = Tirupati.objects.all()

    data = {'title' : 'Travel India Info | Tirupati',
        "tirupatidata" : tirupatidata}
    return render(request, "Andhra-Pradesh/TIRUPATI.html" , data)


def ANANTAPUR(request):
    anantapurdata = Anantapur.objects.all()

    data = {'title' : 'Travel India Info | Anantapur',
        "anantapurdata" : anantapurdata}
    return render(request, "Andhra-Pradesh/ANANTAPUR.html" , data)


def KURNOOL(request):
    kurnooldata = Kurnool.objects.all()

    data = {'title' : 'Travel India Info | Kurnool',
        "kurnooldata" : kurnooldata}
    return render(request, "Andhra-Pradesh/KURNOOL.html" , data)





def KARNATAKA(request):
    karnatakadata = Karnataka.objects.all()

    data = {'title' : 'Travel India Info | Karnataka',
        "karnatakadata" : karnatakadata}
    return render(request, "Karnataka/KARNATAKA.html" , data)


def COORG(request):
    coorgdata = Coorg.objects.all()

    data = {'title' : 'Travel India Info | Coorg',
        "coorgdata" : coorgdata}
    return render(request, "Karnataka/COORG.html" , data)


def BADAMI(request):
    badamidata = Badami.objects.all()

    data = {'title' : 'Travel India Info | Badami',
        "badamidata" : badamidata}
    return render(request, "Karnataka/BADAMI.html" , data)

def HAMPI(request):
    hampidata = Hampi.objects.all()

    data = {'title' : 'Travel India Info | Hampi',
        "hampidata" : hampidata}
    return render(request, "Karnataka/HAMPI.html" , data)




def KERALA(request):
    keraladata = Kerala.objects.all()

    data = {'title' : 'Travel India Info | Kerala',
        "keraladata" : keraladata}
    return render(request, "Kerala/KERALA.html" , data)


def MUNNAR(request):
    munnardata = Munnar.objects.all()

    data = {'title' : 'Travel India Info | Munnar',
        "munnardata" : munnardata}
    return render(request, "Kerala/MUNNAR.html" , data)

def KUMARAKOM(request):
    kumarakomdata = Kumarakom.objects.all()

    data = {'title' : 'Travel India Info | Kumarakom',
        "kumarakomdata" : kumarakomdata}
    return render(request, "Kerala/KUMARAKOM.html" , data)



def TAMILNADU(request):
    tamilnadudata = TamilNadu.objects.all()

    data = {'title' : 'Travel India Info | Tamil Nadu',
        "tamilnadudata" : tamilnadudata}
    return render(request, "Tamil-Nadu/TAMILNADU.html" , data)

def RAMESHWARAM(request):
    rameshwaramdata = Rameshwaram.objects.all()

    data = {'title' : 'Travel India Info | Rameshwaram',
        "rameshwaramdata" : rameshwaramdata}
    return render(request, "Tamil-Nadu/RAMESHWARAM.html" , data)

def YERCAUD(request):
    yercauddata = Yercaud.objects.all()

    data = {'title' : 'Travel India Info | Yercaud',
        "yercauddata" : yercauddata}
    return render(request, "Tamil-Nadu/YERCAUD.html" , data)

def KODAIKANAL(request):
    kodaikanaldata = Kodaikanal.objects.all()

    data = {'title' : 'Travel India Info | Kodaikanal',
        "kodaikanaldata" : kodaikanaldata}
    return render(request, "Tamil-Nadu/KODAIKANAL.html" , data)

def OOTY(request):
    ootydata = Ooty.objects.all()

    data = {'title' : 'Travel India Info | Ooty',
        "ootydata" : ootydata}
    return render(request, "Tamil-Nadu/OOTY.html" , data)

def CHENNAI(request):
    chennaidata = Chennai.objects.all()

    data = {'title' : 'Travel India Info | Chennai',
        "chennaidata" : chennaidata}
    return render(request, "Tamil-Nadu/CHENNAI.html" , data)





def TELANGANA(request):
    telanganadata = Telangana.objects.all()

    data = {'title' : 'Travel India Info | Telangana',
        "telanganadata" : telanganadata}
    return render(request, "Telangana/TELANGANA.html" , data)

def HYDERABAD(request):
    hyderabaddata = Hyderabad.objects.all()

    data = {'title' : 'Travel India Info | Hyderabad',
        "hyderabaddata" : hyderabaddata}
    return render(request, "Telangana/HYDERABAD.html" , data)

def WARANGAL(request):
    warangaldata = Warangal.objects.all()

    data = {'title' : 'Travel India Info | Warangal',
        "warangaldata" : warangaldata}
    return render(request, "Telangana/WARANGAL.html" , data)





# WEST places pages
def GUJARAT(request):
    gujaratdata = Gujarat.objects.all()

    data = {'title' : 'Travel India Info | Gujarat',
        "gujaratdata" : gujaratdata}
    return render(request, "Gujarat/GUJARAT.html" , data)


def AHMEDABAD(request):
    ahmedabaddata = Ahmedabad.objects.all()

    data = {'title' : 'Travel India Info | Ahmedabad',
        "ahmedabaddata" : ahmedabaddata}
    return render(request, "Gujarat/AHMEDABAD.html" , data)


def KUTCH(request):
    kutchdata = Kutch.objects.all()

    data = {'title' : 'Travel India Info | Kutch',
        "kutchdata" : kutchdata}
    return render(request, "Gujarat/KUTCH.html" , data)

def VADODARA(request):
    vadodaradata = Vadodara.objects.all()

    data = {'title' : 'Travel India Info | Vadodara',
        "vadodaradata" : vadodaradata}
    return render(request, "Gujarat/VADODARA.html" , data)



def HARYANA(request):
    haryanadata = Haryana.objects.all()

    data = {'title' : 'Travel India Info | Haryana',
        "haryanadata" : haryanadata}
    return render(request, "Haryana/HARYANA.html" , data)


def CHANDIGARH(request):
    chandigarhdata = Chandigarh.objects.all()

    data = {'title' : 'Travel India Info | Chandigarh',
        "chandigarhdata" : chandigarhdata}
    return render(request, "Haryana/CHANDIGARH.html" , data)




def RAJASTHAN(request):
    rajasthandata = Rajasthan.objects.all()

    data = {'title' : 'Travel India Info | Rajasthan',
        "rajasthandata" : rajasthandata}
    return render(request, "Rajasthan/RAJASTHAN.html" , data)


def JAIPUR(request):
    jaipurdata = Jaipur.objects.all()

    data = {'title' : 'Travel India Info | Jaipur',
        "jaipurdata" : jaipurdata}
    return render(request, "Rajasthan/JAIPUR.html" , data)


def UDAIPUR(request):
    udaipurdata = Udaipur.objects.all()

    data = {'title' : 'Travel India Info | Udaipur',
        "udaipurdata" : udaipurdata}
    return render(request, "Rajasthan/UDAIPUR.html" , data)


def JAISALMER(request):
    jaisalmerdata = Jaisalmer.objects.all()

    data = {'title' : 'Travel India Info | Jaisalmer',
        "jaisalmerdata" : jaisalmerdata}
    return render(request, "Rajasthan/JAISALMER.html" , data)


def JODHPUR(request):
    jodhpurdata = Jodhpur.objects.all()

    data = {'title' : 'Travel India Info | Jodhpur',
        "jodhpurdata" : jodhpurdata}
    return render(request, "Rajasthan/JODHPUR.html" , data)



def GOA(request):
    goadata = Goa.objects.all()

    data = {'title' : 'Travel India Info | Goa',
        "goadata" : goadata}
    return render(request, "Goa/GOA.html" , data)



def MAHARASHTRA(request):
    maharashtradata = Maharashtra.objects.all()

    data = {'title' : 'Travel India Info | Maharashtra',
        "maharashtradata" : maharashtradata}
    return render(request, "Maharashtra/MAHARASHTRA.html" , data)


def MAHABALESHWAR(request):
    mahabaleshwardata = Mahabaleshwar.objects.all()

    data = {'title' : 'Travel India Info | Mahabaleshwar',
        "mahabaleshwardata" : mahabaleshwardata}
    return render(request, "Maharashtra/MAHABALESHWAR.html" , data)


def MUMBAI(request):
    mumbaidata = Mumbai.objects.all()

    data = {'title' : 'Travel India Info | Mumbai',
        "mumbaidata" : mumbaidata}
    return render(request, "Maharashtra/MUMBAI.html" , data)


# Center pages
def NEWDelhi(request):
    newdelhidata = NewDelhi.objects.all()

    data = {'title' : 'Travel India Info | New Delhi',
        "newdelhidata" : newdelhidata}
    return render(request, "New-Delhi/NewDelhi.html" , data)
