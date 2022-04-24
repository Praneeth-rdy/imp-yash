# Django Imports
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Standard Package Imports
import os
import json

# Project Imports
from .models import *
from image_processing import settings
from .app import process_img

# Third Party Imports
from django.template.loader import render_to_string


abpath = str(settings.BASE_DIR)


@csrf_exempt
def index(request):
    if request.method == 'POST':
        imgData = json.loads(request.body)
        # Process the imgData and pass the processedData to dara variable
        data = process_img(imgData)
        return JsonResponse({
            'processedData': data
        })
    else:
        return render(request, "index.html", {'data': 'Welcome!'})
