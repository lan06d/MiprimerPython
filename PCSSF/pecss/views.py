from django.shortcuts import render, redirect, get_object_or_404
from . models import Usuario, Cliente, Mascota, Servicio, TipoServicio
import json
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def helloworld(request):
    if request.method == 'GET':
        return render(request, 'pecss/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect ('inicio')
            except:
                return render(request, 'pecss/signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya exixte '
                })
        else:
            return render(request, 'pecss/signup.html', {
            'form': UserCreationForm,
            "error": 'la cable no coiciden '
            })
            
def salir(request):
    logout(request)
    return redirect('inicio')


def linicio(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("ingreso_Admin")
        # Si la autenticación falla, se renderiza el formulario de inicio de sesión con un mensaje de error.
        return render(request, 'pecss/login.html', {'form': form, 'error': 'Nombre de usuario o contraseña incorrectos.'})
    else:
        # Si es una solicitud GET, simplemente renderiza el formulario de inicio de sesión.
        form = AuthenticationForm()
        return render(request, 'pecss/login.html', {'form': form})


# Envio de coorreos

def enviar_correo_Cliente(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        subject = asunto
        message = mensaje
        from_email = settings.EMAIL_HOST_USER
        to_email = [email]
        # send_mail(subject, message, from_email, to_email, html_message=mensaje_html)
        msg = EmailMultiAlternatives(subject, message, from_email, to_email)
        msg.send()
        return redirect('ingreso_Admin')

    return redirect("ingreso_Admin")


# Create your views here.
def inicio(request):
    return render(request, 'pecss/login.html')


def ingreso_Admin(request):
    usuariosf = Usuario.objects.all()
    clientes = Cliente.objects.all()
    mascota = Mascota.objects.all()
    servicio = Servicio.objects.all()

    data = {
        "usuarios": usuariosf,
        "clientes": clientes,
        "mascotas": mascota,
        "servicios": servicio
    }

    return render(request, "pecss/inicio.html", data)


def formulario_Cliente(request):
    return render(request, 'pecss/cliente.html')


def formulario_Mascota(request):
    clientes = Cliente.objects.all()

    data = {
        "clientes": clientes,
    }
    return render(request, 'pecss/mascota.html', data)


def formulario_Registro(request):

    return render(request, 'pecss/Registro.html')


def formulario_Servicio(request):
    usuariosf = Usuario.objects.all()
    mascota = Mascota.objects.all()
    servicio = TipoServicio.objects.all()

    data = {
        "usuarios": usuariosf,
        "mascotas": mascota,
        "tipoServicio": servicio
    }

    return render(request, 'pecss/servicio.html', data)


def registrar_Usuario0(request):
    if request.method == 'POST':
        rol = request.POST.get('rol')
        email = request.POST.get('email')
        clave = request.POST.get('clave')
        telefono = request.POST.get('telefono')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellido')
        tipoDocumento = request.POST.get('tipoDocumento')
        numDocumento = request.POST.get('numDocumento')
        direccion = request.POST.get('direccion')
        estado = request.POST.get('estado')

        usuario = Usuario(
            # nombre de los campos de la base de datos
            rol=rol,
            email=email,
            clave=clave,
            telefono=telefono,
            nombres=nombres,
            apellidos=apellidos,
            tipoDocumento=tipoDocumento,
            numDocumento=numDocumento,
            direccion=direccion,
            estado=estado,

        )
        usuario.save()
        mensaje_html = """
        <html>
        <head>
            <style>
                body {
                    font-family: Monaco,monospace;
                    background-color: #737373;
                }
                .container {
                    padding: 20px;
                    background-color: #ffffff;
                    border-radius: 5px;
                    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    color: #297EF7;
                }
                 p {
                    color: #353535 ;
                }
                
            </style>
        </head>
        <body>
            <div class="container">
                <h1>¡ISA te da la bienvenida!</h1>
                <img src="https://media.istockphoto.com/id/1184633031/es/vector/ilustraci%C3%B3n-aislada-del-vector-de-hamburguesa-de-dibujos-animados.jpg?s=612x612&w=0&k=20&c=z5ix4pq2ObfRoSLenX6rdYd7zjGoYmpgpjYkQ6ych2Q=" alt="hamburguesa"width="150" height="150" >
                <p>Esperamos que disfrutes de tu experiencia.</p>
            </div>
        </body>
        </html>
        """
        subject = 'Registro exitoso'
        message = '¡Gracias por registrarte en nuestro sitio!'
        from_email = settings.EMAIL_HOST_USER
        to_email = [email]
        # send_mail(subject, message, from_email, to_email, html_message=mensaje_html)
        msg = EmailMultiAlternatives(subject, message, from_email, to_email)
        msg.attach_alternative(mensaje_html, "text/html")
        msg.send()
        return redirect('ingreso_Admin')

    return redirect("ingreso_Admin")



def registrar_Usuario(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        rol = request.POST.get('rol')
        email = request.POST.get('email')
        clave = request.POST.get('password1')
        telefono = request.POST.get('telefono')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellido')
        tipoDocumento = request.POST.get('tipoDocumento')
        numDocumento = request.POST.get('numDocumento')
        direccion = request.POST.get('direccion')
        estado = request.POST.get('estado')

        if password1 == password2:
            # Crear usuario de Django
            try:
                user = User.objects.create_user(username=email, first_name=nombres, last_name=apellidos, email=email, password=password1)
            except:
                return render(request, 'pecss/Registro.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe '
                })

            # Crear usuario personalizado
            usuario = Usuario(
                rol=rol,
                email=email,
                clave=clave,
                telefono=telefono,
                nombres=nombres,
                apellidos=apellidos,
                tipoDocumento=tipoDocumento,
                numDocumento=numDocumento,
                direccion=direccion,
                estado=estado,
            )
            usuario.save()

            # Aquí puedes agregar el código para enviar el correo electrónico

            return redirect('ingreso_Admin')
        else:
            return render(request, 'pecss/Registro.html', {
                'form': UserCreationForm,
                "error": 'Las contraseñas no coinciden '
            })

    return redirect("ingreso_Admin")

# Resto del código...





def listar_usuario(request):
    usuariosf = Usuario.objects.all()
    return render(request, "pecss/inicio.html", {"usuarios": usuariosf})


def eliminar_usuario(request, user_id):
    usuarios = Usuario.objects.get(id=user_id)
    usuarios.delete()
    return redirect("ingreso_Admin")


def pre_editar_usuario(request, user_id):
    usuario = Usuario.objects.get(id=user_id)
    return render(request, 'pecss/editarusuario.html', {'usuario': usuario})


def actualizar_usuario(request, user_id):
    if request.method == 'POST':
        usuario = Usuario.objects.get(id=user_id)
        usuario.rol = request.POST['rol']
        usuario.email = request.POST['email']
        usuario.clave = request.POST['clave']
        usuario.telefono = request.POST['telefono']
        usuario.nombres = request.POST['nombres']
        usuario.apellidos = request.POST['apellidos']
        usuario.tipoDocumento = request.POST['tipoDocumento']
        usuario.numDocumento = request.POST['numDocumento']
        usuario.direccion = request.POST['direccion']
        usuario.estado = request.POST['estado']
        usuario.save()
        return redirect('ingreso_Admin')
    else:
        return redirect('editar_usuario', user_id=user_id)


# Clientes


# Otros métodos existentes omitidos por brevedad

def registrar_cliente(request):
    if request.method == 'POST':
        tipoDocumento = request.POST.get('tipoDocumento')
        numeroIdentificacion = request.POST.get('numeroIdentificacion')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direecion = request.POST.get('direecion')
        estado = request.POST.get('estado')

        cliente = Cliente(
            tipoDocumento=tipoDocumento,
            numeroIdentificacion=numeroIdentificacion,
            nombres=nombres,
            apellidos=apellidos,
            telefono=telefono,
            email=email,
            direecion=direecion,
            estado=estado
        )
        cliente.save()
        # Redirigir a la lista de clientes después de registrar uno nuevo
        return redirect('formulario_Cliente')
    # Si no es un POST, simplemente renderizar el formulario
    return render(request, 'pecss/cliente.html')


def listar_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'pecss/listar_clientes.html', {'clientes': clientes})


def eliminar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    # Redirigir a la lista de clientes después de eliminar uno
    return redirect('ingreso_Admin')


def pre_editar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, 'pecss/editarCliente.html', {'cliente': cliente})


def actualizar_cliente(request, cliente_id):
    if request.method == 'POST':
        cliente = Cliente.objects.get(id=cliente_id)
        cliente.tipoDocumento = request.POST.get('tipoDocumento')
        cliente.numeroIdentificacion = request.POST.get('numeroIdentificacion')
        cliente.nombres = request.POST.get('nombres')
        cliente.apellidos = request.POST.get('apellidos')
        cliente.telefono = request.POST.get('telefono')
        cliente.email = request.POST.get('email')
        cliente.direecion = request.POST.get('direecion')
        cliente.estado = request.POST.get('estado')
        cliente.save()
        # Redirigir a la lista de clientes después de actualizar uno
        return redirect('ingreso_Admin')
    else:
        return redirect('pre_editar_cliente', cliente_id=cliente_id)


# Mascotas


def registrar_mascota(request):
    if request.method == 'POST':
        fk_ID_cliente = request.POST.get('fk_ID_cliente')
        nombreMascota = request.POST.get('nombreMascota')
        estado = request.POST.get('estado')
        raza = request.POST.get('raza')
        edad = request.POST.get('edad')
        observacion = request.POST.get('observacion')

        mascota = Mascota(
            # nombre de los campos de la base de datos
            fk_ID_cliente=Cliente.objects.get(id=fk_ID_cliente),
            nombreMascota=nombreMascota,
            estado=estado,
            raza=raza,
            edad=edad,
            observacion=observacion,

        )
        mascota.save()
    return redirect("ingreso_Admin")


def listar_mascota(request):
    mascota = Mascota.objects.all()
    return render(request, 'pecss/ingreso_Admin.html', {'mascotas': mascota})


def eliminar_mascotas(request, mascotas_id):
    mascota = Mascota.objects.get(id=mascotas_id)
    mascota.delete()
    # Redirigir a la lista de clientes después de eliminar uno
    return redirect('ingreso_Admin')


def pre_editar_mascota(request, mascotas_id):
    mascotas = Mascota.objects.get(id=mascotas_id)
    clientes = Cliente.objects.all()

    data = {
        "clientes": clientes,
        "mascotas": mascotas,
    }

    return render(request, 'pecss/editarMascota.html', data)


def actualizar_mascota(request, mascotas_id):
    if request.method == 'POST':
        mascotas = Mascota.objects.get(id=mascotas_id)
        mascotas.fk_ID_cliente = Cliente.objects.get(
            id=request.POST.get('fk_ID_cliente'))
        mascotas.nombreMascota = request.POST.get('nombreMascota')
        mascotas.estado = request.POST.get('estado')
        mascotas.raza = request.POST.get('raza')

        mascotas.edad = request.POST.get('edad')
        mascotas.observacion = request.POST.get('observacion')

        mascotas.save()
        # Redirigir a la lista de clientes después de actualizar uno
        return redirect('ingreso_Admin')
    else:
        return redirect('pre_editar_mascota', mascotas_id=mascotas_id)


# Tipo de servicio


def registrar_tipo_servicio(request):
    if request.method == 'POST':
        tipo_servicio = request.POST.get('tipo_servicio')
        valor_servicio = request.POST.get('valor_servicio')

        tipoServicio = TipoServicio(
            tipo_servicio=tipo_servicio,
            valor_servicio=valor_servicio,

        )
        tipoServicio.save()
        # Redirigir a la lista de clientes después de registrar uno nuevo
        return redirect('ingreso_Admin')
    # Si no es un POST, simplemente renderizar el formulario
    return render(request, 'pecss/cliente.html')


# Servicio


def registrar_servicio(request):
    if request.method == 'POST':
        fk_id_tipo_servicio = request.POST.get('fk_id_tipo_servicio')
        fk_id_usuario = request.POST.get('fk_ID_usuario')
        fk_id_mascota = request.POST.get('fk_ID_mascota')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        observacion = request.POST.get('observacion')
        estado = request.POST.get('estado')

        servicio = Servicio(
            # nombre de los campos de la base de datos
            fk_id_tipo_servicio=TipoServicio.objects.get(
                id=fk_id_tipo_servicio),
            fk_id_usuario=Usuario.objects.get(id=fk_id_usuario),
            fk_id_mascota=Mascota.objects.get(id=fk_id_mascota),
            fecha=fecha,
            hora=hora,
            observacion=observacion,
            estado=estado

        )
        servicio.save()
    return redirect("ingreso_Admin")


def eliminar_servicio(request, servicios_id):
    servicios = Servicio.objects.get(id=servicios_id)
    servicios.delete()
    # Redirigir a la lista de clientes después de eliminar uno
    return redirect('ingreso_Admin')


def pre_editar_servicio(request, servicios_id):
    servicio = Servicio.objects.get(id=servicios_id)
    usuariosf = Usuario.objects.all()
    mascotas = Mascota.objects.all()
    tipoServicios = TipoServicio.objects.all()

    fa = servicio.fecha

    if fa.day >= 1 and fa.day <= 9:
        dia = "0" + str(fa.day)
    else:
        dia = str(fa.day)

    if fa.month >= 1 and fa.month <= 9:
        mes = "0" + str(fa.month)
    else:
        mes = str(fa.month)

    fecha = str(fa.year) + "-" + mes + "-" + dia

    h = servicio.hora

    hora = h.strftime("%I:%M %p")

    data = {
        "servicios": servicio,
        "usuarios": usuariosf,
        "mascotas": mascotas,
        "tipoServicios": tipoServicios,
        "fechas": fecha,
        "horas": hora
    }

    return render(request, 'pecss/editarServicio.html', data)


def actualizar_servicio(request, servicios_id):
    if request.method == 'POST':
        servicios = Servicio.objects.get(id=servicios_id)
        servicios.fk_id_tipo_servicio = TipoServicio.objects.get(
            id=request.POST.get('fk_id_tipo_servicio'))
        servicios.fk_id_usuario = Usuario.objects.get(
            id=request.POST.get('fk_ID_usuario'))
        servicios.fk_id_mascota = Mascota.objects.get(
            id=request.POST.get('fk_ID_mascota'))
        servicios.fecha = request.POST.get('fecha')
        servicios.hora = request.POST.get('hora')
        servicios.observacion = request.POST.get('observacion')
        servicios.estado = request.POST.get('estado')

        servicios.save()
        # Redirigir a la lista de clientes después de actualizar uno
        return redirect('ingreso_Admin')
    else:
        return redirect('pre_editar_servicio', servicios_id=servicios_id)
