from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html');

def eq(request):

    LN	= float(request.GET['LN'])
    d	= float(request.GET['d'])
    dF	= float(request.GET['dF'])
    dR	= float(request.GET['dR'])
    LT	= float(request.GET['LT'])
    XP	= float(request.GET['XP'])
    CR	= float(request.GET['CR'])
    CT	= float(request.GET['CT'])
    S	= float(request.GET['S'])
    LF	= float(request.GET['LF'])
    R	= float(request.GET['R'])
    XR	= float(request.GET['XR'])
    XB	= float(request.GET['XB'])
    N   = float(request.GET['N'])

    CNN = 2
    XN = 0.666*LN

    CNT = 2 * (((dR/d)**2)-((dF/d)**2))

    XT = XP + (LT/3)*(1+((1-(dF/dR))/(1-((dF/dR)**2))))

    CNF = (1 + R/(S+R))*((4*N*((S/d)**2))/(1 + (1+((2*LF)/(CR+CT))**2)**0.5))

    XF = XB + (XR/3)*((CR+2*CT)/(CR+CT))+(1/6)*((CR+CT)- ((CR*CT)/(CR+CT)))
    
    CNR = CNN + CNT + CNF

    X = ((CNN*XN)+(CNT*XT)+ (CNF*XF))/CNR

    return render(request,'result.html',{'result':X});