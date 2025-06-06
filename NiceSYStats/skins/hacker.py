from rich.text import Text
from rich.panel import Panel
from rich.align import Align


def render(stats):
    mem = stats["memory"]
    cpu = stats["cpu"]
    host = stats["host"]
    uptime = stats["uptime"]
    network = stats["network"]

    def line(label, value, pad=20):
        return f"{label:<{pad}}: {value}"

    lines = [
        "[bold green]>>> SYSTEM INTERFACE ACTIVE <<<[/bold green]",
        "",
        line("HOSTNAME", host["hostname"]),
        line("PUBLIC IP", network["public_ip"]),
        line("LOCAL IP", network["private_ip"]),
        line("UPTIME", uptime["formatted"]),
        "",
        line("DATE", host["date"]),
        line("TIME", host["time"]),
        "",
        line("CPU USAGE", f"{cpu['percent_used']}%"),
        "",
        line("MEMORY USED", f"{mem['percent_used']:.1f}%"),
        line(
            "MEMORY STATS",
            f"{mem['used_bytes'] // (1024**2)}MB / {mem['total_bytes'] // (1024**2)}MB",
        ),
        "",
        "[green]=============================[/green]",
        "[green] TERMINAL MONITOR ONLINE [/green]",
        "[green]=============================[/green]",
    ]

    text = Text("\n".join(lines), style="green")
    return Panel(Align.left(text), border_style="green", padding=(1, 4))
