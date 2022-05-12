movies = {
    "favourite": ["A New Hope", "Empire Strikes Back", "Return of the Jedi",
                  "The Force Awakens", "Jaws", "Predator", "Mad Max",
                  "Back to the Future", "2001: A Space Odyssey", "Robocop",
                  "The Hitchhiker's Guide to the Galaxy", "Doctor Who",
                  "Aliens", "Alien", "Terminator", "Blade Runner", "Matrix"],

    "hated": ["The Phantom Menace", "Attack of the Clones", "Star Trek",
              "Alien Resurrection", "Twilight"]

}

# for key in movies.keys():
#     if "favourite" in key:
#         for value in movies.values():
#             if inserted_text in value:
#                 return f'''
#                                {HTML_GET.format(inserted_text=inserted_text)}
#                                <h2> Yes! You have right!!! I love: {inserted_text}</h2>
#                                '''
#     else:
#         return f'''
#                        {HTML_GET.format(inserted_text=inserted_text)}
#                        <h2>I hate!!!: {inserted_text}</h2>
#                        '''


# #  for value in movies.values():
# if "hated" in movies.keys() and inserted_text in movies.values():
#     return f'''
#                                       {HTML_GET.format(inserted_text=inserted_text)}
#                                       <h2>I hate!!!: {inserted_text}</h2>
#                                       '''
#
# #  for value in movies.values():
# if "favourite" in movies.keys() and inserted_text in movies.values():
#     return f'''
#                           {HTML_GET.format(inserted_text=inserted_text)}
#                           <h2> Yes! You have right!!! I love: {inserted_text}</h2>
#                           '''