
import datetime

class GitLabEmulator:
    def __init__(self):
        self.repo = {
            "name": "my-repo",
            "branches": {
                "master": {
                    "head": "commit1",
                    "commits": {
                        "commit1": {
                            "message": "Initial commit",
                            "author": "John Doe",
                            "date": datetime.datetime.now(),
                            "parent": None,
                        },
                    },
                },
            },
            "remotes": {},
            "tags": {},
        }

    def show_help(self):
        """
        Выводит справку по доступным командам.
        """
        print("Доступные команды:")
        print("help - выводит эту справку.")
        print("git init - инициализирует новый репозиторий Git.")
        print("git add <файл> - добавляет файл в индекс Git.")
        print("git commit -m \"сообщение\" - фиксирует изменения в репозитории.")
        print("git status - показывает текущий статус репозитория.")
        print("git log - показывает историю коммитов.")
        print("git push - отправляет изменения на удаленный сервер.")
        print("git pull - получает изменения с удаленного сервера.")
        print("git branch - показывает список веток.")
        print("git checkout <ветка> - переключается на другую ветку.")
        print("git merge <ветка> - сливает изменения из другой ветки.")
        print("git clone <url> - клонирует репозиторий с удаленного сервера.")
        print("git remote add <имя> <url> - добавляет удаленный репозиторий.")
        print("git remote -v - показывает список удаленных репозиториев.")
        print("git fetch - получает изменения с удаленного сервера, но не сливает их.")
        print("git reset --hard <коммит> - сбрасывает текущую ветку на указанный коммит.")
        print("git revert <коммит> - отменяет изменения из указанного коммита.")
        print("git stash - сохраняет несохраненные изменения.")
        print("git stash pop - восстанавливает сохраненные изменения.")
        print("git tag -a <имя_тега> -m \"сообщение\" - создает тег.")
        print("git tag - показывает список тегов.")
        print("git show <тег> - показывает информацию о теге.")
        print("git diff - показывает различия между файлами.")
        print("git blame <файл> - показывает историю изменений файла.")
        print("clear - очищает терминал")

    def handle_command(self, command):
        """
        Обрабатывает команду пользователя.

        Args:
            command (str): Введенная пользователем команда.
        """
        if command == "help":
            self.show_help()
        elif command == "git init":
            self.init_repo()
        elif command.startswith("git add "):
            self.add_file(command.split(" ")[2])
        elif command.startswith("git commit -m "):
            # Извлекаем сообщение из кавычек, если они есть
            if "\"" in command:
                message = command.split("\"")[1]
            else:
                # Если кавычек нет, выводим ошибку
                print("Ошибка: Отсутствуют кавычки вокруг сообщения коммита.")
                return  # Выходим из функции
            self.commit(message)
        elif command == "git status":
            self.show_status()
        elif command == "git log":
            self.show_log()
        elif command == "git push":
            self.push()
        elif command == "git pull":
            self.pull()
        elif command == "git branch":
            self.show_branches()
        elif command.startswith("git checkout "):
            branch_name = command.split(" ")[2]
            self.checkout(branch_name)
        elif command.startswith("git merge "):
            branch_name = command.split(" ")[2]
            self.merge(branch_name)
        elif command.startswith("git clone "):
            url = command.split(" ")[2]
            self.clone(url)
        elif command.startswith("git remote add "):
            name = command.split(" ")[3]
            url = command.split(" ")[4]
            self.remote_add(name, url)
        elif command == "git remote -v":
            self.show_remotes()
        elif command == "git fetch":
            self.fetch()
        elif command.startswith("git reset --hard "):
            commit = command.split(" ")[3]
            self.reset_hard(commit)
        elif command.startswith("git revert "):
            commit = command.split(" ")[2]
            self.revert(commit)
        elif command == "git stash":
            self.stash()
        elif command == "git stash pop":
            self.stash_pop()
        elif command.startswith("git tag -a "):
            tag_name = command.split(" ")[3]
            self.tag(tag_name)
        elif command == "git tag":
            self.show_tags()
        elif command.startswith("git show "):
            tag_name = command.split(" ")[2]
            self.show_tag(tag_name)
        elif command == "git diff":
            self.show_diff()
        elif command.startswith("git blame "):
            file_name = command.split(" ")[2]
            self.show_blame(file_name)
        elif command == "clear":  # Новая команда!
            print("\n" * 50)  # Печатает 50 пустых строк, чтобы очистить терминал
        else:
            print("Неизвестная команда. Попробуйте 'help' для справки.")

    def init_repo(self):
        print("Репозиторий Git успешно инициализирован!")

    def add_file(self, file_name):
        print(f"Файл '{file_name}' успешно добавлен!")

    def commit(self, message):
        current_branch = "master"  # Предположим, что мы всегда в ветке master
        head_commit = self.repo["branches"][current_branch]["head"]
        new_commit = f"commit{len(self.repo['branches'][current_branch]['commits']) + 1}"
        self.repo["branches"][current_branch]["commits"][new_commit] = {
            "message": message,
            "author": "John Doe",
            "date": datetime.datetime.now(),
            "parent": head_commit,
        }
        self.repo["branches"][current_branch]["head"] = new_commit
        print("Изменения успешно зафиксированы!")

    def show_status(self):
        print("Текущий статус репозитория:")
        print("Ветка: master")
        print("Изменения: нет")

    def show_log(self):
        current_branch = "master"
        head_commit = self.repo["branches"][current_branch]["head"]
        commit = head_commit
        while commit:
            print(f"commit {commit}")
            print(f"Author: {self.repo['branches'][current_branch]['commits'][commit]['author']}")
            print(f"Date:   {self.repo['branches'][current_branch]['commits'][commit]['date']}")
            print(f"    {self.repo['branches'][current_branch]['commits'][commit]['message']}")
            commit = self.repo["branches"][current_branch]["commits"][commit]["parent"]

    def push(self):
        print("Изменения успешно отправлены!")

    def pull(self):
        print("Изменения успешно получены!")

    def show_branches(self):
        print("Список веток:")
        for branch in self.repo["branches"]:
            print(f"* {branch}")

    def checkout(self, branch_name):
        if branch_name in self.repo["branches"]:
            print(f"Успешно переключено на ветку '{branch_name}'!")
        else:
            print(f"Ветка '{branch_name}' не найдена.")

    def merge(self, branch_name):
        if branch_name in self.repo["branches"]:
            print(f"Изменения из ветки '{branch_name}' успешно слиты!")
        else:
            print(f"Ветка '{branch_name}' не найдена.")

    def clone(self, url):
        print(f"Репозиторий успешно клонирован!")

    def remote_add(self, name, url):
        self.repo["remotes"][name] = url
        print(f"Удаленный репозиторий '{name}' успешно добавлен!")

    def show_remotes(self):
        print("Список удаленных репозиториев:")
        for name, url in self.repo["remotes"].items():
            print(f"{name}  {url} (fetch)")
            print(f"{name}  {url} (push)")

    def fetch(self):
        print("Изменения успешно получены!")

    def reset_hard(self, commit):
        current_branch = "master"
        if commit in self.repo["branches"][current_branch]["commits"]:
            self.repo["branches"][current_branch]["head"] = commit
            print(f"Ветка успешно сброшена на коммит '{commit}'!")
        else:
            print(f"Коммит '{commit}' не найден.")

    def revert(self, commit):
        print(f"Изменения из коммита '{commit}' успешно отменены!")

    def stash(self):
        print("Изменения успешно сохранены!")

    def stash_pop(self):
        print("Изменения успешно восстановлены!")

    def tag(self, tag_name):
        current_branch = "master"
        head_commit = self.repo["branches"][current_branch]["head"]
        self.repo["tags"][tag_name] = head_commit
        print(f"Тег '{tag_name}' успешно создан!")

    def show_tags(self):
        print("Список тегов:")
        for tag in self.repo["tags"]:
            print(tag)

    def show_tag(self, tag_name):
        if tag_name in self.repo["tags"]:
            print(f"Тег '{tag_name}' создан в коммите {self.repo['tags'][tag_name]}...")
        else:
            print(f"Тег '{tag_name}' не найден.")

    def show_diff(self):
        print("diff --git a/file.txt b/file.txt")
        print("index 1234567..abcdef0")
        print("--- a/file.txt")
        print("+++ b/file.txt")
        print("@@ -1,2 +1,2 @@")
        print("- Строка 1")
        print("+ Строка 1 (изменена)")

    def show_blame(self, file_name):
        print(f"1234567 (John Doe 2024-08-27) Строка 1 (изменена)")

def main():
    """
    Основная функция.
    """
    gitlab = GitLabEmulator()
    while True:
        command = input("Введите команду: ")
        gitlab.handle_command(command)

if __name__ == "__main__":
    main()

