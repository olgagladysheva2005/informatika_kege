'''
(Е. Джобс) Дана программа для исполнителя Редактор:
НАЧАЛО
ПОКА нашлось(11)
  заменить(112, 4)
  заменить(113, 2)
  заменить(42, 3)
  заменить(43, 1)
КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой программы к строке вида 1…13…32…2, состоящей из 170 единиц,
100 троек и 7 двоек?
'''
s = 170 * '1' + 100 * '3' + 7 * '2'
while '11' in s:
    s = s.replace('112', '4', 1)
    s = s.replace('113', '2', 1)
    s = s.replace('42', '3', 1)
    s = s.replace('43', '1', 1)
print(s)