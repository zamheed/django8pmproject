from django.shortcuts import render
from .models import State
from .models import City


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
    states = ["Select"]
    for x in res:
        states.append(x["name"])

    return render(request, "index.html", {"type": type,"states":states})


def getCityFromState(request):
    sel_state = request.GET.get("state")
    res = State.objects.values('idno').filter(name=sel_state)

    #res = City.objects.filter(state_name=sel_state)
    print(res)
    return None