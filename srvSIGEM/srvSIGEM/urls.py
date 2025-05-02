from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from paginas import views  
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('inicio/', views.index, name='index'),

    # Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='paginas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegistroUsuario.as_view(), name='register'),  # ✅ Correcto

    # Cambio de contraseña
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='paginas/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='paginas/password_change_done.html'), name='password_change_done'),

    # Recuperación de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='paginas/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='paginas/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='paginas/reset.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='paginas/password_reset_done.html'), name='password_reset_complete'),

    # Inventario CRUD
    path('inventario/', views.inventario_list, name='inventario'),
    path('inventario/agregar/', views.agregar_articulo, name='agregar_articulo'),
    path('inventario/editar/<int:pk>', views.editar_articulo, name='editar_articulo'),
    path('inventario/eliminar/<int:pk>', views.eliminar_articulo, name='eliminar_articulo'),
    
    path('control_vista_admin/', views.control_solicitudes, name='control_vista_admin'),
    path('solicitudes/', views.solicitudes_list, name='solicitudes_list'),
    
    path('miembros/', views.lista_miembros, name='lista_miembros'),
    path('miembros/agregar/', views.agregar_miembro, name='agregar_miembro'),
    path('miembros/editar/<int:pk>/', views.editar_miembro, name='editar_miembro'),
    path('miembros/eliminar/<int:pk>/', views.eliminar_miembro, name='eliminar_miembro'),
    
    path('reporte/', views.reporte_formulario, name='reporte_formulario'),
    path('reporte/pdf/', views.generar_reporte_pdf, name='generar_reporte_pdf'),
]

# Servir archivos estáticos y media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


