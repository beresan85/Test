"""
Servidor MCP mínimo (sin base de datos).

Local:   pip install "mcp[cli]"  y luego  python server.py
Endpoint: http://localhost:8000/mcp
"""
import os

from mcp.server.fastmcp import FastMCP

# PORT lo define el hosting; en local usa 8000
mcp = FastMCP("servidor-prueba", host="0.0.0.0", port=int(os.getenv("PORT", "8000")))


@mcp.tool()
def saludar(nombre: str) -> str:
    """Saluda a una persona por su nombre."""
    return f"¡Hola, {nombre}! Tu servidor MCP está funcionando."


@mcp.tool()
def sumar(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
