import cachipun
import login

print("Bienvenidos al juego de cachipun")

if login.registrar():
        cachipun.cachipun()

else:
        print("Vuelve a ingresar")