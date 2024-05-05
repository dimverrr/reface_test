
from django.http import JsonResponse
import logging
from django.shortcuts import render

class ExceptionHandling500ErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 500:
            logging.error('Internal Server Error')
            return render(request, "500error.html", status=500)

        return response
    
class ExceptionHandling404ErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 404:
            logging.error('Not found')
            return render(request, "404error.html", status=404)

        return response

class ExceptionHandling403ErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 403:
            logging.error('Permission denied')
            return render(request, "403error.html", status=403)

        return response
    