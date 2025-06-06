from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from rich.console import Group


def render(stats):
    mem = stats["memory"]
    cpu = stats["cpu"]
    host = stats["host"]
    network = stats["network"]
    uptime = stats["uptime"]

    def centered(text, style=""):
        return Align.center(Text(text, style=style))

    title = centered("⟡ SYSTEM STATUS ⟡", style="bold magenta")

    sections = []

    sections.append(centered("╾─── SYSTEM ───╼", style="bold cyan"))
    sections.append(centered(f"Host: {host['hostname']}", style="cyan"))
    sections.append(centered(f"Public IP: {network['public_ip']}", style="cyan"))
    sections.append(centered(f"Local IP: {network['private_ip']}", style="cyan"))
    sections.append(centered(f"Uptime: {uptime}", style="cyan"))

    sections.append(centered("╾─── TIME ───╼", style="bold green"))
    sections.append(centered(f"{host['date']}", style="green"))
    sections.append(centered(f"{host['time']}", style="green"))

    sections.append(centered("╾─── CPU ───╼", style="bold yellow"))
    sections.append(centered(f"Usage: {cpu['percent_used']}%", style="yellow"))

    sections.append(centered("╾─── MEMORY ───╼", style="bold red"))
    sections.append(centered(f"{mem['percent_used']:.1f}% used", style="red"))
    sections.append(
        centered(
            f"{mem['used_bytes'] // (1024**2)}MB / {mem['total_bytes'] // (1024**2)}MB",
            style="red",
        )
    )

    layout = Group(title, *sections)
    return Panel(layout, border_style="bold white")
