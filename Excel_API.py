import xlsxwriter
import datetime

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('balances.xlsx')
worksheet = workbook.add_worksheet()

# Формат отображения данных в ячейке
money = workbook.add_format({'num_format': '#,##0.00 р"."'})
date_format = workbook.add_format({'num_format': 'd mmmm yyyy'})

# Формат ширины колонки (первая колонка, последняя колонка, ширина)
worksheet.set_column(1, 10, 20)

# Календарь
date = datetime.date.today()
print(date)

# Ввод данных с клавиатуры
expenses = str(input("Введите данные ЧЕРЕЗ ПРОБЕЛ БЕЗ ЗНАКОВ ПРЕПИНАНИЯ: "))

# Создание удобной для сохранение конструкции
expenses = expenses.split()
expenses1 = expenses[::2]
expenses2 = expenses[1::2]
expenses2_temp = ['Этого не должно тут быть aka сбой в перенятии данных']
expenses2_temp.pop()
for number in expenses2:
	expenses2_temp.append(float(number))
expenses2 = expenses2_temp
expenses = tuple(map(list, zip(expenses1, expenses2)))

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Заполнить дату для трат
worksheet.write_datetime(row, col + 1, date, date_format)

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row + 1, col, item)
    worksheet.write(row + 1, col + 1, cost, money)
    row += 1

# check
print(expenses)

'''# Write a total using a formula.
# worksheet.write(row, 0, 'Total')
# worksheet.write(row, 1, '=SUM(B1:B4)')'''

workbook.close()
