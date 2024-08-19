def send_email(message, recipient, sender="university.help@gmail.com"):
    znaki = ["@", ".com", ".ru", ".net"]
    cnt_rec = sum(list(recipient.count(i) for i in znaki))  # проверка нахождения @ и окончания почты
    cnt_sen = sum(list(sender.count(i) for i in znaki))
    if cnt_rec != 2 or cnt_sen != 2:  # если хоть одна из почт будет указано не правильно сообщение не отправиться
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

message = input("Введите сообщение: ")
recipient = input("Введите почту получателя: ")
if input("Вы хотите изменить отправителя да/нет: ").lower() == "да":
    sender = input("Введите почту отправителя: ")
    send_email(message, recipient, sender)
else:
    send_email(message, recipient)