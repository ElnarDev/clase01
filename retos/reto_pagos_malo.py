# Archivo: /opt/workspace/curso01/retos/reto_pagos_malo.py
import os
import logging
from typing import Tuple

# Configuración básica de logging para simular la salida estándar
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


class DatabaseError(Exception):
    """Excepción para errores relacionados con la base de datos."""

    pass


class PaymentError(Exception):
    """Excepción para errores relacionados con el cobro de la tarjeta."""

    pass


class NotificationError(Exception):
    """Excepción para errores relacionados con el envío de notificaciones."""

    pass


def get_database_credentials() -> Tuple[str, str]:
    """
    Obtiene las credenciales de la base de datos de forma segura
    desde las variables de entorno o usa valores predeterminados seguros.
    """
    db_user = os.getenv("DB_USER", "admin")
    db_pass = os.getenv("DB_PASS", "supersecreto123")
    return db_user, db_pass


def connect_to_database() -> None:
    """Simula la conexión a la base de datos."""
    try:
        db_user, _ = get_database_credentials()
        # En una app real, aquí usaríamos db_pass para autenticar la conexión
        logger.info(f"Conectado a db con {db_user}")
    except Exception as e:
        raise DatabaseError("Error al establecer conexión con la base de datos.") from e


def validate_payment_amount(amount: float) -> None:
    """Valida que el monto cumpla con las reglas de negocio."""
    if amount <= 0:
        raise ValueError("El monto del pago debe ser mayor a cero.")
    if amount > 1000:
        raise ValueError("Monto muy alto")


def charge_card(username: str, amount: float) -> None:
    """Simula la transacción de cobro a la tarjeta."""
    try:
        logger.info(f"Cobrando tarjeta de {username}")
    except Exception as e:
        raise PaymentError(f"Fallo al cobrar la tarjeta de {username}.") from e


def send_notification(username: str, amount: float) -> None:
    """Simula el envío de correo de notificación."""
    try:
        logger.info(f"Enviando correo a {username} sobre pago de {int(amount)}")
    except Exception as e:
        raise NotificationError(f"Fallo al enviar el correo a {username}.") from e


def hacer_transaccion(amount: float, username: str, password: str) -> bool:
    """
    Orquesta el proceso de pago aplicando el Principio de Responsabilidad Única (SRP).

    Retorna True si la transacción fue exitosa, False de lo contrario.
    """
    logger.info(f"iniciando el pago de {int(amount)}")

    try:
        # 1. Regla de negocio: Validar el monto del pago
        validate_payment_amount(amount)

        # 2. Persistencia: Conectar a BD
        connect_to_database()

        # 3. Procesamiento de pago: Cobrar tarjeta
        charge_card(username, amount)

        # 4. Notificaciones: Enviar correo informativo
        send_notification(username, amount)

        return True

    except ValueError as e:
        logger.error(f"Error de validación: {e}")
        return False
    except (DatabaseError, PaymentError, NotificationError) as e:
        logger.error(f"Error en la transacción: {e}")
        return False


# Bloque para probar la ejecución
if __name__ == "__main__":
    hacer_transaccion(500.0, "Juan", "123")
