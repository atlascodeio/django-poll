from django.db import models
from django.utils import timezone
from datetime import timedelta



# Create your models here.

class Preguntas(models.Model):

	asunto = models.TextField()
	fecha  = models.DateTimeField()

	def __str__(self):
		return self.asunto

	def hoy(self):
		return self.fecha >= timezone.now() - timezone.timedelta(days=1)


class Respuestas(models.Model):

	respuesta = models.TextField()
	pregunta = models.ForeignKey(Preguntas)

	def __str__(self):
		return '{0} --- {1}'.format(self.pregunta,self.respuesta)
