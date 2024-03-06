palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for vogal in palavras:
    print(f'\nNa palavra {vogal} temos ', end='')
    for letra in vogal:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')