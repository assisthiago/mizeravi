from django.db.models import Q

def build_lookup(request, model_name):
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
