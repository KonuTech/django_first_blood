## Cwiczenie - urls
W oparciu o urls.py i views.py z mathematics dodaj implementacje w ktore dla funkcji matematycznych i ich argumentow zwracany bedzie odpowiedni wynik
add, sub, div, mul

po wejsciu na adres http://127.0.0.1:8000/mathematics/add/1/2
3

/mathematics/sub/1/2
-1

/mathematics/mul/10/2
20


## cwiczenie 2 - widok listy postow

po wejsciu na ten adres
 http://127.0.0.1:8000/blog/posts

chce miec wypisane tytuly postow ktore beda jednoczesnie linkami

1. trzeba utworzyc nowa aplikacje (blog)
2. utworz serwis BlogService - z metodą list (na razie zwraca wymyślona liste tytulow postow)
3. w nowej aplikacji trzeba utworzyc szablon, ktory wypisze te tytuly w formie listy odnosnikow
4. analogicznie do mathematics - zadbać o url, stworzyc odpowiednia funkcje widoku

/blog/posts/<id> (liczone od 1)


# cwiczenie 

Projekt: bp_monitor
aplikacja: measurements
urls, widok, service, faker -wykorzystaj do pokazania listy fakeowych pomiarow cisnienia

data: datetime
systolic: int (60-250)
diastolic: int (30-180)

rozwiazanie przeslac jako link do platformy github