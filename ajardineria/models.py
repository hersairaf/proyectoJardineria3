from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apaterno = models.CharField(max_length=20)
    amaterno = models.CharField(max_length=20)
    #fecha_nacimiento = models.DateField(blank=False, null=False)  # wea del ppt
    #id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero') # wea del ppt
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True) 
    fono = models.CharField(max_length=45)
    #direccion = models.CharField(max_length=50, blank=True, null=True) # wea del ppt
    #activo = models.IntegerField() # wea del ppt

    def __str__(self):
        return f"{self.nombre} {self.apaterno} {self.amaterno}"
        #return str(self.nombre) + " " + str(self.apaterno) + " " + str(self.amaterno)
    
# class Genero(models.Model):
#     id_genero = models.AutoField(db_column='idGenero', primary_key=True)
#     genero = models.CharField(max_length=20, blank=False, null=False)
#
#     def __str__(self):
#         return self.genero