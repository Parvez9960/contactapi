# from django.shortcuts import render

# # Create your views here.


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact

@csrf_exempt
def create_contact(request):
    if request.method == "POST":
        data = json.loads(request.body)
        contact = Contact.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone")
        )
        return JsonResponse({
            "message": "Contact created successfully",
            "contact": {
                "name": contact.name,
                "email": contact.email,
                "phone": contact.phone
            }
        }, status=201)
    return JsonResponse({"error": "Invalid request"}, status=400)

def health_check(request):
    return JsonResponse({"status": "ok"})
