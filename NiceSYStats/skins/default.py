from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from datetime import datetime


def render(stats):
    now = datetime.now().strftime("%A %d %b %Y %H:%M:%S")

    body = Text()
    body.append(f"🖥️ Hostname: ", style="bold cyan")
    body.append(f"{stats['hostname']}\n\n")

    body.append(f"🧠 CPU Usage: ", style="bold green")
    body.append(f"{stats['cpu_percent']}%\n")

    mem = stats["memory"]
    body.append(f"💾 Memory Usage: ", style="bold yellow")
    body.append(
        f"{mem['percent_used']:.1f}% used ({mem['used_bytes'] // (1024**2)}MB / {mem['total_bytes'] // (1024**2)}MB)\n"
    )

    disk = stats["disk"]
    body.append(f"🗄️ Disk Usage: ", style="bold magenta")
    body.append(
        f"{disk.percent}% used ({disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB)\n\n"
    )

    body.append(f"🌍 Public IP: ", style="bold blue")
    body.append(f"{stats['public_ip']}\n")

    body.append(f"📡 Local IP: ", style="bold blue")
    body.append(f"{stats['local_ip']}\n\n")

    body.append(f"⏳ Uptime: ", style="bold white")
    body.append(f"{stats['uptime']}\n")

    temp = stats.get("cpu_temp", "N/A")
    body.append(f"🌡️ CPU Temp: ", style="bold red")
    body.append(f"{temp}\n")

    return Panel(
        Align.center(body, vertical="middle"),
        title=f"System Monitor — {now}",
        border_style="bright_blue",
        padding=(1, 2),
    )
