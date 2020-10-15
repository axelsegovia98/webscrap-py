import requests
from bs4 import BeautifulSoup

#Request a la web de la que vamos a obtener datos.

url = 'https://www.netflix.com/ar/title/70143836'
raw_data = requests.get(url)
data = BeautifulSoup(raw_data.content, 'html.parser')

#Lista que va a contener los datos que buscamos.
scrap = list() 

#Clases del HTML de la web que identifican los datos que buscamos.
clases = (  'title-title', 
            'item-year', 
            'item-maturity', 
            'duration', 
            'item-genre', 
            'title-info-synopsis', 
            'title-data-info-item-list', 
            'hook-text'
            ) 

#Ciclo for que va a recorrer la lista clases. Esta va a ser usada para cambiar el dato buscado.
for i in clases:  
    #Variable que va a contener la parte del HTML que contiene uno de los datos.
    #Como mencioné antes, se utiliza la variable i declarada en el ciclo for para iterar el dato
    #que se busca por clase.
    info = data.find_all(class_= i) 
    #Ciclo for que extrae sólo el texto (o dato) del HTML.
    for e in info:
        scrap.append(e.text)
#Se imprime la lista completa con los datos esperados.
print(scrap)



#Se busca obtener la lista total de capítulos de la serie.

#Lista que va a contener los datos que buscamos.
listacaps = list() 

#Se busca en todo el HTML las etiquetas h3 que tengan la clase 'episode-title' y se guarda en la variable caps.
caps = data.find_all('h3', class_='episode-title')

#Ciclo for que va a recorrer la lista caps. Esta va a ser usada para dejar sólo el dato sin rastro de HTML.
for i in caps:
    listacaps.append(i.text)

#Variable que va a guardar la lista total de capítulos.
totalcaps = len(listacaps)   

#Se imprimen la listas completa con los datos esperados.
print(listacaps)
print(totalcaps)



#Hola Joel, muchas gracias por la ayuda. La verdad me sirvió muchísimo y en esta horita le metí a full y aprendí un poco.
#Sé que es código está sobrecomentado pero quería que se entienda que buscaba hacer en cada paso.
#Me gustaría, si es posible, un feedback sobre en qué aspectos se puede mejorar o si hace falta algo.
#Sueno repetitivo pero no está de más decirlo, gracias!
