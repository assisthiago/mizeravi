from django.db.models import Q

def build_search_lookups(request):
    value = request.GET.get('search')
    return Q(name__contains=value) | Q(plataforms__contains=value)

def build_filters_lookups(request, model_name):
    if model_name == 'games':
        if request.GET.getlist('plataforms'):
            plataforms = request.GET.getlist('plataforms')
            plataform_lookup = Q(plataforms__contains=plataforms)
        else:
            plataform_lookup = Q(plataforms__isnull=False)
    else:
        if request.GET.get('plataforms'):
            plataforms = request.GET.get('plataforms')
            plataform_lookup = Q(plataform=plataforms)
        else:
            plataform_lookup = Q(plataform__isnull=False)

    if request.GET.get('price'):
        gte, lte = request.GET.get('price').split('_')
        gte = '{}.00'.format(gte)
        lte = '{}.99'.format(lte)
        price_lookup = Q(price__gte=gte, price__lte=lte)
    else:
        price_lookup = Q(price__isnull=False)

    return (plataform_lookup, price_lookup)

def check_which_filter_is_selected(request):
    if request.GET.getlist('plataforms'):
        plataforms = request.GET.getlist('plataforms')
        plataforms_filters = [p.lower().replace(' ', '-') for p in plataforms]
    elif request.GET.get('plataforms'):
        plataforms = request.GET.get('plataforms')
        plataforms_filters = [p.lower().replace(' ', '-') for p in plataforms]
    else:
        plataforms_filters = []

    if request.GET.get('price'):
        price_filter = request.GET.get('price')
    else:
        price_filter = ''

    return (plataforms_filters, price_filter)
