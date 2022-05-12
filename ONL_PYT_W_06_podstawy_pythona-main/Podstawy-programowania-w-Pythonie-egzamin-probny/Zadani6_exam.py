# Zapoznaj się z modułem exam umieszczonym w pliku dołączonym do tego egzaminu. W tym module znajduje się słownik movies, w którym można znaleźć listę ulubionych i znienawidzonych filmów pewnego programisty.
#
# Używając Flaska, utwórz stronę, którą udostępnisz pod adresem /movies:
#
#     jeśli użytkownik wejdzie na stronę metodą GET, wyświetl formularz, który:
#         będzie miał pole tekstowe o nazwie title,
#         opisem pola będzie: "Insert title",
#
#     jeśli użytkownik wejdzie na stronę metodą POST:
#         sprawdź, czy film znajduje się na liście ulubionych filmów, jeśli tak, zwróć tekst "favourite",
#         sprawdź, czy film znajduje się na liście znienawidzonych filmów, jeśli tak, zwróć tekst "hated",
#         jeśli nie znajduje się na żadnej liście, zwróć tekst "no such movie!".
#
# Ważne: Powołując aplikację Flaska, użyj zmiennej app!

from flask import Flask, request
from exam import movies


app = Flask(__name__)


HTML_GET='''
<!DOCTYPE html>
    <html lang="en"> 

    <head>
    <meta charset="UTF-8">
    <title>FAVORITE & HATED FILMS</title>
    </head>
        <body>
        
        <h3>LOVED & HATED FILMS BY ME:</h3>
        
            <form  action = "" method = "POST">
            Insert name of film: <input type="text" name="inserted_text" ><br>
            <input type="submit" value="Check film name">
            </form >
        
            
        </body>
    </html>

'''


HTML_POST='''

'''






@app.route("/movies/", methods=("GET", "POST"))

def movies_view():
    if request.method == "GET":
        return HTML_GET

    if request.method == "POST":
#favourite

        inserted_text = str(request.form.get("inserted_text"))
#        favourite = []
        values = []






        if inserted_text in movies["favourite"]:
                    return f'''
                                            {HTML_GET.format(inserted_text=inserted_text)}
                                            <h2>I love: {inserted_text}</h2>
                                            '''
        elif inserted_text in movies["hated"]:
                    return f'''
                                            {HTML_GET.format(inserted_text=inserted_text)}
                                            <h2>I hate: {inserted_text}</h2>
                                            '''
        else:
            return f'''
                                                {HTML_GET}
                                                <h2>NO FILM IN DICTIONARY</h2>
                                                '''
        # if "favourite" in movies.keys():
        #     for value in movies.values():
        #         if inserted_text in value:
        #
        #
        #             return f'''
        #                         {HTML_GET.format(inserted_text=inserted_text)}
        #                         <h2> Yes! You have right!!! I love: {inserted_text}</h2>
        #                         '''






        #for inserted_text in movies.keys():
        #        favourite.append(value)


        #if inserted_text in movies:





if __name__ == '__main__':
    app.run(debug=True, port=5001)



