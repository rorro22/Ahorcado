import random
from django.shortcuts import render, redirect

# Lista de dibujos ASCII del ahorcado
HANGMANPICS = [
r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', 
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

# Lista de palabras mexicanas
PALABRAS = [
    "tamal", "chile", "nopal", "aguacate", "pozole", "quesadilla", "chapulin",
    "mariachi", "charro", "cempasuchil", "xoloitzcuintle", "huarache", "tlacoyo",
    "huipil", "axolote", "cuate", "alebrije", "mezcal", "tequila",
    "cenote", "piñata", "frida", "sombrero", "mole", "tlatoani", "papalote",
    "calavera", "loteria", "tlacualero", "cobija", "milpa", "antojito", "carnitas",
    "pastorela", "nahual", "zacate", "jacal", "mitote", "guajolote"
]

# Vista que inicializa el juego
def iniciar_juego(request):
    palabra = random.choice(PALABRAS)
    espacios = ["_" for _ in palabra]

    request.session["palabra"] = palabra
    request.session["espacios"] = espacios
    request.session["errores"] = 0
    request.session["letras_usadas"] = []

    return redirect("juego")


# Vista principal del juego
def juego(request):
    # Verifica que existan los datos en sesión, si no, redirige a iniciar_juego
    if not all(k in request.session for k in ("palabra", "espacios", "errores", "letras_usadas")):
        return redirect("iniciar")

    palabra = request.session["palabra"]
    espacios = request.session["espacios"]
    errores = request.session["errores"]
    letras_usadas = request.session["letras_usadas"]

    terminado = False
    perdido = False

    if request.method == "POST":
        letra = request.POST.get("letra", "").lower()

        if letra and letra not in letras_usadas:
            letras_usadas.append(letra)
            if letra in palabra:
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        espacios[i] = letra
            else:
                errores += 1

        request.session["espacios"] = espacios
        request.session["errores"] = errores
        request.session["letras_usadas"] = letras_usadas

    if "_" not in espacios:
        terminado = True
    elif errores >= len(HANGMANPICS) - 1:
        perdido = True

    ascii_art = HANGMANPICS[min(errores, len(HANGMANPICS) - 1)]

    contexto = {
        "palabra": palabra,
        "espacios": " ".join(espacios),
        "errores": errores,
        "letras_usadas": letras_usadas,
        "ascii": ascii_art,
        "terminado": terminado,
        "perdido": perdido
    }

    return render(request, "juego/index.html", contexto)


# Vista para reiniciar el juego
def reiniciar(request):
    for key in ['palabra', 'espacios', 'errores', 'letras_usadas']:
        request.session.pop(key, None)
    return redirect('index')

def reiniciar_juego(request):
    request.session.flush()  # Borra todos los datos de la sesión
    return redirect('iniciar')  # Redirige a la vista de inicio