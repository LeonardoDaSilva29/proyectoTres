from django.shortcuts import render, get_object_or_404 # <----- Nuevo import
from django.shortcuts import render
from ejemplo.models import Familiar, Mascotas, Vehiculos
from ejemplo.forms import Buscar, FamiliarForm, MascotaForm, VehiculoForm  # <--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT 

# Create your views here.
def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre):
    return render (request, 'ejemplo/saludar_a.html',
    {"nombre": nombre}
    )

def sumar(request, a, b):
    return render(request, 'ejemplo/sumar.html', 
    {"a": a,
    "b": b,
    "resultado": a + b
    }
    )

def buscar(request):
    lista_de_nombre = ["leonardo", "natalia", "santiago", "olga", "antonio"]
    query = request.GET ['q']
    if query in lista_de_nombre:
        indice_del_resultado = lista_de_nombre.index(query)
        resultado = lista_de_nombre[indice_del_resultado]
    else:
        resultado = "No hay concidencia con lo buscado"
    return render(request, 'ejemplo/buscar.html', {"resultado": resultado})

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render (request, "ejemplo/familiares.html",  {"lista_familiares": lista_familiares})

def mostrar_mascotas(request):
    lista_mascotas = Mascotas.objects.all()
    return render (request, "ejemplo/mascotas.html",  {"lista_mascotas": lista_mascotas})

def mostrar_vehiculos(request):
    lista_vehiculos = Vehiculos.objects.all()
    return render (request, "ejemplo/vehiculo.html",  {"lista_vehiculos": lista_vehiculos})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarFamiliar(View):
  template_name = 'ejemplo/familiares.html'

  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiares})

class BuscarMascota(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_mascotas.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_mascotas = Mascotas.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_mascotas':lista_mascotas})
        return render(request, self.template_name, {"form": form})

class AltaMascotas(View):

    form_class = MascotaForm
    template_name = 'ejemplo/alta_mascotas.html'
    initial = {"nombre":"", "edad":"", "color":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la mascota {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarMascotas(View):
  form_class = MascotaForm
  template_name = 'ejemplo/actualizar_mascotas.html'
  initial = {"nombre":"", "edad":"", "color":""}
  

  def get(self, request, pk): 
      mascota = get_object_or_404(Mascotas, pk=pk)
      form = self.form_class(instance=mascota)
      return render(request, self.template_name, {'form':form,'mascota': mascota})


  def post(self, request, pk): 
      mascota = get_object_or_404(Mascotas, pk=pk)
      form = self.form_class(request.POST ,instance=mascota)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito la mascota {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'mascota': mascota,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarMascotas(View):
  template_name = 'ejemplo/mascotas.html'

  

  def get(self, request, pk): 
      mascota = get_object_or_404(Mascotas, pk=pk)
      mascota.delete()
      mascotas = Mascotas.objects.all()
      return render(request, self.template_name, {'lista_mascotas': mascotas})





class BuscarVehiculo(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_vehiculo.html'
    initial = {"modelo":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            modelo = form.cleaned_data.get("modelo")
            lista_vehiculos = Vehiculos.objects.filter(nombre__icontains=modelo).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_vehiculos':lista_vehiculos})
        return render(request, self.template_name, {"form": form})

class AltaVehiculos (View):

    form_class = VehiculoForm
    template_name = 'ejemplo/alta_vehiculos.html'
    initial = {"modelo":"", "marca":"", "año":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el nuevo vehiculo {form.cleaned_data.get('modelo')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarVehiculos(View):
  form_class = VehiculoForm
  template_name = 'ejemplo/actualizar_vehiculos.html'
  initial = {"marca":"", "modelo":"", "año":""}
  

  def get(self, request, pk): 
      vehiculo = get_object_or_404(Vehiculos, pk=pk)
      form = self.form_class(instance=vehiculo)
      return render(request, self.template_name, {'form':form,'vehiculo': vehiculo})


  def post(self, request, pk): 
      vehiculo = get_object_or_404(Vehiculos, pk=pk)
      form = self.form_class(request.POST ,instance=vehiculo)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el vehiculo {form.cleaned_data.get('modelo')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'vehiculo': vehiculo,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarVehiculo(View):
  template_name = 'ejemplo/vehiculo.html'

  

  def get(self, request, pk): 
      vehiculo = get_object_or_404(Vehiculos, pk=pk)
      vehiculo.delete()
      vehiculos = Vehiculos.objects.all()
      return render(request, self.template_name, {'lista_vehiculos': vehiculos})