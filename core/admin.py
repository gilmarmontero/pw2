from django.contrib import admin
from .models import(
    Marca, 
    Veiculo, 
    Pessoa, 
    Mensalista,
    MovMensalista,
    Parametro_hora,
    Parametro_mensal,
    Movimento_Rotativo
)

class Mov_Rotativo_Admin(admin.ModelAdmin):
    list_display = (
        'veiculo', 'checkin', 'checkout', 'valor_hora', 'quant_hora', 'valor_total', 'pago')

    def veiculo(self, obj):
        return obj.veiculo


class Mov_Mensalista_Admin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pgto', 'total')







admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametro_hora)
admin.site.register(Parametro_mensal)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, Mov_Mensalista_Admin)
admin.site.register(Movimento_Rotativo, Mov_Rotativo_Admin)



