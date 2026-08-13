# Archivo: /opt/workspace/curso01/retos/reto_usuarios_limpio.py
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def validar_email(email: str) -> bool:
    if "@" not in email:
        logger.warning(f"Validación fallida: Email inválido ({email})")
        return False
    return True


def guardar_usuario(nombre: str, email: str, edad: int) -> bool:
    logger.info(f"Iniciando registro para {nombre}...")

    if not validar_email(email):
        return False

    try:
        if edad < 18:
            logger.warning("El usuario es menor de edad.")
            return False

        logger.info("Usuario guardado en base de datos exitosamente.")
        return True
    except TypeError as e:
        logger.error(
            f"Error crítico de tipos: La edad debe ser un número entero. Detalle: {e}"
        )
        return False


if __name__ == "__main__":
    # La aplicación ya no explota, el error se intercepta elegante y estructuradamente
    guardar_usuario("Ana", "ana@mail.com", "veinte")  # type: ignore
