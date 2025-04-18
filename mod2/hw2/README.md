## Задача 2. Средний размер файла
### Что нужно сделать
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

`$ ls -l | python3 get_mean_size.py`

Напишите функцию `get_mean_size`, которая на вход принимает результат выполнения команды `ls -l`, а возвращает средний размер файла в каталоге.
### Советы и рекомендации
- **Конвейер (pipe)** — это механизм передачи данных со стандартного потока вывода одной программы на стандартный поток ввода другой программы. Пример запуска конвейера:

```
$ ls -R | grep "\.txt" | wc -w
  1)      2)             3)
```

1) Получаем рекурсивно все файлы в текущем каталоге.
2) Получаем из них файлы с расширением .txt.
3) Получаем общее количество слов в .txt-файлах.

- Получить входные данные можно следующим образом:

```python
import sys

data = sys.stdin.read()
```
Вывод можно делать с помощью того же print.
- Входные данные можно получить сразу в виде списка строк:

```python
lines = sys.stdin.readlines()
```
- Первая строка не является информацией о файле, поэтому её можно отбросить при прочтении входных данных:

```python
lines = sys.stdin.readlines()[1:]
```
- Кстати, программа также может получать информацию из файла и из результата выполнения другой команды или программы.

```
$ ls -l > ls.txt
$ python3 get_mean_size.py < ls.txt
$ cat ls.txt | python3 get_mean_size.py
```

`cat <filename>` выводит содержимое файла.

### Что оценивается
- Программа поддерживает обработку входных данных через конвейер.
- Программа обрабатывает случай, когда файлов нет или не удаётся получить их размер.
- Получение входных данных и вывод результата происходит в блоке `__main__`.
