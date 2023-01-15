"""
LAB - Zagnieżdżanie pętli i to samo w postaci jednolinijkowej
Postanawiasz otworzyć linie lotnicze "Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:
    ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
             'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
1. Zbuduj listę tupletów symbolizujących port początkowy i końcowy. Wykonaj połączenie każdy-z-każdym
2. Wyeliminuj z powyższej listy połączenie z portu do tego samego portu
3. Ponieważ połączenie z A do B dubluje się z połączeniem z B do A - wygeneruj możliwe połączenia krajowe pomijając takie zdublowane trasy.
4. Policz ilość generowanych połączeń w krokach 1,2,3
"""

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = [(start, stop) for start in ports for stop in ports]
print(routes)
print(len(routes))

routes = [(start, stop) for start in ports for stop in ports if start != stop]
print(routes)
print(len(routes))

routes = [(start, stop) for start in ports for stop in ports if start < stop]
print(routes)
print(len(routes))