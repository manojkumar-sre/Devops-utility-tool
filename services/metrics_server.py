import psutil


def get_system_metrics():
    """
    this API gets the system Metrics(CPU, Memory, Disk, System Health)
    Based on CPU threshold i.e 10 (configurable)

    """
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_usages = psutil.disk_usage("/").percent

    cpu_threshold = 10

    if cpu_percent > cpu_threshold:
         status = "high cpu"
    else:
        status = "healthy"

    return{
        "cpu_percentage":cpu_percent,
        "disk_percentage": disk_usages,
        "memory_percentage": memory_percent,
        "cpu_threshold": cpu_percent,
        "system_status": status,
}

