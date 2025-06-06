import socket
import psutil
import os
import platform
import time
import urllib.request


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "N/A"


def get_public_ip():
    try:
        return urllib.request.urlopen("https://api.ipify.org").read().decode()
    except Exception:
        return "Unavailable"


def get_cpu_info():
    return {
        "percent_used": psutil.cpu_percent(),
        "temp": get_cpu_temp(),
        "cores": psutil.cpu_count(logical=False),
        "threads": psutil.cpu_count(logical=True),
        "load_avg": (
            os.getloadavg() if hasattr(os, "getloadavg") else ("N/A", "N/A", "N/A")
        ),
    }


def get_cpu_temp():
    try:
        temps = psutil.sensors_temperatures()
        for name in temps:
            for entry in temps[name]:
                if entry.label == "Package id 0" or not entry.label:
                    return entry.current
        return None
    except Exception:
        return None


def get_memory_info():
    mem = psutil.virtual_memory()
    used = mem.total - mem.available
    percent = (used / mem.total) * 100
    return {
        "used_bytes": used,
        "total_bytes": mem.total,
        "available_bytes": mem.available,
        "percent_used": percent,
    }


def get_disk_info():
    disk = psutil.disk_usage("/")
    return {
        "used_bytes": disk.used,
        "total_bytes": disk.total,
        "free_bytes": disk.free,
        "percent_used": disk.percent,
    }


def get_battery_info():
    try:
        battery = psutil.sensors_battery()
        if battery:
            return {
                "percent": battery.percent,
                "plugged": battery.power_plugged,
                "secs_left": battery.secsleft,
            }
        return None
    except Exception:
        return None


def get_uptime():
    try:
        seconds = time.time() - psutil.boot_time()
        mins, secs = divmod(int(seconds), 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        return {"seconds": int(seconds), "formatted": f"{days}d {hours}h {mins}m"}
    except Exception:
        return {"seconds": 0, "formatted": "Unknown"}


def get_network_info():
    return {
        "public_ip": get_public_ip(),
        "private_ip": get_local_ip(),
    }


def get_host_info():
    return {
        "hostname": socket.gethostname(),
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "date": time.strftime("%A, %d %B %Y"),
    }


def get_os_info():
    return {
        "name": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "kernel": platform.uname().release,
    }


def get_system_stats():
    return {
        "host": get_host_info(),
        "os": get_os_info(),
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "battery": get_battery_info(),
        "uptime": get_uptime(),
        "network": get_network_info(),
    }
