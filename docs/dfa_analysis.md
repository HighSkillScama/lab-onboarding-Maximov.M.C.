# Анализ потоков данных (Def-Use)

**Переменная: log_entry**
- Def: Строка 2 (log_entry = "Start processing")
- Use: Нет (значение перезаписывается на строке 10, поэтому первое присваивание бесполезно)
- Def: Строка 10 (log_entry = "Transaction finished with status: " + status)
- Use: Строка 12 (file.write(log_entry))

**Переменная: status**
- Def: Строка 5 (status = "approved")
- Use: Строка 10 (использование в конкатенации строки), Строка 13 (return status)

**Переменная: balance**
- Def: Строка 6 (balance = get_balance(user_id))
- Use: Строка 7 (new_balance = balance - amount)

**Переменная: new_balance**
- Def: Строка 7 (new_balance = balance - amount)
- Use: Строка 8 (update_balance(user_id, new_balance))

**Переменная: file**
- Def: Строка 11 (file = open("audit_log.txt", "w"))
- Use: Строка 12 (file.write(log_entry))
