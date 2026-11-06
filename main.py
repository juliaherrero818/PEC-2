from app import operaciones

from colorama import Fore, Back, Style, init

init(autoreset = True)

while True:
    print('')
    print("\033[0;37m  \033[0;97m██████\033[0;37m   \033[0;97m██████\033[0;37m  \033[0;97m██████\033[0;37m  \033[0;97m████████\033[0;37m  \033[0;97m██████\033[0;37m  \033[0;97m██████\033[0;37m      \033[0;97m██████\033[0;37m  \033[0;97m██████\033[0;37m      \033[0;97m████████\033[0;37m  \033[0;97m██████\033[0;37m  \033[0;97m██████\033[0;37m  \033[0;97m██████\033[0;37m  \033[0;97m██████\033[0;37m  \033[0;97m██████\033[0m")
    print("\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;94;44m▄ \033[0;97m█\033[0;94m██\033[0;94;44m \033[0;97m███\033[0;94;44m▄ \033[0;97m█\033[0;94m█\033[0;94;44m \033[0;97m██\033[0;94;44m▄▄▄\033[0;94m██\033[0;94;44m \033[0;97m█\033[0;94;44m▄ \033[0;97m██\033[0;94;44m▄ \033[0;97m█\033[0;94m█\033[0;34m█\033[0;97m██\033[0;94;44m▄\033[0;34m█\033[0;97m██\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;94;44m▄ \033[0;97m█\033[0;37m    \033[0;94m█\033[0;34m█\033[0;97m███\033[0;94;44m▄\033[0;34m█\033[0;97m█\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;94;44m▄ \033[0;97m█\033[0;37m    \033[0;94m█\033[0;94;44m \033[0;97m█\033[0;94;44m▄ \033[0;97m██\033[0;94;44m▄ \033[0;97m█\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;94;44m▄ \033[0;97m█\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;94;44m▄ \033[0;97m█\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;94;44m▄ \033[0;97m█\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;94;44m▄ \033[0;97m█\033[0;94m█\033[0;94;44m \033[0;97m██\033[0;94;44m▄▄▄\033[0;94m█\033[0m")
    print("\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;94;44m███\033[0;94m██\033[0;94;44m \033[0;97m████\033[0;94;44m▄█\033[0;94m█\033[0;94;44m \033[0;97m██████\033[0;94m█\033[0;94;44m▄█\033[0;94m█\033[0;94;44m \033[0;97m██\033[0;94m█\033[0;94;44m▄\033[0;94m██\033[0;34m█\033[0;97m██\033[0;94m█\033[0;34m█\033[0;97m██\033[0;94m█\033[0;94;44m \033[0;97m██████\033[0;37m    \033[0;94m█\033[0;34m█\033[0;97m███\033[0;94m█\033[0;34m█\033[0;97m█\033[0;94m█\033[0;94;44m \033[0;97m████\033[0;94;44m▄█\033[0;37m    \033[0;94m█\033[0;94;44m▄█\033[0;94m█\033[0;94;44m \033[0;97m██\033[0;94m█\033[0;94;44m▄\033[0;94m██\033[0;94;44m \033[0;97m██████\033[0;94m█\033[0;94;44m \033[0;97m██████\033[0;94m█\033[0;94;44m \033[0;97m████\033[0;94;44m▄█\033[0;94m█\033[0;94;44m \033[0;97m██████\033[0;94m█\033[0;94;44m \033[0;97m██████\033[0m")
    print("\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;94;44m█\033[0;97m███\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;94;44m█▀\033[0;97m█\033[0;94m█\033[0;94;44m▄▄▄▄▄ \033[0;97m█\033[0;94m████\033[0;94;44m \033[0;97m██\033[0;94m████\033[0;34m█\033[0;97m██\033[0;94m█\033[0;34m█\033[0;97m██\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;34m█\033[0;97m█\033[0;94m█\033[0;37m    \033[0;94m█\033[0;34m█\033[0;97m███\033[0;94m█\033[0;34m█\033[0;97m█\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;94;44m█▀\033[0;97m█\033[0;37m    \033[0;94m████\033[0;94;44m \033[0;97m██\033[0;94m████\033[0;94;44m \033[0;97m███\033[0;94;44m▄ \033[0;97m█\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;34m█\033[0;97m█\033[0;94m██\033[0;94;44m \033[0;97m███\033[0;94;44m█▀\033[0;97m█\033[0;94m█\033[0;94;44m \033[0;97m███\033[0;94;44m▄ \033[0;97m█\033[0;94m█\033[0;94;44m▄▄▄▄▄ \033[0;97m█\033[0m")
    print("\033[0;95;45m█ \033[0;97m██████\033[0;95;45m██ \033[0;97m██████\033[0;95;45m█ \033[0;97m██████\033[0;95;45m████ \033[0;97m██\033[0;95;45m████ \033[0;97m██████\033[0;95;45m█ \033[0;97m███\033[0;97;45m \033[0;97m██\033[0;37m    \033[0;95;45m█ \033[0;97m██████\033[0;95;45m█ \033[0;97m██████\033[0;37m    \033[0;95;45m████ \033[0;97m██\033[0;95;45m████ \033[0;97m███\033[0;95;45m█ \033[0;97m█\033[0;95;45m█ \033[0;97m███\033[0;97;45m \033[0;97m██\033[0;95;45m█ \033[0;97m██████\033[0;95;45m█ \033[0;97m███\033[0;95;45m█ \033[0;97m█\033[0;95;45m█ \033[0;97m██████\033[0m")
    print("\033[0;95;45m█▄▄▄▄▄▄███▄▄▄▄▄▄██▄▄▄▄▄▄█████▄▄█████▄▄▄▄▄▄██▄▄▄█▄▄█\033[0;37m    \033[0;95;45m█▄▄▄▄▄▄██▄▄▄▄▄▄█\033[0;37m    \033[0;95;45m████▄▄█████▄▄▄██ \033[0;97m█\033[0;95;45m█▄▄▄█▄▄██▄▄▄▄▄▄██▄▄▄██ \033[0;97m█\033[0;95;45m█▄▄▄▄▄▄█\033[0m")
    print("\033[0;95;45m███████████████████████████████████████████████████\033[0;37m    \033[0;95;45m████████████████\033[0;37m    \033[0;95;45m████████████████▄███████████████████████▄█████████\033[0m")

    print('')
    print(Back.WHITE + Fore.BLUE + Style.BRIGHT + '¡Bienvenido/a a tu gestor de tareas!')
    print('')
    print(Fore.CYAN + '1. Añadir tarea')
    print(Fore.GREEN + '2. Ver lista completa de tareas pendientes')
    print(Fore.MAGENTA + '3. Buscar tarea específica')
    print(Fore.YELLOW + '4. Salir del programa')
    print('')

    try:
        opcion = int(input(Fore.BLUE + 'Seleccione una opción (1, 2, 3 o 4): '))
        print('')

    except ValueError:
        print(Fore.RED + 'Error. Introduce una opcion valida (numero de la opcion)')
        print('')
        input('Pulsa ENTER para volver al menú principal')  
        continue


    if opcion == 1:
        while True:
            pregunta_tarea = input(Fore.CYAN + 'Introduce la tarea que desea añadir: ')
            if pregunta_tarea.strip() == '':
                print(Fore.RED + 'Error. La tarea debe tener un nombre')
                print('')
                continue

            pregunta_prioridad = input(Fore.CYAN + 'Introduce la prioridad de la tarea (opcional): ')
            pregunt_fecha_limite = input(Fore.CYAN + 'Introduce la fecha límite de la tarea (opcional): ')
            pregunta_etiqueta = input(Fore.CYAN + 'Introduce la etiqueta de la tarea (opcional): ')

            datos_opcionales = {}
            datos_opcionales['prioridad'] = pregunta_prioridad
            datos_opcionales['fecha_limite'] = pregunt_fecha_limite
            datos_opcionales['etiqueta'] = pregunta_etiqueta

            operaciones.añadir_tarea(pregunta_tarea, **datos_opcionales)
            
            print('')
            print(Back.GREEN + Style.BRIGHT + '¡Tarea añadida correctamente!')
            print('')

            mas_tareas = input(Fore.YELLOW + Style.BRIGHT + '¿Deseas añadir otra tarea (s/n)? ').lower()
            print('')

            if mas_tareas != 's' and mas_tareas != 'si':
                break

        input(Back.WHITE + Fore.BLACK + Style.BRIGHT + 'Pulsa ENTER para volver al menú principal')
    

    elif opcion == 2:
        lista_tareas = operaciones.mostrar_lista()
        print('')
        
        if not lista_tareas:
            print(Fore.GREEN + 'No hay tareas pendientes')
        
        else:
            print(Back.GREEN + Style.BRIGHT + 'Lista de tareas pendientes:')
            print('---------------------------')
            for elemento in lista_tareas:
                print(Back.GREEN + Fore.WHITE + '--TAREA--')
                print(Fore.GREEN + 'Nombre: ', elemento.nombre)
                print(Fore.GREEN + 'Prioridad: ', elemento.prioridad if elemento.prioridad else 'No especificada')
                print(Fore.GREEN + 'Fecha límite: ', elemento.fecha_limite if elemento.fecha_limite else 'No especificada')
                print(Fore.GREEN + 'Etiqueta: ', elemento.etiqueta if elemento.etiqueta else 'No especificada')
                print('---------------------------')

        input('Pulsa ENTER para volver al menú principal')

    

    elif opcion == 3:
        busca_tarea = input(Fore.MAGENTA + 'Introduzca la tarea que desea buscar: ')
        resultado = operaciones.buscar_tarea(busca_tarea)
        print('')
        
        if resultado is not None:
            print(Back.MAGENTA + Fore.WHITE + '--TAREA--')
            print('---------------------------')
            print(Fore.MAGENTA + 'Nombre: ', resultado.nombre)
            print(Fore.MAGENTA + 'Prioridad: ', resultado.prioridad if resultado.prioridad else 'No especificada')
            print(Fore.MAGENTA + 'Fecha límite: ', resultado.fecha_limite if resultado.fecha_limite else 'No especificada')
            print(Fore.MAGENTA + 'Etiqueta: ', resultado.etiqueta if resultado.etiqueta else 'No especificada')
            print('---------------------------')

        else:
            print('')
            print(Fore.RED + Style.BRIGHT + 'Tarea no encontrada') 
            print('')

        input('Pulsa ENTER para volver al menú principal')

    
    elif opcion == 4:
        print(Fore.GREEN + Style.BRIGHT + 'Se ha cerrado el programa correctamente')
        print('')
        break
    

    else:
        print(Fore.RED + Style.BRIGHT + 'Opcion no encontrada. Introduce una opcion valida')
        print('')
        input('Pulsa ENTER para volver al menú principal')





     