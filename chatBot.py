print("ChatBot Fitness iniciado")

nome = input("Qual seu nome?\n")
print(f"Prazer, {nome}! Vou te ajudar com treino e dieta")

objetivo = input("Qual seu objetivo? (emagrecer/ganhar massa): ").lower()

def responder_treino(obj):
    if obj == "emagrecer":
        return "Recomendo treino com cardio + musculação leve (ex: caminhada + treino ABC)."
    elif obj == "ganhar massa":
        return "Foque em musculação pesada (treino ABC) + progressão de carga."
    else:
        return "Treino básico: musculação 3x por semana + cardio leve."

def responder_dieta(obj):
    if obj == "emagrecer":
        return "Dieta com déficit calórico, proteína alta e menos açúcar."
    elif obj == "ganhar massa":
        return "Dieta com superávit calórico, bastante proteína e carboidrato."
    else:
        return "Tente manter uma alimentação equilibrada com proteínas, carboidratos e gorduras boas."

while True:
    msg = input("\nQuer saber sobre treino, dieta, uma dica ou encerrar chat ?(Digite um por vez)\n").lower()

    if "treino" in msg:
        print("Bot:", responder_treino(objetivo))

    elif "dieta" in msg:
        print("Bot:", responder_dieta(objetivo))

    elif "dica" in msg:
        print("Bot: Beba bastante água, durma bem e mantenha consistência")

    elif "encerrar chat" in msg:
        print("Bot: Encerrando. Bons treinos")
        break

    else:
        print("Bot: Não entendi. Tente falar sobre treino ou dieta")