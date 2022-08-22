"""
Zaaimplementuj funkcję generującą even_numbers(n: int) zwracającą kolejne liczby parzyste,
nie podzielne przez 3 do wartości maksymalnej, włącznie podanej jako argument
funkcji na przykład:
    - even_numbers(7) powinna zwracać kolejno: [2, 4]
    - even_numbers(15) powinna zwracać kolejno: [2, 4, 8, 10, 14]
"""


def even_numbers(n):
    generator_comprehension = (i for i in range(n + 1) if i % 3 and not i % 2)
    return generator_comprehension