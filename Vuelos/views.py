from django.shortcuts import render, redirect
from .forms import FormsVuelo
from django.db.models import Avg
from .models import Vuelo

def home(request):
    return render(request, 'vuelos/home.html')

def registrar_vuelo(request):
    if request.method == 'POST':
        form = FormsVuelo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadevuelos')
    else:
        form = FormsVuelo()
    return render(request, 'vuelos/registrar_vuelo.html', {'form': form})

def estadisticas(request):
    total_n = Vuelo.objects.filter(tipo_vuelo='Nacional').count()
    total_intern = Vuelo.objects.filter(tipo_vuelo='Internacional').count()
    promedio_n = Vuelo.objects.filter(tipo_vuelo='Nacional').aggregate(Avg('precio'))['promedio'] or 0
    return render(request, 'vuelos/estadisticas.html', {
        'total_n': total_n,
        'total_intern': total_intern,
        'promedio_n': promedio_n,
    })

def listadevuelos(request):
    vuelos = Vuelo.objects.all().order_by('precio')
    return render(request, 'vuelos/listadevuelos.html', {'vuelos': vuelos})