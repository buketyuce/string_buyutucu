#Verilen string= "hi my name is Buket and i am learning python"
#Çıktı olarak almak istediğim= "Hi mY NaMe iS BuKeT AnD I Am lEaRnInG PyThOn"

#Bu çıktının alınması için girilen string'in çift indexleri büyütülmeli, tek indexleri ise küçük kalmalı.

def harf_buyutucu(string):
    yeni_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            yeni_string += string[i].upper()
        else:
            yeni_string += string[i].lower()

    print(yeni_string)

harf_buyutucu("hi my name is Buket and i am learning python"):









