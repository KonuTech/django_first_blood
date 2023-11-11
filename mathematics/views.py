from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from mathematics.services import AlgebraService
# Create your views here.

from django.template.loader import render_to_string


# def hello(request, name="World!"):
#     rendered = render_to_string("mathematics/calculations.html", {"text": f"Hello {name}"})
#     return HttpResponse(rendered)

# def hello(request, name="World!"):
#     return render(
#         request, 
#         "mathematics/calculations.html",
#          {"text": f"Hello {name}"}
#     )


def hello(request, name="World!"):
    return render(
        request=request, 
        template_name="mathematics/calculations.html",
        context={
            "text": f"Hello {name}",
            "text2": "Ala ma kota",  
            "lista": [10, 2, "a", "b"],
            "tupla": ("x", "y", 100),
            "zbior": {1, 2, 3},
            "slownik": {"klucz": "wartosc"}
        }
    )


def calculator(request: HttpRequest , operation: str, a: int, b: int) -> HttpResponse:
    
    try:
        result = AlgebraService.calculate(operation, a, b)
    except ValueError as e:
        return HttpResponse(f"{e}")
    except KeyError:
        return HttpResponse("Niepoprawna operacja")
    return HttpResponse(f"{result}")

