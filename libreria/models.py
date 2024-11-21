from django.db import models

class Libro(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    descripcion = models.TextField(verbose_name="Descripcion", null=True)

def __str__(self):
    fila = "Titulo: " + self.titulo + " " + "Descripcion: " + self.descripcion
    return fila

def delete(self, using=None, keep_parent=False):
    self.imagen.storage.delete(self.imagen.name, keep_parent=keep_parent)
    super().delete()