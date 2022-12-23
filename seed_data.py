from ejemplo.models import Familiar
#Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
#Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
#Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
#Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
#print("Se cargo con éxito los usuarios de pruebas")

from ejemplo.models import Mascotas
Mascotas(nombre="Teddy", color="marron", edad=3).save()
Mascotas(nombre="Zeus", color="negro", edad=2).save()

print("Se cargo con éxito los usuarios de pruebas")

from ejemplo.models import Vehiculos
Vehiculos(modelo="207", marca="Ford", año=2018).save()
Vehiculos(modelo="Duna", marca="Fiat", año=1999).save()

print("Se cargo con éxito los usuarios de pruebas")