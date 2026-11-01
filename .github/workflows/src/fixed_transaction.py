def process_transaction(user_id, amount, db_connection):  # noqa: F841
    # Исправление 1: Инициализация до if
    status = "pending"
    
    if amount > 0:
        status = "approved"
        balance = get_balance(user_id)
        new_balance = balance - amount
        update_balance(user_id, new_balance)
    
    # Исправление 2: Удалено мертвое присваивание log_entry = "Start processing"
    log_entry = "Transaction finished with status: " + status
    
    # Исправление 3: Использование with для автозакрытия файла
    with open("audit_log.txt", "w") as file:
        file.write(log_entry)
        
    return status
