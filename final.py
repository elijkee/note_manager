user_name=input("Введите имя пользователя")
print("Имя пользователя:", user_name)
title1=input("Введите заголовок заметки:")
title2=input("Персонажи")
title3=input("Рекомендации для чтения")
title4=input("Основные темы")
all_titles=[title1,title2,title3,title4]
print("заголовок заметки:",all_titles)
content=input("Введите описание заметки")
print("описание заметки:", content)
status=input("Введите статус заметки")
print("статус заметки:", status)
created_date=input("Введите дату создания заметки в формате 'день-месяц-год")
print(created_date[0:5])
issue_date=input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год"')
print( issue_date[0:5])
note1={"имя пользователя":user_name,"заголовок заметки":all_titles,"описание заметки":content,"статус заметки":status,"Дата создания заметки":created_date,"дата истечения заметки":issue_date}
print(note1.values())