"""
20. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas
tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos.
"""

euros2 = int(input('¿Cuánto dinero tienes en monedas de 2 euros?: '))
euros1 = int(input('¿Cuánto dinero tienes en monedas de 1 euro?: '))
cent50 = int(input('¿Cuánto dinero tienes en monedas de 50 centimos?: '))
cent20 = int(input('¿Cuánto dinero tienes en monedas de 20 centimos: '))
cent10 = int(input('¿Cuánto dinero tienes en monedas de 10 centimos: '))

centimos = (euros2 * 200) + (euros1 * 100) + (cent50 * 50) + (cent20 * 20) + (cent10 * 10)
euros = centimos / 100

print(f'El dinero total que tienes es de: {euros} €')
