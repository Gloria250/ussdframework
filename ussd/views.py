from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def  welcome(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='glorianiyonkuru7@gmail.com'
api_key ='56ae7384a0c2794b0580f2c189748b0add1ee3ffa46ca64d73d20c32513c6bc7'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):

    if request.method == 'POST':

        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST['text']
        level = text.split('*')
        category = text[:3]
        response =""
        #  main menu for our application
        if text == '':
            response =  "CON Welcome on agrivi platform \n"
            response += "1. report for crop updates \n"
            response += "2. reports on required equipments \n"
        elif text == '1':
            response = "CON report for crop updates \n"
            response += "1. sweet potatoes \n"
            response += "2. maize"
        elif text == '1*1':
            product="sweet potatoes"
            response = "CON report on sweet potatoes yeild "+str(product)+"\n"
        elif category =='1*1' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "CON input code\n"
        elif category =='1*1' and int(len(level)) == 4 and str(level[3]) in  str(level):
            response = "CON here is the report you requested for\n"
        elif category =='1*1' and int(len(level)) == 5 and str(level[4]) in  str(level):
            response = "END thank you for using our services\n"


        elif text == '1*2':
            product ="maize"
            response ="CON report on maize yeild "+str(product)+"\n"
        elif category =='1*2' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "CON input code\n"
        elif category =='1*2' and int(len(level)) == 4 and str(level[3]) in  str(level):
            response = "CON here is the report you requested \n"
        elif category =='1*2' and int(len(level)) == 5 and str(level[4]) in  str(level):
            response = "END thank you for using our services \n"
         
        #  ======================== required equipments==================
        elif text == '2':
            response = "CON here are the required equipments \n "
            response += "1. fertilizers needed \n"
            response += "2. tools needed \n"
        elif text == '2*1':
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe rimwe mukwezi"
        elif text == '2*2':
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe kabiri mukwezi"
        else:
            response = "END Ukanze ibitaribyo, ongera mukanya"
        return HttpResponse(response)
    else:
        return HttpResponse('we are on ussd app')