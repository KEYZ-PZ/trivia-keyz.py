import preguntas
import respuestas
import random


def inicioJ():
    print("Bienvenido al juego de trivia.")
    print(" 1 - Comenzar juego\n 2 - Agregar nuevas preguntas")
    opc = input(":")

    if opc == "1":
        buscaPreguntas = preguntas.devolverPr()
        lista_preguntas = buscaPreguntas.cargapreguntas()
        buscarRespuestas = respuestas.retornaRespuesta()
        lista_respuestas = buscarRespuestas.cargarespuestas()
        cont = 0
        while cont < len(lista_preguntas):
            intR = random.randint(0, len(lista_preguntas) - 1)
            print("\nPregunta {}\n ".format(cont + 1))
            print(" - {}\n".format(lista_preguntas[intR]))
            opc = input("Su respuesta es: ")
            if opc in lista_respuestas[intR]:
                print("\nFelicidades haz acertado")
            else:
                print("\nHaz fallado")
            cont += 1
    else:
        lista_pr = list()
        list_rp = list()
        creaP = preguntas.devolverPr()
        creaR = respuestas.retornaRespuesta()
        bandera = True
        while bandera:
            print("Su pregunta debe iniciar con ¿ y terminar con ?")
            opc = input(":> ")
            print()
            # agrego la pregunta en la lista

            print(opc)
            lista_pr.append(preguntas.Pregunta(pregunta=opc))
            # # agrego la pregunta en el archivo
            creaP.agregapreguntas(lista_pr[len(lista_pr) - 1].retornaPregunta())
            print("\n se ha agregado con exito la pregunta {}\n".format(
                lista_pr[len(lista_pr) - 1]))
            print("Su Respuesta debe iniciar con R/ seguido de un espacio y terminar con .")
            opc1 = input(":> ")
            # agrego la respuesta en la lista
            list_rp.append(respuestas.Respuesta(resp=opc1))
            # # agrego la respuesta en el archivo
            creaR.agregarespuestas(list_rp[len(list_rp) - 1].retornaR())
            print("\n se ha agregado con exito la respuesta {}".format(list_rp[len(list_rp) - 1]))
            print("\n¿Desea añadir otra pregunta?\n 1 - si\n 2 - no")
            opc2 = input(":> ")

            if opc2 == "2":
                bandera = False
        inicioJ()


inicioJ()