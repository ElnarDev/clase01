# Archivo: /opt/workspace/curso01/retos/reto_descuentos_malo.py

def calcular(precio: float, tipo: str) -> float:
    """
    Calcula el precio final aplicando descuentos según el tipo de cliente.
    
    Aplica el patrón de Cláusulas de Guarda (Early Return) para eliminar
    por completo los niveles de anidamiento de condicionales.
    
    Parámetros:
        precio (float): El precio base a evaluar.
        tipo (str): El tipo de cliente ('VIP', 'Normal').
        
    Retorna:
        float: El precio calculado tras aplicar las reglas de descuento:
               - 0 si el precio es menor o igual a 0.
               - -1 si el tipo de cliente no es reconocido.
               - Precio con 20% de descuento si es VIP y precio > 500.
               - Precio con 10% de descuento si es VIP y precio <= 500.
               - Precio completo si es cliente Normal.
    """
    # 1. Cláusula de guarda: Validar precio
    if precio <= 0:
        return 0.0

    # 2. Cláusula de guarda: Validar tipo de cliente conocido
    if tipo not in ("VIP", "Normal"):
        return -1.0

    # 3. Regla de negocio para VIP
    if tipo == "VIP":
        if precio > 500:
            return precio * 0.8
        return precio * 0.9

    # 4. Regla de negocio para clientes Normales
    return precio


if __name__ == "__main__":
    print(f"Descuento VIP (600): {calcular(600, 'VIP')}")
    print(f"Descuento VIP (400): {calcular(400, 'VIP')}")
    print(f"Cliente Normal (300): {calcular(300, 'Normal')}")
    print(f"Tipo Inválido (300): {calcular(300, 'Otro')}")
    print(f"Precio Inválido (-50): {calcular(-50, 'VIP')}")
