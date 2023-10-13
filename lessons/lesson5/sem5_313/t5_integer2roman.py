"""
Задача 5: Перовод из десятичной системы в Римскую

Римская система записи чисел использует следующие 7 символов: 'I', 'V', 'X', 'L', 'C', 'D' и 'M'.

Символ | Значение
I      |   1
V      |   5
X      |   10
L      |   50
C      |   100
D      |   500
M      |   1000

Например, число 2 в Римской системе записывается как 'II',
просто приписывание двух единиц рядом.
Число 12 записывается как 'XII'. Другими словами это 'X' + 'II'.
Число 27 записывается как 'XXVII', что предстваляется как 'XX' + 'V' + 'II'.

Римские цифры обычно пишутся от наибольшего к наименьшему слева направо.
Однако число 4 это НЕ 'IIII'. Вместо этого число 4 записывается как 'IV'.
Поскольку меньшее число стоит перед большим (единица перед пятью), 
мы вычитаем 1 и получаем 4.
Аналогичный принцип применяется для числа 9, которое пишется так: 'IX'.
Существует 6 ситуаций, где используется такое вычитание:
    1) IV = 4, IX = 9
    2) XL = 40, XC = 90
    3) CD = 400, CM = 900

Ваша задача перевести десятичное число в Римскую систему записи
"""


def intToRoman(num: int) -> str:
    
    thousands=(num//1000)
    five_hundred=(num//500-2*thousands)
    hundreds= num//100 -thousands*10-five_hundred*5
    fifty=(num%100)//50
    tens=(num%100)//10 - fifty*5
    fives=(num%10)//5
    ones=(num%10)-5*fives

    stroka_num = "M"*thousands+"D"*five_hundred+"C"*hundreds+"L"*fifty+"X"*tens+"V"*fives+"I"*ones
    
    stroka_num=stroka_num.replace("DCCCC","CM").replace("LXXXX","XC").replace("VIIII","IX").replace("CCCC","CD").replace("XXXX","XL").replace("IIII","IV")

    return(stroka_num)


if __name__ == "__main__":
    assert intToRoman(3) == "III"
    assert intToRoman(58) == "LVIII"
    assert intToRoman(1994) == "MCMXCIV"