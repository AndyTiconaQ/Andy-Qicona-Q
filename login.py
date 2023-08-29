def registrar():
    usuario = "Andy"
    contraseña = "andy2236"

    nombre_usuario= input("Ingrese su nombre de usuario: ")
    password=input("Ingrese la contraseña: ")

    if usuario == nombre_usuario and contraseña == password:
          return True
    else:
          return False
if __name__ =="__main__":
     registrar()