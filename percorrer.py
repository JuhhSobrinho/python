lista = [' ', 'a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v']

palavraKey = 'Ola Mundo'
result = '';
item_Uper = ''

for itemKey in palavraKey:

    for itemLista in lista: 
       item_Uper = itemLista.upper()
       
       if itemKey == itemLista:
            result += itemLista;
            print(result)
       elif itemKey == item_Uper:
            result += item_Uper;
            print(result)