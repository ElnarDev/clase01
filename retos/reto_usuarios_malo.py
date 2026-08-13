# Archivo: /opt/workspace/curso01/retos/reto_usuarios_malo.py
import logging
from typing import Any

# Configuración básica de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """Excepción para representar errores de validación de negocio."""
    pass

def validar_usuario(email: str, age: int) -> None:
    """
    Función encargada exclusivamente de la validación del usuario (SRP).
    Aplica Tipado Fuerte para documentar los tipos esperados.
    """
    # Validación de formato de email simple
    if "@" not in email:
        raise ValidationError("Email inválido (falta '@')")
    
    # Esta línea provocará TypeError en tiempo de ejecución si 'age' no es comparable con int
    if age < 18:
        raise ValidationError("El usuario es menor de edad")

def guardar_user(name: str, email: str, age: int) -> bool:
    """
    Orquesta el proceso de guardado y manejo de errores para el usuario.
    """
    logger.info("Guardando usuario...")
    
    try:
        # Validación externa aplicando SRP
        validar_usuario(email, age)
        
        # Simulación de guardado
        logger.info("Usuario guardado exitosamente")
        return True
        
    except TypeError as e:
        # Captura y logea el error de tipo específico
        logger.error(f"Error de tipo (TypeError) al procesar la edad para '{name}': {e}")
        return False
    except ValidationError as e:
        # Maneja la regla de negocio que falló sin romper la aplicación
        logger.warning(f"Error de validación para '{name}': {e}")
        return False

# Bloque para probar la ejecución
if __name__ == "__main__":
    # Provocará un TypeError capturado correctamente por el bloque try-except
    guardar_user("Ana", "ana@mail.com", "veinte")  # type: ignore
