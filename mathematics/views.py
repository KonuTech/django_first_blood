from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from mathematics.services import AlgebraService
# Create your views here.

from django.template.loader import render_to_string


def hello(request, name="World!"):
    rendered = render_to_string("mathematics/calculations.html", {})
    return HttpResponse(rendered)

def calculator(request: HttpRequest , operation: str, a: int, b: int) -> HttpResponse:
    
    try:
        result = AlgebraService.calculate(operation, a, b)
    except ValueError as e:
        return HttpResponse(f"{e}")
    except KeyError:
        return HttpResponse("Niepoprawna operacja")
    return HttpResponse(f"{result}")

