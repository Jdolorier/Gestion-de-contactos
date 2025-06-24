# gestion de contactos

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