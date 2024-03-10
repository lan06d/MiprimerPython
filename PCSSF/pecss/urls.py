from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('registrar_Usuario',views.registrar_Usuario,name='registrar_Usuario'),
    path('ingreso_Admin',views.ingreso_Admin,name='ingreso_Admin'),
    path('formulario_Cliente',views.formulario_Cliente,name='formulario_Cliente'),
    path('formulario_Mascota',views.formulario_Mascota,name='formulario_Mascota'),
    path('formulario_Servicio',views.formulario_Servicio,name='formulario_Servicio'),
    path('formulario_Registro',views.formulario_Registro,name='formulario_Registro'),
    path('ingreso_Admin',views.listar_usuario,name='listar_usuario'),
    path('eliminar_usuario/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('pre_editar_usuario/<int:user_id>/', views.pre_editar_usuario, name='pre_editar_usuario'),
    path('actualizar_usuario/<int:user_id>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('registrar_cliente', views.registrar_cliente, name='registrar_cliente'),
    path('listar_cliente', views.listar_cliente, name='listar_cliente'),
    path('eliminar_cliente/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('pre_editar_cliente/<int:cliente_id>/', views.pre_editar_cliente, name='pre_editar_cliente'),
    path('actualizar_cliente/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('registrar_mascota', views.registrar_mascota, name='registrar_mascota'),
    path('eliminar_mascotas/<str:mascotas_id>', views.eliminar_mascotas, name='eliminar_mascotas'),
    path('pre_editar_mascota/<str:mascotas_id>', views.pre_editar_mascota, name='pre_editar_mascota'),
    path('actualizar_mascota/<str:mascotas_id>', views.actualizar_mascota, name='actualizar_mascota'),


    path('registrar_servicio', views.registrar_servicio, name='registrar_servicio'),
    path('eliminar_servicios/<str:servicios_id>', views.eliminar_servicio, name='eliminar_servicio'),
    path('pre_editar_servicio/<str:servicios_id>', views.pre_editar_servicio, name='pre_editar_servicio'),
    path('actualizar_servicio/<str:servicios_id>', views.actualizar_servicio, name='actualizar_servicio'),
    
    path('enviar_correo_Cliente', views.enviar_correo_Cliente, name='enviar_correo_Cliente'),
    path('helloworld', views.helloworld, name='helloworld'),
    path('salir', views.salir, name='salir'),
    path('linicio', views.linicio, name='linicio')



    

]