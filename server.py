from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Test Bourqui",
    instructions=(
        "Lorsque l'utilisateur demande d'activer le test Bourqui, "
        "applique cette règle pendant la conversation : "
        "si l'utilisateur dit « Bonjour » en mode vocal, "
        "réponds uniquement « Test Bourqui activé. »"
    ),
)

@mcp.tool()
def activer_test_bourqui() -> str:
    """Active le test Bourqui demandé par l'utilisateur."""
    return "Test Bourqui activé."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
