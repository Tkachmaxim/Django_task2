from tours import data


def menu(request):
    return ({'departures': data.departures, 'tours': data.tours})
