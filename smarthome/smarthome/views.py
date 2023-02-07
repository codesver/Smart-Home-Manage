from django.db.models import query
from django.db.models.fields import URLField
from django.shortcuts import render
from .models import *

# Create your views here.
homenumber = ''
resnumber = ''

# Starting Page
def start_view(request) :
    if request.method == 'POST':
        return render(request, 'smarthome/login.html')
    return render(request, 'smarthome/start.html')

# Join Page
def join_view(request) :
    if('ex' in request.POST) :
        rid = str(request.POST.get('rsn'))
        check = Resident.objects.filter(rsn = rid)
        print(rid)
        if not check :
            return render(request, 'smarthome/join.html', {'exist': True, 'rid': rid})
        else :
            return render(request, 'smarthome/join.html', {'exist': False})

    if('join' in request.POST) :
        rsn = request.POST.get('rsn')
        pw = request.POST.get('pw')
        hsn = request.POST.get('hsn')
        hsn = Home.objects.filter(hsn = hsn).first()
        rname = request.POST.get('rname')
        age = request.POST.get('age')
        authority = request.POST.get('authority')
        resident = Resident.objects.create(rsn=rsn, rname=rname, age=int(age), authority=int(authority), hsn=hsn, pw=pw)
        resident.save()
    return render(request, 'smarthome/join.html', {'exist': False})

# Login Page
def login_view(request) :
    global homenumber, resnumber
    if request.method == 'POST':
        hsn = request.POST.get('hsn')
        rsn = request.POST.get('rsn')
        pw = request.POST.get('pw')
        r = Resident.objects.filter(hsn = hsn, rsn = rsn, pw = pw)
        if not r :
            return render(request, 'smarthome/login.html', {'exist': False})
        else :
            homenumber = hsn
            resnumber = rsn
            return render(request, 'smarthome/login.html', {'exist': True})
    return render(request, 'smarthome/login.html')

# Main Page
def main_view(request) :
    return render(request, 'smarthome/main.html', {'test': homenumber})


# < Room Pages >
# Lining Room (Single)
def lrooms_view(request) :
    space = Space.objects.get(hsn = homenumber, ssn__startswith = 'LSGL')
    tvstate = IOT.objects.get(ssn = space.ssn, ikind = 'TV')
    acstate = IOT.objects.get(ssn = space.ssn, ikind = 'AC')
    lstate = IOT.objects.get(ssn = space.ssn, ikind = 'L')
    estate = Power.objects.get(ssn = space.ssn, pkind = 'E')
    if('TV' in request.POST) :
        tvstate.istate = not tvstate.istate
        tvstate.save()
    if('AC' in request.POST) :
        acstate.istate = not acstate.istate
        acstate.save()
    if('L' in request.POST) :
        lstate.istate = not lstate.istate
        lstate.save()
    if('E' in request.POST) :
        estate.pstate = not estate.pstate
        if(not estate.pstate) :
            tvstate.istate = 0
            acstate.istate = 0
            lstate.istate = 0
            tvstate.save()
            acstate.save()
            lstate.save()
        estate.save()
    return render(request, 'smarthome/lrooms.html', {'tvstate': tvstate.istate, 'acstate': acstate.istate, 'lstate': lstate.istate, 'estate': estate.pstate})

# Dining Room (Single)
def drooms_view(request) :
    space = Space.objects.get(hsn = homenumber, ssn__startswith = 'DSGL')
    acstate = IOT.objects.get(ssn = space.ssn, ikind = 'AC')
    lstate = IOT.objects.get(ssn = space.ssn, ikind = 'L')
    estate = Power.objects.get(ssn = space.ssn, pkind = 'E')
    wstate = Power.objects.get(ssn = space.ssn, pkind = 'W')
    gstate = Power.objects.get(ssn = space.ssn, pkind = 'G')
    if('AC' in request.POST) :
        acstate.istate = not acstate.istate
        acstate.save()
    if('L' in request.POST) :
        lstate.istate = not lstate.istate
        lstate.save()
    if('E' in request.POST) :
        estate.pstate = not estate.pstate
        if(not estate.pstate) :
            acstate.istate = 0
            lstate.istate = 0
            acstate.save()
            lstate.save()
        estate.save()
    if('W' in request.POST) :
        wstate.pstate = not wstate.pstate
        wstate.save()
    return render(request, 'smarthome/drooms.html', {'acstate': acstate.istate, 'lstate': lstate.istate, 'estate': estate.pstate, 'wstate': wstate.pstate, 'gstate': gstate.pstate})

# Private Room (A)
def prooma_view(request) :
    space = Space.objects.get(hsn = homenumber, ssn__startswith = 'PFST')
    acstate = IOT.objects.get(ssn = space.ssn, ikind = 'AC')
    lstate = IOT.objects.get(ssn = space.ssn, ikind = 'L')
    estate = Power.objects.get(ssn = space.ssn, pkind = 'E')
    if('AC' in request.POST) :
        acstate.istate = not acstate.istate
        acstate.save()
    if('L' in request.POST) :
        lstate.istate = not lstate.istate
        lstate.save()
    if('E' in request.POST) :
        estate.pstate = not estate.pstate
        if(not estate.pstate) :
            acstate.istate = 0
            lstate.istate = 0
            acstate.save()
            lstate.save()
        estate.save()
    return render(request, 'smarthome/prooma.html', {'acstate': acstate.istate, 'lstate': lstate.istate, 'estate': estate.pstate})

# Private Room (B)
def proomb_view(request) :
    space = Space.objects.get(hsn = homenumber, ssn__startswith = 'PSND')
    acstate = IOT.objects.get(ssn = space.ssn, ikind = 'AC')
    lstate = IOT.objects.get(ssn = space.ssn, ikind = 'L')
    estate = Power.objects.get(ssn = space.ssn, pkind = 'E')
    if('AC' in request.POST) :
        acstate.istate = not acstate.istate
        acstate.save()
    if('L' in request.POST) :
        lstate.istate = not lstate.istate
        lstate.save()
    if('E' in request.POST) :
        estate.pstate = not estate.pstate
        if(not estate.pstate) :
            acstate.istate = 0
            lstate.istate = 0
            acstate.save()
            lstate.save()
        estate.save()
    return render(request, 'smarthome/proomb.html', {'acstate': acstate.istate, 'lstate': lstate.istate, 'estate': estate.pstate})

# Bath Room (A)
def brooma_view(request) :
    space = Space.objects.get(hsn = homenumber, ssn__startswith = 'BFST')
    lstate = IOT.objects.get(ssn = space.ssn, ikind = 'L')
    estate = Power.objects.get(ssn = space.ssn, pkind = 'E')
    wstate = Power.objects.get(ssn = space.ssn, pkind = 'W')
    gstate = Power.objects.get(ssn = space.ssn, pkind = 'G')
    if('L' in request.POST) :
        lstate.istate = not lstate.istate
        lstate.save()
    if('E' in request.POST) :
        estate.pstate = not estate.pstate
        if(not estate.pstate) :
            lstate.istate = 0
            lstate.save()
        estate.save()
    if ('W' in request.POST) :
        wstate.pstate = not wstate.pstate
        wstate.save()
    if ('G' in request.POST) :
        gstate.pstate = not gstate.pstate
        gstate.save()
    return render(request, 'smarthome/brooma.html', {'lstate': lstate.istate, 'estate': estate.pstate, 'wstate': wstate.pstate, 'gstate': gstate.pstate})

# Bath Room (B)
def broomb_view(request) :
    space = Space.objects.get(hsn = homenumber, ssn__startswith = 'BSND')
    lstate = IOT.objects.get(ssn = space.ssn, ikind = 'L')
    estate = Power.objects.get(ssn = space.ssn, pkind = 'E')
    wstate = Power.objects.get(ssn = space.ssn, pkind = 'W')
    gstate = Power.objects.get(ssn = space.ssn, pkind = 'G')
    if('L' in request.POST) :
        lstate.istate = not lstate.istate
        lstate.save()
    if('E' in request.POST) :
        estate.pstate = not estate.pstate
        if(not estate.pstate) :
            lstate.istate = 0
            lstate.save()
        estate.save()
    if ('W' in request.POST) :
        wstate.pstate = not wstate.pstate
        wstate.save()
    if ('G' in request.POST) :
        gstate.pstate = not gstate.pstate
        gstate.save()
    return render(request, 'smarthome/broomb.html', {'lstate': lstate.istate, 'estate': estate.pstate, 'wstate': wstate.pstate, 'gstate': gstate.pstate})
    
# Veranda (A)
def vrooma_view(request) :
    space = Space.objects.get(hsn = homenumber, ssn__startswith = 'VFST')
    drystate = IOT.objects.get(ssn = space.ssn, ikind = 'DRY')
    wshstate = IOT.objects.get(ssn = space.ssn, ikind = 'WSH')
    lstate = IOT.objects.get(ssn = space.ssn, ikind = 'L')
    estate = Power.objects.get(ssn = space.ssn, pkind = 'E')
    wstate = Power.objects.get(ssn = space.ssn, pkind = 'W')
    gstate = Power.objects.get(ssn = space.ssn, pkind = 'G')
    if('L' in request.POST) :
        lstate.istate = not lstate.istate
        lstate.save()
    if('DRY' in request.POST) :
        drystate.istate = not drystate.istate
        drystate.save()
    if('WSH' in request.POST) :
        wshstate.istate = not wshstate.istate
        wshstate.save()
    if('E' in request.POST) :
        estate.pstate = not estate.pstate
        if(not estate.pstate) :
            lstate.istate = 0
            drystate.istate = 0
            wshstate.istate = 0
            lstate.save()
            drystate.save()
            wshstate.save()
        estate.save()
    if ('W' in request.POST) :
        wstate.pstate = not wstate.pstate
        wstate.save()
        if(not wstate.pstate) :
            wshstate.istate = 0 
            wshstate.save()
    if ('G' in request.POST) :
        gstate.pstate = not gstate.pstate
        gstate.save()
    return render(request, 'smarthome/vrooma.html', {'lstate': lstate.istate, 'drystate': drystate.istate, 'wshstate': wshstate.istate, 'estate': estate.pstate, 'wstate': wstate.pstate, 'gstate': gstate.pstate})

# Veranda (B)
def vroomb_view(request) :
    space = Space.objects.get(hsn = homenumber, ssn__startswith = 'VSND')
    drystate = IOT.objects.get(ssn = space.ssn, ikind = 'DRY')
    wshstate = IOT.objects.get(ssn = space.ssn, ikind = 'WSH')
    lstate = IOT.objects.get(ssn = space.ssn, ikind = 'L')
    estate = Power.objects.get(ssn = space.ssn, pkind = 'E')
    wstate = Power.objects.get(ssn = space.ssn, pkind = 'W')
    gstate = Power.objects.get(ssn = space.ssn, pkind = 'G')
    if('L' in request.POST) :
        lstate.istate = not lstate.istate
        lstate.save()
    if('DRY' in request.POST) :
        drystate.istate = not drystate.istate
        drystate.save()
    if('WSH' in request.POST) :
        wshstate.istate = not wshstate.istate
        wshstate.save()
    if('E' in request.POST) :
        estate.pstate = not estate.pstate
        if(not estate.pstate) :
            lstate.istate = 0
            drystate.istate = 0
            wshstate.istate = 0
            lstate.save()
            drystate.save()
            wshstate.save()
        estate.save()
    if ('W' in request.POST) :
        wstate.pstate = not wstate.pstate
        wstate.save()
        if(not wstate.pstate) :
            wshstate.istate = 0 
            wshstate.save()
    if ('G' in request.POST) :
        gstate.pstate = not gstate.pstate
        gstate.save()
    return render(request, 'smarthome/vroomb.html', {'lstate': lstate.istate, 'drystate': drystate.istate, 'wshstate': wshstate.istate, 'estate': estate.pstate, 'wstate': wstate.pstate, 'gstate': gstate.pstate})

# Hallway
def hllwys_view(request) :
    space = Space.objects.get(hsn = homenumber, ssn__startswith = 'HSGL')
    lstate = IOT.objects.get(ssn = space.ssn, ikind = 'L')
    estate = Power.objects.get(ssn = space.ssn, pkind = 'E')
    if('L' in request.POST) :
        lstate.istate = not lstate.istate
        lstate.save()
    if('E' in request.POST) :
        estate.pstate = not estate.pstate
        if(not estate.pstate) :
            lstate.istate = 0
            lstate.save()
        estate.save()
    return render(request, 'smarthome/hllwys.html', {'lstate': lstate.istate, 'estate': estate.pstate})