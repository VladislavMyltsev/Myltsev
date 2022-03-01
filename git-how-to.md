Создание ssh ключа:
	Терминал: ssh-keygen -t "keyname" -C "email"
Добавление ключа в Github:
	GitHub: Репозиторий -> Settings -> Deploy keys (Сюда вписать публичный)
	Терминал: ssh-add path (Путь до приватного ключа)
Склонировать репозиторий:
	Терминал: git clone (SSH ссылка на репозиторий)
