
import os
from mcp.server.mcpserver import MCPServer

PROMPT = os.environ.get("BOURQUI_PROMPT", "").strip()

mcp = MCPServer(
    "Méthode Bourqui",
    instructions=PROMPT or "Méthode Bourqui en cours de configuration."
)

@mcp.tool()
def demarrer_methode_bourqui() -> str:
    """Active le tutorat oral personnalisé de la Méthode Bourqui."""
    if not PROMPT:
        return "Le programme pédagogique n'est pas encore configuré."
    return "Méthode Bourqui activée. Suis les instructions du serveur."

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "10000"))
    )
