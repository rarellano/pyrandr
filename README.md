# pyrandr
Es un pequeño script que hace uso de xrandr para cambiar la configuración de 2 pantallas.
Está pensado para ser un shortcut y no tener que abrir aplicaciones mas complejas como por ejemplo: arandr u otras. 

Máximo dos pantallas, en caso de existir mas de dos pantallas, deberá hacerse uso de la opción --exclude.

Si solo encuentra una pantalla, activará esta.

Esta aplicación depende de xrandr que viene instalada por defecto en la mayoría de las distribuciones GNU/Linux.

# Uso (Dos pantallas):
  Cada vez que se ejecute cambiará de estado. El Estado será ciclico cada nuevo encendido, empezando por la configuración 0.
  
    Conf 0:  Pantalla A (Encendida) y Pantalla B (Apagada).
    Conf 1:  Pantalla B (Encendida) y Pantalla A (Apagada).
    Conf 2:  Escritorio extendido Pantalla A a la izquierda de la Pantalla B.
    Conf 3:  Escritorio extendido Pantalla A a la derexha de la Pantalla B.
    Conf 4:  Pantalla B clondada de la Pantalla A.
