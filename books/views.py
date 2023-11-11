from django.shortcuts import render
from dataclasses import dataclass
# Create your views here.

@dataclass
class Book:
    id: int
    title: str
    description: str

def books_list(request):
    books = [
        Book(1, "Pan Tadeusz", "Ala ma kota"), 
        Book(2, "Krzyzacy", "Lubie biegac")
    ]

    return render(
        request=request, 
        template_name="books/list.html",
        context={"books":books}
    )

def book_details(request, id):
    pass