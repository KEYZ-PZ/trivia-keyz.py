import re


class Respuesta:
    def __init__(self, **kwargs):
        self.resp = kwargs.get("resp", "no")

    def __str__(self):
        return "Se ha agregado exitosamente {}".format(self.resp)

    def retornaR(self):
        return self.resp


class retornaRespuesta:
    def cargarespuestas(self):
        archivo = open("lista_preguntas.txt", encoding="utf-8")
        informacion = archivo.read()
        archivo.close()
        lista_respuestas = re.findall(r"R\/[\s\w]+\.*", informacion)
        return lista_respuestas

    def agregarespuestas(self, respuestaN):
        archivo = open("lista_preguntas.txt", "a")
        informacion = archivo.write("\n\n" + respuestaN)
        archivo.close()
