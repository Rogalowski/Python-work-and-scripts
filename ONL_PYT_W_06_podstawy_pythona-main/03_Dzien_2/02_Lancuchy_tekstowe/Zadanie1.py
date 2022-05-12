# def message(input_dict, movie=None):
#     print("In movie, name is a role.")
#     keys = {"movie", "name", "role"}
#    # input_dict = {"movie":, "name":, "role:"}
#     if set(input_dict.keys()) == keys:
#         return f"In {input_dict['movie']}, {input_dict['name']} is a {input_dict['role']}."
#     else:
#         return None
#
#   #  print(f"In {movie}, {name} is a {role}.")
#
#
#
#     input_dict = {
#         "name": "Han Solo",
#         "role": "smuggler",
#         "movie": "Star Wars"
#     }
#     print(message(input_dict))

#----------------------------------------------------------------------

def message(actor):
    # if "name" not in actor:
    #     return None
    # if "role" not in actor:
    #     return None
    # if "movie" not in actor:
    #     return None

    # for key in ("name", "role", "movie"):
    #     if key not in actor:
    #         return None

    if set(actor.keys()) != {"name", "role", "movie"}:
        return None

    return "In %(movie)s, %(name)s is a %(role)s." % actor

input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

# In Star Wars, Han Solo is a smuggler.
print(message(input_dict))

input_dict = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

# None
print(message(input_dict))