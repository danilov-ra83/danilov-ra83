money = int(input('введите сумму для расчета вклада:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
TKB = int((per_cent['ТКБ']) * (money/100))
SKB = int((per_cent['СКБ']) * (money/100))
VTB = int((per_cent['ВТБ']) * (money/100))
SBER = int((per_cent['СБЕР']) * (money/100))
deposit = {'ТКБ': TKB, 'СКБ': SKB, 'ВТБ': VTB, 'СБЕР': SBER}
print(deposit)
fin_max = max(per_cent.values())
deposit_max = max(deposit.values())
print('максимально выгодная процентная ставка =', fin_max,'%,',
      'доходность:', deposit_max, 'руб.')