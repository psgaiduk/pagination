import csv
from urllib.parse import urlencode

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

all_bus_station = []

with open(settings.BUS_STATION_CSV, newline='') as csvfile:
    all_stations = csv.DictReader(csvfile)
    for station in all_stations:
        all_bus_station.append(station)


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):

    paginator = Paginator(all_bus_station, 10)
    current_page = request.GET.get('page', 1)
    bus_station = paginator.get_page(current_page)
    prev_page, next_page = None, None
    text = '?page'
    if bus_station.has_previous():
        prev_page = bus_station.number - 1
        prev_page = urlencode(query={text: prev_page}, safe='?')
    if bus_station.has_next():
        next_page = bus_station.number + 1
        next_page = urlencode(query={text: next_page}, safe='?')

    return render(request, 'index.html', context={
        'bus_stations': bus_station,
        'current_page': bus_station.number,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
    })

