# Lista de contactos (cada contacto será un diccionario)
contactos = []

# Función para validar correo electrónico (sin usar re)
def validar_correo(correo):
    if '@' in correo and '.' in correo.split('@')[-1]:
        return True
    return False

# Función para crear un nuevo contacto
def crear_contacto():
    while True:
        try:
            nombre = input("Ingrese el nombre del contacto (máximo 50 caracteres): ")
            if len(nombre) > 50:
                print("El nombre es demasiado largo. Debe tener como máximo 50 caracteres.")
                continue  # Vuelve a pedir el nombre
            
            telefono = input("Ingrese el teléfono del contacto (11 dígitos): ")
            if len(telefono) != 11 or not telefono.isdigit():
                print("El teléfono debe tener exactamente 11 dígitos numéricos.")
                continue  # Vuelve a pedir el teléfono
            
            direccion = input("Ingrese la dirección del contacto (máximo 60 caracteres): ")
            if len(direccion) > 60:
                print("La dirección es demasiado larga. Debe tener como máximo 60 caracteres.")
                continue  # Vuelve a pedir la dirección
            
            correo = input("Ingrese el correo electrónico del contacto (máximo 50 caracteres): ")
            if len(correo) > 50:
                print("El correo electrónico es demasiado largo. Debe tener como máximo 50 caracteres.")
                continue  # Vuelve a pedir el correo
            if not validar_correo(correo):
                print("El correo electrónico no tiene un formato válido.")
                continue  # Vuelve a pedir el correo
            
            # Crear el contacto como un diccionario
            contacto = {
                'nombre': nombre,
                'telefono': telefono,
                'direccion': direccion,
                'correo': correo
            }
            contactos.append(contacto)
            print("Contacto creado exitosamente.")
            break  # Sale del bucle una vez que todo es válido
        
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

# Función para modificar un contacto
def modificar_contacto():
    while True:
        try:
            nombre_buscar = input("Ingrese el nombre del contacto que desea modificar: ")
            for contacto in contactos:
                if contacto['nombre'].lower() == nombre_buscar.lower():
                    print("Contacto encontrado.")
                    print("1. Modificar nombre")
                    print("2. Modificar teléfono")
                    print("3. Modificar dirección")
                    print("4. Modificar correo electrónico")
                    opcion = input("Seleccione la opción que desea modificar: ")

                    if opcion == '1':
                        while True:
                            nuevo_nombre = input("Ingrese el nuevo nombre: ")
                            if len(nuevo_nombre) > 50:
                                print("El nombre es demasiado largo. Debe tener como máximo 50 caracteres.")
                                continue  # Vuelve a pedir el nombre
                            contacto['nombre'] = nuevo_nombre
                            break
                    elif opcion == '2':
                        while True:
                            nuevo_telefono = input("Ingrese el nuevo teléfono (11 dígitos): ")
                            if len(nuevo_telefono) != 11 or not nuevo_telefono.isdigit():
                                print("El teléfono debe tener exactamente 11 dígitos numéricos.")
                                continue  # Vuelve a pedir el teléfono
                            contacto['telefono'] = nuevo_telefono
                            break
                    elif opcion == '3':
                        while True:
                            nueva_direccion = input("Ingrese la nueva dirección: ")
                            if len(nueva_direccion) > 60:
                                print("La dirección es demasiado larga. Debe tener como máximo 60 caracteres.")
                                continue  # Vuelve a pedir la dirección
                            contacto['direccion'] = nueva_direccion
                            break
                    elif opcion == '4':
                        while True:
                            nuevo_correo = input("Ingrese el nuevo correo electrónico: ")
                            if len(nuevo_correo) > 50:
                                print("El correo electrónico es demasiado largo. Debe tener como máximo 50 caracteres.")
                                continue  # Vuelve a pedir el correo
                            if not validar_correo(nuevo_correo):
                                print("El correo electrónico no tiene un formato válido.")
                                continue  # Vuelve a pedir el correo
                            contacto['correo'] = nuevo_correo
                            break
                    else:
                        print("Opción no válida.")
                        continue  # Vuelve a pedir la opción
                
                    print("Contacto modificado exitosamente.")
                    return
            print("No se encontró el contacto con ese nombre.")
            break
        
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

# Función para eliminar un contacto
def eliminar_contacto():
    while True:
        try:
            nombre_buscar = input("Ingrese el nombre del contacto que desea eliminar: ")
            for contacto in contactos:
                if contacto['nombre'].lower() == nombre_buscar.lower():
                    contactos.remove(contacto)
                    print("Contacto eliminado exitosamente.")
                    return
            print("No se encontró el contacto con ese nombre.")
            break
        
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

# Función para listar los contactos
def listar_contactos():
    try:
        if not contactos:
            print("No hay contactos registrados.")
        else:
            for contacto in contactos:
                print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Dirección: {contacto['direccion']}, Correo: {contacto['correo']}")
    
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

# Función para buscar un contacto
def buscar_contacto():
    while True:
        try:
            print("Seleccione el criterio de búsqueda:")
            print("1. Buscar por nombre")
            print("2. Buscar por teléfono")
            print("3. Buscar por dirección")
            print("4. Buscar por correo electrónico")
            
            opcion = input("Seleccione la opción que desea: ")
            
            if opcion == '1':
                nombre_buscar = input("Ingrese el nombre del contacto: ")
                for contacto in contactos:
                    if contacto['nombre'].lower() == nombre_buscar.lower():
                        print(f"Contacto encontrado: {contacto}")
                        break
                else:
                    print("No se encontró el contacto con ese nombre.")
                    break
            
            elif opcion == '2':
                telefono_buscar = input("Ingrese el teléfono del contacto: ")
                for contacto in contactos:
                    if contacto['telefono'] == telefono_buscar:
                        print(f"Contacto encontrado: {contacto}")
                        break
                else:
                    print("No se encontró el contacto con ese teléfono.")
                    break
            
            elif opcion == '3':
                direccion_buscar = input("Ingrese la dirección del contacto: ")
                for contacto in contactos:
                    if direccion_buscar.lower() in contacto['direccion'].lower():
                        print(f"Contacto encontrado: {contacto}")
                        break
                else:
                    print("No se encontró el contacto con esa dirección.")
                    break
            
            elif opcion == '4':
                correo_buscar = input("Ingrese el correo electrónico del contacto: ")
                for contacto in contactos:
                    if contacto['correo'].lower() == correo_buscar.lower():
                        print(f"Contacto encontrado: {contacto}")
                        break
                else:
                    print("No se encontró el contacto con ese correo electrónico.")
                    break
            
            else:
                print("Opción no válida.")
                continue  # Vuelve a pedir la entrada si la opción no es válida
            
            break  # Sale del bucle después de una búsqueda exitosa
        
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            continue  # Vuelve a pedir la entrada si ocurre un error

# Menú principal
def menu():
    while True:
        try:
            print("\nMENU SISTEMA DE GESTION DE CONTACTOS")
            print("1. Crear Contacto")
            print("2. Modificar Contactos")
            print("3. Eliminar Contactos")
            print("4. Listar Contactos")
            print("5. Buscar Contactos")
            print("6. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                crear_contacto()
            elif opcion == '2':
                modificar_contacto()
            elif opcion == '3':
                eliminar_contacto()
            elif opcion == '4':
                listar_contactos()
            elif opcion == '5':
                buscar_contacto()
            elif opcion == '6':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        
        except Exception as e:
            print(f"Ha ocurrido un error en el menú: {e}")

# Iniciar el menú
if __name__ == "__main__":
    menu()
