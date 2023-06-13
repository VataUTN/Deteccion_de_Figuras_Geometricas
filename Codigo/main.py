import Instalador

# Clase Principal.
if __name__ == "__main__":
    # Instalamos las dependencias necesarias (linux):
    Instalador.instalar_dependencias()

    # Importar el módulo PaginaPrincipal:
    import PaginaPrincipal as pag

    # Iniciar la UI:
    app = pag.App()
