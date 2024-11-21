from django.urls import path
from libreria import views
from django.conf import settings

from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('crear', views.crear, name='crear'),
    path('editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('crear usuario', views.crear_usuario, name='crear_usuario'),
    path('login', views.login_request, name="Login"),
    path('cursoFormulario', views.cursoFormulario, name="cursoformulario"),
    path('registrar', views.registrar, name="registrar")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)