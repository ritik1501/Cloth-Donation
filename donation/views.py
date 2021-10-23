from django.http.response import HttpResponse
from django.shortcuts import render
from utils.states import states_list
from django.views import View

# Create your views here.
def home(request):
    return render(request, 'home.html', context={"states":states_list})


class AddClothes(View):

    def get(self, request):
         return HttpResponse("Error!!!")

    def post(self, request):
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip = request.POST["zip"]
        noClothes = request.POST["noClothes"]
        typeCloth = request.POST.getlist("typeCloth")
        gender = request.POST["gender"]

        return HttpResponse(f"{name}, {email}, {phone}, {city}, {state}, {zip}, {noClothes}, {typeCloth}, {gender}")

def contact(request):
    return render(request, 'contact.html')