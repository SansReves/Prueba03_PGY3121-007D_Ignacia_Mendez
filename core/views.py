from django.contrib import messages
from django.shortcuts import redirect, render
from .models import categoria, pedido
from django.contrib.auth.decorators import login_required, permission_required

from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import PasswordResetForm

from .filters import pedidoFiltros

# Create your views here.

def home (request):
        return render(request, 'core/index.html')

def quienes_somos (request):
        return render(request, 'core/quienessomos.html')

@login_required
def pedidos (request):
        #combo box
        listado_categ = categoria.objects.all()
        data = {"categorias" : listado_categ}

        #guardar
        if request.POST:
                ped = pedido()
                ped.nombre = request.POST.get("txtNombre")
                ped.correo= request.POST.get("emailC")
                ped.telefono = request.POST.get("cell")
                ped.direccion = request.POST.get("direc")
                ped.cantidad = request.POST.get("cant")
                ped.comentario = request.POST.get("descrp")
                ped.imagen = request.FILES.get("txtImagen")


                cat = categoria()
                cat.id = request.POST.get("cboCategoria")
                ped.categoria = cat

                try:
                        ped.save()
                        mensaje = "Enviado correctamente"
                        messages.success(request, mensaje)
                except:
                        mensaje = "Error al Enviar"
                        messages.error(request, mensaje)

        return render(request, 'core/pedido.html', data)


@login_required
def listado(request):
        listado_pedido = pedido.objects.all()
        miFiltro = pedidoFiltros(request.POST, queryset=listado_pedido)
        listado_pedido = miFiltro.qs

        #diccionario
        data = {"lista_ped" : listado_pedido,
                "filtro": miFiltro}

        return render(request, 'core/listado.html',data)



@login_required
@permission_required('core.add_pedido')
def eliminar(request, id):
        ped = pedido.objects.get(id=id)
        try:
                ped.delete()
                mensaje = "Eliminado correctamente"
                messages.success(request, mensaje)
        except:
                mensaje = "Error al Eliminar"
                messages.error(request, mensaje)
        return redirect('listado')


@login_required
@permission_required('core.delete_pedido')
def modificar(request, id):
        ped = pedido.objects.get(id=id)
        listado_categ = categoria.objects.all()
        data = {"categorias" : listado_categ,
                "ped": ped}

        if request.POST:
                ped = pedido()
                ped.nombre = request.POST.get("txtNombre")
                ped.correo= request.POST.get("emailC")
                ped.telefono = request.POST.get("cell")
                ped.direccion = request.POST.get("direc")
                ped.cantidad = request.POST.get("cant")
                ped.comentario = request.POST.get("descrp")
                ped.imagen = request.FILES.get("txtImagen")


                cat = categoria()
                cat.id = request.POST.get("cboCategoria")
                ped.categoria = cat

                try:
                        ped.save()
                        mensaje = "Modificado correctamente"
                        messages.success(request, mensaje)
                except:
                        mensaje = "Error al Modificar"
                        messages.error(request, mensaje)
                return redirect("listado")
        
        return render(request, "core/modificar.html", data)


def registroUsuarios(request):
    data = { "form" : CustomUserCreationForm  }
    if request.POST:
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"],
                                password = formulario.cleaned_data["password1"])
            messages.success(request, "Te has registrado correctamente")
            login(request, user)
            return redirect("home")
        data["form"] = formulario
    return render(request,  "registration/registroUsuarios.html", data)


def cambiarContrasenia(request):
        data= { "form" : PasswordResetForm }
        if request.POST:
                formulario = PasswordResetForm(request.POST)
        

        return render(request, "password_reset/cambiarContrasenia.html", data)

