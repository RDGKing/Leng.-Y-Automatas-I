# Importa el módulo de registro para mostrar mensajes de registro.
import logging
# Importa el módulo de expresiones regulares para trabajar con patrones de texto.
import re

# Importa la clase ForceReply y Update de la biblioteca python-telegram-bot.
from telegram import ForceReply, Update
# Importa varias clases y funciones de la biblioteca python-telegram-bot.
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Habilita el registro para mostrar mensajes de registro con un formato específico y un nivel de importancia.
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
# Establece el nivel de registro para el módulo httpx.
logging.getLogger("httpx").setLevel(logging.WARNING)
# Crea un objeto logger con el nombre del módulo actual.
logger = logging.getLogger(__name__)


# Expresión regular para detectar mensajes que contienen saludos en diferentes idiomas.
expresion_saludo = re.compile(r"hello|hi|hey|hola", re.IGNORECASE)
expresion_despedida = re.compile(r"bye|goodbye|adios|chao", re.IGNORECASE)
patron_origen_destino_fecha = re.compile(
    r"volar de (\w+) a (\w+) el (\d{1,2} de \w+)")
patron_precio = re.compile(r"cuánto cuesta un vuelo de (\w+) a (\w+)")
patron_ida_vuelta = re.compile(r"un vuelo de ida y vuelta de (\w+) a (\w+)")
correo_electronico = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

# Función para manejar el comando /start.


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user  # Obtiene el usuario que envió el mensaje.
    # Responde al usuario saludándolo utilizando su nombre.
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

# Función para manejar el comando /help.


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    # Responde al usuario con un mensaje de ayuda.
    await update.message.reply_text("Help!")


# Función para manejar mensajes de texto.
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message if it matches the regular expression."""

    # Obtiene el texto del mensaje enviado por el usuario.
    message_text = update.message.text
    # Comprueba si el texto del mensaje coincide con la expresión regular para saludos.


# Comprobación de saludos y despedidas
    if expresion_saludo.search(message_text):
        await update.message.reply_text("¡Hola! ¿Cómo estás?")
    elif expresion_despedida.search(message_text):
        await update.message.reply_text("¡Hasta luego! Vuelve pronto.")
    else:
        # Procesar consultas de vuelo
        if patron_origen_destino_fecha.search(message_text):
            origen_destino_fecha = patron_origen_destino_fecha.search(
                message_text)
            origen = origen_destino_fecha.group(1)
            destino = origen_destino_fecha.group(2)
            fecha = origen_destino_fecha.group(3)
            await update.message.reply_text(f"Buscar vuelo de {origen} a {destino} para el {fecha}")
        elif patron_precio.search(message_text):
            precio = patron_precio.search(message_text)
            origen = precio.group(1)
            destino = precio.group(2)
            await update.message.reply_text(f"Consultar precio de vuelo de {origen} a {destino}")
        elif patron_ida_vuelta.search(message_text):
            ida_vuelta = patron_ida_vuelta.search(message_text)
            origen = ida_vuelta.group(1)
            destino = ida_vuelta.group(2)
            await update.message.reply_text(f"Buscar vuelo de ida y vuelta de {origen} a {destino}")
            # Procesar consultas de correo electrónico
        elif correo_electronico.search(message_text):
            direccion = correo_electronico.search(message_text)
            correo = direccion.group(0)
            await update.message.reply_text(f"La expresion {correo} es un correo electronico")
        else:
            await update.message.reply_text("Lo siento, no puedo entender tu consulta.")


# Función principal para iniciar el bot.
def main() -> None:
    """Start the bot."""
    # Crea una instancia de la aplicación del bot utilizando el token de acceso proporcionado por Telegram.
    application = Application.builder().token("TOKEN").build()

    # Agrega manejadores de comandos y mensajes a la aplicación para que el bot pueda responder a diferentes eventos.
    # Agrega un manejador para el comando /start.
    application.add_handler(CommandHandler("start", start))
    # Agrega un manejador para el comando /help.
    application.add_handler(CommandHandler("help", help_command))
    # Agrega un manejador para mensajes de texto.
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, echo))

    # Inicia la aplicación para que empiece a escuchar y procesar los mensajes entrantes del bot.
    application.run_polling(allowed_updates=Update.ALL_TYPES)


# Comprueba si el script se está ejecutando como un programa principal.
if __name__ == "__main__":
    main()  # Si es así, llama a la función main() para iniciar el bot.
