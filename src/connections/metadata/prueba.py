import psutil

def get_disk_io_operations():
    disk_io_counters = psutil.disk_io_counters()
    read_bytes = disk_io_counters.read_bytes
    write_bytes = disk_io_counters.write_bytes
    total_bytes = read_bytes + write_bytes
    
  
    
    return total_bytes

