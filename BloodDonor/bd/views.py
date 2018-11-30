from django.shortcuts import render
from .models import State
from .models import City
from .models import DonorRegister

def openDonorLogin(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})


def openHomePage(request):
    type = "home"
    return render(request,"index.html",{"type":type})


def openOrganizationLogin(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})


def openDonorRegister(request):
    type = request.GET.get("type")
    res = State.objects.values('name')
    states = ["State"]
    for x in res:
        states.append(x["name"])

    return render(request, "index.html", {"type": type,"states":states})


def getCityFromState(request):
    sel_state = request.GET.get("state")
    res = State.objects.values('idno').filter(name=sel_state)
    idno = 0
    for x in res:
        idno = x["idno"]
    res1 = City.objects.values('city_name').filter(state_name=idno)
    city_names = ["City"]
    if not res1:
        city_names = ["No City Available"]
    else:
        for x in res1:
            city_names.append(x['city_name'])

    res2 = State.objects.values('name')
    states = ["State"]
    for x in res2:
        states.append(x["name"])

    return render(request, "index.html", {"type": 'h_donor_register',"city_names":city_names,"states":sel_state,"key":"one"})


def registerDonor(request):
    d_name = request.POST.get('d_name')
    d_cno = request.POST.get('d_cno')
    d_state = request.POST.get('d_state')
    d_city = request.POST.get('d_city')
    d_email = request.POST.get('d_email')
    d_pass = request.POST.get('d_pass')

    print(d_name,d_cno,d_state,d_city,d_email,d_pass)

    # res = City.objects.values('idno').filter(city_name=d_city)
    #     # idno = 0
    #     # for x in res:
    #     #     idno = x["idno"]

    dr = DonorRegister(name=d_name,contact_no=d_cno,city_name=d_city,email_id=d_email,password=d_pass)
    dr.save()
    return render(request,"index.html",{"type":'h_donor',"message":"Registred"})