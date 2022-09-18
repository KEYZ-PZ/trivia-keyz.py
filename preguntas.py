import re


class Pregunta:
    def __init__(self, **kwargs):
        self.pregunta = kwargs.get("pregunta", "no.")
        self.puntos = kwargs.get("puntos", 0)

    def __str__(self):
        return "Se ha agregado exitosamente {}".format(self.pregunta)

    def retornaPregunta(self):
        return self.pregunta


class devolverPr:
    def cargapreguntas(self):
        archivo = open("lista_preguntas.txt", encoding="utf-8")
        informacion = archivo.read()
        archivo.close()
        lista_p = re.findall(r"¿\w+[\s\w]+\?", informacion)
        return lista_p

    def agregapreguntas(self, preguntaN):
        archivo = open("lista_preguntas.txt", "a", encoding="utf-8")
        informacion = archivo.write("\n" + preguntaN)
        archivo.close()