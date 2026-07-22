from django.shortcuts import render, HttpResponse
# Create your views here.
#creamos la Primera vied de la pagina

def tienda(request):
    #return HttpResponse("Tienda")
    return render(request, 'ProyectoPag/tienda.html')
def inicio(request):
    #return HttpResponse("Inicio")
    return render(request, 'ProyectoPag/inicio.html')

def servicio(request):
    #return HttpResponse("Servicio")
    return render(request, 'ProyectoPag/servicio.html')

def contacto(request):
    #return HttpResponse("Contacto")
    return render(request, 'ProyectoPag/contacto.html')



