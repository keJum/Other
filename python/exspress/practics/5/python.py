temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))
print('Максимальная темпрература :')
print(max(temperatures))
print('Минимальная температура :')
print(min(temperatures));
print('Средняя темпартура :')
sum_temperature = sum(temperatures)
count_temperature = len(temperatures)
print(sum_temperature/count_temperature);

print("Медиан температуры :")
temperatures.sort();
print(temperatures[count_temperature%2])

print("Количество уникальных значений")
unique_list = set(temperatures)

print(len(unique_list))
