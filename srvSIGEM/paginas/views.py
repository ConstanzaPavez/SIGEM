from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Articulo, Miembro
from .forms import ArticuloForm, MiembroForm
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


def lista_miembros(request):
    query = request.GET.get('buscar')
    if query:
        miembros = Miembro.objects.filter(nombre__icontains=query) | Miembro.objects.filter(rol__icontains=query)
    else:
        miembros = Miembro.objects.all()
    return render(request, 'paginas/lista_miembros.html', {
        'miembros': miembros,
        'buscar': query or '',
    })

def agregar_miembro(request):
    if request.method == 'POST':
        form = MiembroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_miembros')
    else:
        form = MiembroForm()
    
    return render(request, 'paginas/agregar_miembro.html', {'form': form})

def editar_miembro(request, pk):
    miembro = get_object_or_404(Miembro, pk=pk)
    if request.method == 'POST':
        form = MiembroForm(request.POST, request.FILES, instance=miembro)
        if form.is_valid():
            form.save()
            return redirect('lista_miembros')
    else:
        form = MiembroForm(instance=miembro)
    return render(request, 'paginas/editar_miembro.html', {'form': form, 'miembro': miembro})


def eliminar_miembro(request, pk):
    miembro = get_object_or_404(Miembro, pk=pk)
    if request.method == 'POST':
        miembro.delete()
        return redirect('lista_miembros')
    return render(request, 'paginas/eliminar_miembro.html', {'miembro': miembro})    

    
def reporte_formulario(request):
    return render(request, 'paginas/reporte.html')

def generar_reporte_pdf(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_equipo')
        fecha = request.POST.get('fecha')
        responsable = request.POST.get('responsable')
        # le pregunte a chatgpt esta parte porque no sabia como hacerla knjcenwdnwdk
        # Aquí va la lógica del backend para generar el PDF
        # pdf_file = generar_pdf_reporte(nombre, fecha, responsable)
        # return FileResponse(open(pdf_file, 'rb'), content_type='application/pdf')

        # Temporal
        return render(request, 'paginas/reporte.html', {'mensaje': 'PDF generado (simulado)'})    

     