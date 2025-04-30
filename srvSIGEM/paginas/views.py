from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Articulo

from .forms import ArticuloForm
from django.contrib.auth.forms import UserCreationForm


def inicio(request):
    return render(request, 'paginas/inicio.html')

def index(request):
    return render(request, 'paginas/index.html')    

def inventario_list(request):
    busqueda = request.GET.get('buscar', '')
    articulos = Articulo.objects.all()

    if busqueda:
        articulos = articulos.filter(nombre__icontains=busqueda)

    return render(request, 'paginas/inventario.html', {'articulos': articulos})

def agregar_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = ArticuloForm()
    return render(request, 'paginas/agregar_articulo.html', {'form': form})

def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'paginas/editar_articulo.html', {'form': form, 'articulo': articulo})

def eliminar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        return redirect('inventario')
    return render(request, 'paginas/eliminar_articulo.html', {'articulo': articulo})

class RegistroUsuario(CreateView):
    form_class = UserCreationForm
    template_name = 'paginas/register.html'
    success_url = reverse_lazy('login')


def control_solicitudes(request):
    return render(request, 'paginas/control_vista_admin.html')

def solicitudes_list(request):
    return render(request, 'paginas/solicitudes.html')

