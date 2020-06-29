from django.db.models import Q

def build_search_lookups(request):
    value = request.GET.get('search')
    return Q(name__icontains=value)

def build_filters_lookups(request, model_name):
    if request.GET.getlist('plataforms'):
        plataforms = request.GET.getlist('plataforms')
        plataforms_lookup = Q(plataforms__contains=plataforms)
    else:
        plataforms_lookup = Q(plataforms__isnull=False)

    if request.GET.get('price'):
        gte, lte = request.GET.get('price').split('_')
        gte = '{}.00'.format(gte)
        lte = '{}.99'.format(lte)
        price_lookup = Q(price__gte=gte, price__lte=lte)
    else:
        price_lookup = Q(price__isnull=False)

    return (plataforms_lookup, price_lookup)

def check_which_filter_is_selected(request):
    if request.GET.getlist('plataforms'):
        plataforms = request.GET.getlist('plataforms')
        plataforms_filters = [p.lower().replace(' ', '-') for p in plataforms]
    else:
        plataforms_filters = []

    if request.GET.get('price'):
        price_filter = request.GET.get('price')
    else:
        price_filter = ''

    return (plataforms_filters, price_filter)
