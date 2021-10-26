from django.conf import settings


def context(request):
    debug = settings.DEBUG
    return{'debug_flag': debug}
