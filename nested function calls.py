# nested functions calls = function calls inside other function calls
#                          innermost function calls are resolved first
#                          returned value is used as argument for the next outer function

#example

#num = input("Dodaj pasa moj neki brojcic")
#num = float(num)
#num = abs(num)
#num = round(num)



print(round(abs(float(input("Dodaj neki broj")))))
