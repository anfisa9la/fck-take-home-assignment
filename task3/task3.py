import os

# Редьюсер, принимающий массив и функцию,
# возвращает аккумулированное значение
def reduce(arr, func):
	x = arr[0]
	for i in arr[1:]:
		x = func(x, i)
	return x

# Функция суммы элементов массива на основе редьюсера
def sum(arr):
	return reduce(arr, lambda x, y: x + y)

# Основная функция
def main(path):

	# Массив исходных файлов
	dir_files = os.listdir(path)
	# Массив касс
	cashes = []

	# Добавляем в массив касс массивы средних значений по кассам
	for c in dir_files:
		cashes.append(
			[float(i) for i in open(path + "/" + c).read().split(" ")]
		)


	# Массив номеров интервалов с максимальной загруженностью
	arr_max = []
	# Максимальная совокупная средняя загруженность по всем кассам
	max_val = 0

	for i in range(16):
		# Совокупная средняя загруженность по всем кассам в период i
		s = sum([c[i] for c in cashes])

		# Если равна максимальной, то добавляем индекс в arr_max
		if s == max_val:
			arr_max.append(i)
		# Если превышает максимум, то обновляем max_val,
		# также обвновляем arr_max
		if s > max_val:
			arr_max = [i]
			max_val = s

	print(arr_max[0] + 1)



if __name__ == "__main__":
	import sys
	main(sys.argv[1])





