# CeneoScraper

## Struktura opinii w serwisie [Ceneo.pl] (https://www.ceneo.pl/)

|Składowa opinii|Selektor|Nazwa zmiennej|Typ danych|
|---------------|--------|--------------|----------|
|opinia|div.js_product-review|opinion||
|identyfikator opinii|div.js_product-review\["data-entry-id\]|opinion_id||
|autor opinii|span.user-post__author-name|author||
|rekomendacja autora|span.user-post__author-recomendation > em|recomendation||
|liczba gwiazdek|span.user-post__score-count|stars||
|treść opinii|div.user-post__text|content||
|lista zalet|div[class$=positives] ~ div.review-feature__item|pros||
|lista wad|div[class$=negatives] ~ div.review-feature__item|cons||
|dla ilu osób przydatna|button.vote-yes > span|useful||
|dla ilu osób nieprzydatna|button.vote-no > span|useless||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)\["datetime"\]|published||
|data zakupu produktu|span.user-post__published > time:nth-child(2)\["datetime"\]|purchased||

# Etapy pracy nad projektem
1. Pobranie elementów pojedynczej opinii do niezależnych zmiennych.
2. Zapisanie wszystkich elementów pojedynczej opinii do jednej zmiennej \(słownik\).
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i dodanie ich do listy.
4. Zapisanie wszystkich opinii o produkcie z wszystkich stron i zapisanie ich do pliku.
5. Dodanie możliwości podania id produktu przez użytkownika za pomocą klawiatury
6. Refaktoryzacja \(optymalizacja\) kodu:
    a. utworzenie funkcji do do pobierania składowych strony HTML 
    b. utworzenie słownika opisującego strukturę opinii wraz z selektorami poszczególnych elementów
    c. zamiana instrukcji pobierających składowe opinii do pojedynczych zmiennych i tworzących z nich słownik na 
    wyrażenie słownikowe \(dictionary comprehension\) tworzące słownik reprezentujący pojedynczą opinię na
    podstawie słownika selektorów
7. Analiza opinii o wybranym produkcie
    1. wczytanie wszystkich opinii o wskazanym produkcie do obiektu DataFrame
    2. wyliczenie podstawowych statystyk na podstawie opinii
        1. liczba wszystkich opinii o produkcie
        2. liczba opinii w których autor podał listę zalet produktu
        3. liczba opinii w których autor podał listę wad produktu
    3. przygotowanie wykresów na podstawie zawartości opinii
        1. udział poszczególnych rekomendacji w ogólnej liczbie opinii
        2. histogram występowania poszczególnych ocen