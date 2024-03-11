from django.shortcuts import render
from urllib.parse import unquote_plus
from django.shortcuts import redirect
from django.http import JsonResponse


# Create your views here.
def testview(request):
    values = ""
    for key, value in request.GET.items():
        value = unquote_plus(value)
        values = values + value
    from testapp.models import TestModel
    obj = TestModel.objects.create(value=value)
    return JsonResponse({'OK':'SUCCESS'})