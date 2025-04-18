## Person.get_age()
`datetime` используется в методе но не был импортирован. *Решение:* `import datetime` вверху файла.

Возвращает значение обратное возрасту. *Решение:* `datetime.datetime.now().year - self.yob` а не наоборот.

## Person.set_name()
Не меняет имя. *Решение:* `self.name = name` вместо `self.name = self.name`.

## Person.set_address()
Не устанавливает адрес. *Решение:* `self.address = address` вместо `self.address == address`

## Person.is_homeless()
`name 'address' is not defined` *Решение:* `self.address`

Возвращает `False` если не установить адрес т.к. он стандартное значение - `""`, а проверяется на `None`. *Решение:* `== ""` вместо `is None'.
