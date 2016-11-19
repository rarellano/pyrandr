# pyrandr
Es un pequeño script que hace uso de xrandr para cambiar la configuración de 2 pantallas.
Está pensado para ser un shortcut y no tener que abrir aplicaciones mas complejas como por ejemplo: arandr u otras. 

Esta aplicación depende de xrandr que viene instalada por defecto en la mayoría de las distribuciones GNU/Linux.

# Uso (Dos pantallas):
  Cada vez que se ejecute cambiará de estado. El Estado será ciclico cada nuevo encendido, empezando por la configuración 0.
  
    Conf 0:  Pantalla A (Encendida) y Pantalla B (Apagada).
    Conf 1:  Pantalla B (Encendida) y Pantalla A (Apagada).
    Conf 2:  Escritorio extendido Pantalla A a la izquierda de la Pantalla B.
    Conf 3:  Escritorio extendido Pantalla A a la derecha de la Pantalla B.
    Conf 4:  Pantalla B clondada de la Pantalla A.

# Uso de fichero de configuración externo
	Crear un fichero con el nombre pyrandr en /home/usuario/.config/, quedaría como /home/usuario/.config/pyrandr
	Cada configuración deberá ir en una linea diferente. 
	La configuración será el comando xrandr necesario, salvo que llamaremos a las pantallas {a} y {b} para tener una configuración genérica. 

	Ejemplo de fichero de configuración:
		xrandr --output {b} --off --output {a} --auto
		xrandr --output {a} --off --output {b} --auto
		xrandr --output {a} --auto --output {b} --same-as {a}

