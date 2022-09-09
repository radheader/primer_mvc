from django.http import HttpResponse
from django.template import Template, Context, loader
from familia.models import FamiliaMiembro

def listar_familia(request):
    queryset = FamiliaMiembro.objects.all()
    diccionario = {'datos_familiares':queryset}
    plantilla = loader.get_template ("familia_list.html")
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)





