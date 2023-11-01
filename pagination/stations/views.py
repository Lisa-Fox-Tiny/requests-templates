from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


with open(settings.BUS_STATION_CSV, encoding = 'utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    bus_stations_list = []
    for row in reader:
        bus_stations_list.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})


def bus_stations(request):
    count = 10
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations_list, count)

    page = paginator.get_page(page_num)
    data = page.object_list
    context = {
            'bus_stations': data,
            'page': page,
    }

    return render(request, 'stations/index.html', context)