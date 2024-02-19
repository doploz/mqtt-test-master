import psutil

def obtener_estadisticas_disco():
    particiones = psutil.disk_partitions()
    for particion in particiones:
        print(f"Disco: {particion.device}")
        try:
            uso_disco = psutil.disk_usage(particion.mountpoint)
            print(f"  - Total: {uso_disco.total / (1024 ** 3):.2f} GB")
            print(f"  - Usado: {uso_disco.used / (1024 ** 3):.2f} GB")
            print(f"  - Libre: {uso_disco.free / (1024 ** 3):.2f} GB")
            print(f"  - Porcentaje de uso: {uso_disco.percent}%")
        except PermissionError:
            print("  - Permiso denegado")

if __name__ == "__main__":
    obtener_estadisticas_disco()
