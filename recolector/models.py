from django.db import models

# Create your models here.

class Recolector(models.Model):
    nombre_recolector = models.CharField(max_length = 50, null = False, blank = False)
    apellido_recolector = models.CharField(max_length = 50, null = False, blank = False)
    correo_recolector = models.EmailField( null = False, blank = False)
    telefono_recolector = models.CharField( max_length = 50, null = False, blank = False)
    calificacion_recolector = models.FloatField()
    estado = models.IntegerField()
    cantidad_calificaciones = models.FloatField()
    suma_calificaciones = models.FloatField()

    class Meta:
        verbose_name = 'Recolector'
        verbose_name_plural = 'Recolectores'
        ordering = ['nombre_recolector']

    def __str__(self):
        return self.nombre_recolector
        
class Historial_Recolector(models.Model):
    id_recolector = models.ForeignKey(Recolector, null = True, blank = True, on_delete=models.CASCADE)
    fecha_finalizado = models.CharField(max_length = 50, null = False, blank = False)

    class Meta:
        verbose_name = "Historial"
        verbose_name_plural = "Historiales"

    def __str__(self):
        return self.fecha_finalizado
    