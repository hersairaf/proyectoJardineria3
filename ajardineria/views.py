from django.shortcuts import render
from .models import Cliente

def index(request):
    clientes = Cliente.objects.all() 
    context = {'clientes': clientes} 
    return render(request, 'ajardineria/index.html', context)

def crud(request):
    clientes = Cliente.objects.all() 
    context = {'clientes': clientes} 
    return render(request, 'ajardineria/clientes_list.html', context)

def listadoSQL(request):
    clientes = Cliente.objects.raw('SELECT * FROM ajardineria_cliente')
    print(clientes)
    context = {'clientes': clientes}
    return render(request, 'ajardineria/listadoSQL.html', context)

def ClientesAdd(request):
    if request.method is not 'POST':
        clientes = Cliente.objects.all()
        context = {'clientes': clientes}
        return render(request, 'ajardineria/clientes_add.html', context)
    
    else:
        rut=request.POST('rut')
        nombre=request.POST('nombre')
        apaterno=request.POST('apaterno')
        amaterno=request.POST('amaterno')
        email=request.POST('email')
        fono=request.POST('fono')

        obj = Cliente.objects.create(rut=rut, nombre=nombre, apaterno=apaterno, amaterno=amaterno, email=email, fono=fono)
        obj.save()
        context = {'mensaje':"Datos guardados..."}
        return render(request, 'ajardineria/clientes_add.html', context)
    
def clientes_del(request, pk):
    context = {}
    try:
        cliente=Cliente.objects.get(rut=pk)

        cliente.delete()
        mensaje="Cliente eliminado"
        clientes = Cliente.objects.all()
        context = {'clientes': clientes, 'mensaje': mensaje}
        return render(request, 'ajardineria/clientes_list.html', context)
    except:
        mensaje="Cliente no encontrado"
        clientes = Cliente.objects.all()
        context = {'clientes': clientes, 'mensaje': mensaje}
        return render(request, 'ajardineria/clientes_list.html', context)
    
def ClientesUpdate(request):
    if request.method == 'POST':
        rut=request.POST('rut')
        nombre=request.POST('nombre')
        apaterno=request.POST('apaterno')
        amaterno=request.POST('amaterno')
        email=request.POST('email')
        fono=request.POST('fono')

        try:
            cliente = Cliente.objects.get(rut=rut)
            cliente.nombre=nombre
            cliente.apaterno=apaterno
            cliente.amaterno=amaterno
            cliente.email=email
            cliente.fono=fono
            cliente.save()
            context = {'mensaje':"Datos actualizados...", 'cliente': cliente}
            return render(request, 'ajardineria/clientes_edit.html', context)
        except Cliente.DoesNotExist:
            mensaje="Cliente no encontrado"
            clientes = Cliente.objects.all()
            context = {'clientes': clientes, 'mensaje': mensaje}
            return render(request, 'ajardineria/clientes_list.html', context)
    else:
        clientes = Cliente.objects.all()
        context = {'clientes': clientes}
        return render(request, 'ajardineria/clientes_list.html', context)
    
def clientes_findEdit(request, pk):
    if pk != "":
        cliente = Cliente.objects.get(rut=pk)

        context = {'cliente': cliente}
        if cliente:
            return render(request, 'ajardineria/clientes_edit.html', context)
        else:
            context = {'mensaje': "Cliente no encontrado"}
            return render(request, 'ajardineria/clientes_list.html', context)