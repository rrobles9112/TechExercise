from test import exportable_function


def hola():
    pass


print(exportable_function())

print(exportable_function().__doc__)