from django.db import models
import math
from datetime import datetime
from datetime import timedelta
import datetime


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    endereco = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    marca = models.ForeignKey("Marca", on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey("Pessoa", on_delete=models.CASCADE)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()

    def __str__(self):
        return str(self.modelo) + ' - ' +str(self.placa) 


class Parametro_hora(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.valor_hora)


class Parametro_mensal(models.Model):
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.valor_mes)



class Movimento_Rotativo(models.Model):
    
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora = models.ForeignKey("Parametro_hora", on_delete=models.CASCADE)
    veiculo = models.ForeignKey("Veiculo", on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def quant_hora(self):
        return math.ceil((self.checkout-self.checkin).total_seconds() / 3600)

    def valor_total(self):
        return self.valor_hora * self.quant_hora()


    def __str__(self):
        return self.veiculo.placa
    

class Mensalista(models.Model):
    veiculo = models.ForeignKey("Veiculo", on_delete=models.CASCADE)
    inicio = models.DateField(null=True, blank=True)
    valor_mes = models.ForeignKey("Parametro_mensal", on_delete=models.CASCADE)
    data_pgto = models.DateField(null=True, blank=True)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return str(self.veiculo) + ' - ' + str(self.veiculo.placa) + ' - ' + str(self.inicio)   



class MovMensalista(models.Model):
    mensalista = models.ForeignKey("Mensalista", on_delete=models.CASCADE)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.mensalista) + '  -  ' + str(self.total)
     


