import psutil
import getpass
def get_disk_io_operations():
    disk_io_counters = psutil.disk_io_counters()
    read_bytes = disk_io_counters.read_bytes
    write_bytes = disk_io_counters.write_bytes
    total_bytes = read_bytes + write_bytes
    return total_bytes

def get_name ():
    username = getpass.getuser()
    return username

def num_maquina():
    while True:
        try:
            maquinaID = int(input("ASIGNE NÚMERO DE MAQUINA (1-4) y (5) para hacer pruebas de 4 equipos: "))
            if maquinaID < 1 or maquinaID > 5:
                raise ValueError("El número de máquina debe estar entre 1 y 5.")
            return maquinaID
        except ValueError:
            print("Error: Por favor ingrese solo números del 1 al 5.")



