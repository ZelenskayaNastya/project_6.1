def _amount(x, y):
    """Среднее арифметрическое чисел"""
    amount = x / y
    return amount


def main():
    input_file = input('Введите название файла: ')
    try:
        with open(input_file, 'r') as f_in:
            t = f_in.read()
            r = t.split()
            try:
                for i in range(len(r)):
                    r[i] = int(r[i])
                my_sum = sum(r)
                quantity = len(r)
                my_amount = int(_amount(my_sum, quantity))
                output_file = open('output.txt', 'w')
                print('Среднее арифметическое значение из файла: ', my_amount, file=output_file)
                output_file.close()
            except ValueError:
                print('Прверьте иходный файл, там должны содержаться только числовые значения.')
    except FileNotFoundError:
        print('Файл "{}\" не найден.'.format(input_file))


if __name__=='__main__':
    main()


