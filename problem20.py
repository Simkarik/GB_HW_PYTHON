# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

one_point = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"]
two_point = ["D", "G"]
three_point = ["B", "C", "M", "P"]
four_point = ["F", "H", "V", "W", "Y"]
five_point = ["K"]
six_point = ["J", "X"]
seven_point = ["Q", "Z"]

word = (input('Enter the word: '))
word = word.upper()
score = 0
for i in range(len(word)):
    for t in range(len(one_point)):
        if word[i] == one_point[t]:
            score += 1
    for t in range(len(two_point)):
        if word[i] == two_point[t]:
            score += 2
    for t in range(len(three_point)):
        if word[i] == three_point[t]:
            score += 3
    for t in range(len(four_point)):
        if word[i] == four_point[t]:
            score += 4
    for t in range(len(five_point)):
        if word[i] == five_point[t]:
            score += 5
    for t in range(len(six_point)):
        if word[i] == six_point[t]:
            score += 6
    for t in range(len(seven_point)):
        if word[i] == seven_point[t]:
            score += 7
print(f'This word is worth {score} pints!')