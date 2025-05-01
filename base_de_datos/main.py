import sys
from controlador import controlador

if __name__ == "__main__":

    parametros_cmd = 'gui'

    if parametros_cmd == 'gui':
        objeto_contolador_gui = controlador.ControladorGUI()
        objeto_contolador_gui.mainloop()
        sys.exit(0)

    else:
        sys.exit(1)
