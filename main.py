herois = [
    ["Carlos", 800],
    ["Ricardo", 1300],
    ["Maria", 4000],
    ["João", 5500],
    ["José", 7100],
    ["Jorge", 8400],
    ["Hélio", 9050],
    ["Mácio", 50000]
]

for heroi in herois:
    if heroi[1] < 1000:
        nivel = "Ferro"
    elif heroi[1] < 2000:
        nivel = "Bronze"
    elif heroi[1] < 5000:
        nivel = "Prata"
    elif heroi[1] < 7000:
        nivel = "Ouro"
    elif heroi[1] < 8000:
        nivel = "Platina"
    elif heroi[1] < 9000:
        nivel = "Ascendente"
    elif heroi[1] < 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"

    print(f"O Herói de nome **{heroi[0]}** está no nível de **{nivel}**")