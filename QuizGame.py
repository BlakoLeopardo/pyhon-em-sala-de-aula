questoes = ("Quantos elementos estão na tabela periodica?: ",
            "Qual animal tem os maiores ovos?: ",
            "Qual o gás mais abundande na atmosfera terrestre?: ",
            "Quantos ossos tem no corpo humano?: ",
            "Qual o planeta mais quente do sistema solar?: "
            )
opcoes = (("A. 116", "B. 117", "C. 118", "D. 119"),
          ("A. Baleia", "B. Crocodilo", "C. Elefante", "D. Avestruz"),
          ("A. Nitrogênio", "B. Oxigênio", "C. Dióxido de Carbono", "D. Hidrogênio"),
          ("A. 206", "B. 207", "C. 208", "D. 209"),
          ("A. Mercúrio", "B. Vênus", "C. Terra", "D. Marte")
          )
respostas = ("C", "D", "A", "A", "B")

palpites = []

score = 0
questao_num = 0

for questoes in questoes:
    print("--------------------------------------------------")
    print(questoes)
    for opcoes in opcoes[questao_num]:
        print(opcoes)

    questao_num += 1