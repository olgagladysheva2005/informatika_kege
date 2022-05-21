'''
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди,
первый ход делает Петя. За один ход игрок может добавить в кучу один камень или увеличить количество камней
в куче в два раза. Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней.
Игра завершается в тот момент, когда количество камней в куче становится не менее 29. Победителем считается игрок, сделавший последний ход, т.е. первым получивший кучу, в которой будет 29 или больше камней.
В начальный момент в куче было S камней, 1 ≤ S ≤ 28.
Задание 19.
Укажите такое значение S, при котором Петя не может выиграть за один ход, но при любом ходе Пети Ваня может выиграть своим первым ходом.
Задание 20.
Найдите два таких значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.
Задание 21
Найдите значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
'''
def game(s):
    if s >= 29:
        return 0
    nextstep = [game(s + 1), game(s * 2)]
    lose = [x for x in nextstep if x <= 0]
    if lose:
        result = -max(lose) + 1
    else:
        result = -max(nextstep)
    return result
results = [(s, game(s)) for s in range(1, 29)]
print([s for s, p in results if p == -1])
print([s for s, p in results if p == 2])
print([s for s, p in results if p == -2])


