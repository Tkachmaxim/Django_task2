import operator
from random import sample
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseServerError
from tours import data


def main_view(request):
    random_hotel = dict(sample(data.tours.items(), 6))
    main_info = {}
    main_info['departures'] = data.departures
    main_info['hotels'] = random_hotel
    return render(request, 'index.html', context={'main_info': main_info})


def departure_view(request, departure):
    direction_template = {}
    choose_direction = {}

    for id, tour in data.tours.items():
        if tour['departure'] == departure:
            choose_direction[id] = tour

    direction_template['tours'] = choose_direction
    maxprice = sorted(choose_direction.values(), key=operator.itemgetter('price'), reverse=True)[0]['price']
    minprice = sorted(choose_direction.values(), key=operator.itemgetter('price'), reverse=False)[0]['price']
    maxnights = sorted(choose_direction.values(), key=operator.itemgetter('nights'), reverse=True)[0]['nights']
    minnights = sorted(choose_direction.values(), key=operator.itemgetter('nights'), reverse=False)[0]['nights']
    direction_template['maxprice'] = maxprice
    direction_template['minprice'] = minprice
    direction_template['maxnights'] = maxnights
    direction_template['minnights'] = minnights
    direction_template['len'] = len(choose_direction)
    direction_template['dep'] = data.departures
    direction_template['rus_departure'] = data.departures[departure]
    return render(request, 'departure.html', direction_template)


def tour_view(request, id):
    info = data.tours[id]
    info['rus_departure'] = data.departures[data.tours[id]['departure']]
    info['dep'] = data.departures
    return render(request, 'tour.html', info)


def c_handler400(request, exception):
    return HttpResponseBadRequest('Error 400')


def c_handler500(request):
    return HttpResponseServerError('Server error')
