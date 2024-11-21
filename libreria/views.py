from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Libro
from .forms import LibroForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
@login_required

def inicio(request):
    return render(request, 'registration/login.html')
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "paginas/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "paginas/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "paginas/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "registration/login.html", {"form": form})

def inicio(request):
    return render(request, 'registration/login.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def libros(request):
    libros = Libro.objects.all()
    return render(request, 'paginas/libros/index.html', {'libros': libros})
def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'paginas/libros/crear.html', {'formulario': formulario})
def editar(request, id):
    libros = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libros)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros')
    return render(request, 'paginas/libros/editar.html', {'formulario': formulario})
def eliminar(request, id):
    libros = Libro.objects.get(id=id)
    libros.delete()
    return redirect('libros')
def registrar(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"paginas/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"paginas/registro.html" ,  {"form":form})


def crear_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'paginas/registro.html', {'form': form})

def cursoFormulario(request):
    return render(request,"paginas/curso_formulario.html")


