documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

def people():

  num = input(">")
  for doc in documents:
    if doc['number'] == num:
      print(doc['name'])
    else:
      print('Not ->',doc['name'])

def list_doc():
  for doc in documents:
    print("Passpotr №: " + doc['number']+'\n'+"Name: " + doc['name']+'\n')

list_doc()
people()