# Archivo: reto_pagos_limpio.py
import os
import logging
from typing import Optional

# 1. Configuración de Logging Profesional
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# 2. Responsabilidad Única: Notificaciones
def enviar_recibo_correo(usuario: str, monto: float) -> None:
    logger.info(f"Simulando envío de recibo a {usuario} por el monto de ${monto}")


# 3. Responsabilidad Única: Lógica de Reglas de Negocio
def validar_monto(monto: float) -> bool:
    MONTO_MAXIMO = 1000.0
    if monto > MONTO_MAXIMO:
        logger.warning(
            f"Intento de transacción rechazado: Monto {monto} excede el límite de {MONTO_MAXIMO}"
        )
        return False
    return True


# 4. Responsabilidad Única: Orquestador Principal (Controlador)
def procesar_transaccion_segura(monto: float, usuario: str) -> bool:
    logger.info(f"Iniciando transacción para {usuario}...")

    if not validar_monto(monto):
        return False

    # Seguridad: Lectura desde .env
    db_password = os.getenv("DB_PASSWORD")
    if not db_password:
        logger.critical(
            "Error Crítico: DB_PASSWORD no se encontró en las variables de entorno."
        )
        # Evitamos crashear, devolvemos False para que la UI sepa que falló.
        return False

    try:
        # Simulamos la operación de cobro en BD
        logger.info(f"Cobrando a la tarjeta de {usuario}...")
        enviar_recibo_correo(usuario, monto)
        logger.info("Transacción finalizada con éxito.")
        return True
    except Exception as error:
        # Resiliencia: Intercepción del fallo
        logger.error(f"La base de datos rechazó la operación: {str(error)}")
        return False


# Bloque de ejecución principal
if __name__ == "__main__":
    # La librería dotenv lee el archivo .env y carga las variables al sistema
    from dotenv import load_dotenv

    load_dotenv()

    procesar_transaccion_segura(500, "Juan")
