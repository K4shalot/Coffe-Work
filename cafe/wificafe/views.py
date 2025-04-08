from django.shortcuts import render, redirect, get_object_or_404
import os
from dotenv import load_dotenv
from django.conf import settings
from .models import CafeBlock

load_dotenv()

def cafes_list(request):
    cafes = CafeBlock.objects.all()
    return render(request, 'mainpage.html',{'cafes': cafes})

def cafe_detail(request, cafe_id):
    cafe = get_object_or_404(CafeBlock, id=cafe_id)
    return render(request, 'cafe_detail.html', {'cafe': cafe})
