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


#img process imports
from imageio import imread
import io
import base64
import numpy as np
import cv2

abpath = str(settings.BASE_DIR)

@csrf_exempt
def index(request):
    if request.method == 'POST':
        imgData = request.body.decode('utf-8')
        #imgBytes = bytes(imgData[25:-1], 'utf-8')
        b64ImgString = imgData.split('base64,')[1][:-1] 

        with open('./main/dataset/test.jpeg', 'wb') as fh:
            fh.write(base64.b64decode(b64ImgString.encode('UTF-8'))) 
        # Process the imgData and pass the processedData to dara variable
        data = process_img('./main/dataset/test.jpeg')
        data = {} 
        return JsonResponse({
            'processedData': data
        })
    else:
        return render(request, "index.html", {'data': 'Welcome!'})
