# Archivo: /opt/workspace/curso01/retos/reto_descuentos_limpio.py
def calcular_descuento(precio: float, tipo_cliente: str) -> float:
    """Calcula el precio final aplicando descuentos según el tipo de cliente."""

    # 1. Cláusulas de guarda (Filtros iniciales rápidos)
    if precio <= 0:
        return 0.0

    if tipo_cliente not in ["VIP", "Normal"]:
        raise ValueError("Tipo de cliente no reconocido")

    if tipo_cliente == "Normal":
        return precio

    # 2. Lógica principal (Llegar aquí significa que superó los filtros)
    if precio > 500:
        return precio * 0.8

    return precio * 0.9


if __name__ == "__main__":
    print(f"Descuento VIP: {calcular_descuento(600, 'VIP')}")
