def tabela (lista=[]):
    janeiro = 'Janeiro'
    fevereiro = 'Favereiro'
    marco = 'Março'
    abril = 'Abril'
    maio = 'Maio'
    junho = 'Junho'
    julho = 'Julho'
    agosto = 'Agosto'
    setembro = 'Setembro'
    outubro = 'Outubro'
    novembro = 'Novembro'
    dezembro = 'Dezembro'
    lista = janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro

    lista.insert (janeiro, '31')
    lista.insert (fevereiro, '28 (ou 29 se ano bissexto)')
    lista.insert (marco, '31')
    lista.insert (abril, '30')
    lista.insert (maio, '31')
    lista.insert (junho, '30')
    lista.insert (julho, '31')
    lista.insert (agosto, '31')
    lista.insert (setembro, '30')
    lista.insert (outubro, '31')
    lista.insert (novembro, '30')
    lista.insert (dezembro, '31')
    print(lista)
    return lista
tabela()
