import random

def get_bot_response(user_input):
    # Lista de respuestas del bot
    bot_responses = [
        "Hola, ¿en qué puedo ayudarte?",
        "¡Claro, pregúntame lo que necesites!",
        "Lo siento, no puedo responderte en este momento.",
        "No entiendo lo que dices, ¿podrías reformular la pregunta?"
    ]
    # Retorna una respuesta aleatoria del bot
    return random.choice(bot_responses)

# Función para iniciar el chatbot
def run_chatbot():
    print("¡Bienvenido al chatbot!")
    while True:
        user_input = input("Tú: ")
        response = get_bot_response(user_input)
        print("Bot:", response)

# Ejecuta el chatbot
run_chatbot()