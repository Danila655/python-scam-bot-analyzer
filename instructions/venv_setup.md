# Установка виртуального окружения Python

Эта инструкция помогает создать виртуальное окружение `.venv` для проекта на Python.

Виртуальное окружение нужно, чтобы зависимости проекта устанавливались отдельно и не мешали другим проектам на компьютере.

---

## 1. Проверка Python

Сначала нужно проверить, что Python установлен.

### macOS и Linux

```bash
python3 --version
```

Если команда не работает, попробуй:

```bash
python --version
```

### Windows

```powershell
py --version
```

Если команда не работает, попробуй:

```powershell
python --version
```

Для этого проекта желательно использовать Python `3.12`.

---

## 2. Переход в папку проекта

Перед созданием виртуального окружения нужно открыть терминал в папке проекта.

### macOS и Linux

```bash
cd путь/к/папке/проекта
```

Пример:

```bash
cd ~/projects/analyzer_scam_bot
```

### Windows

```powershell
cd путь\к\папке\проекта
```

Пример:

```powershell
cd C:\Users\User\projects\analyzer_scam_bot
```

---

## 3. Создание виртуального окружения

Виртуальное окружение нужно создать один раз.

### macOS и Linux

```bash
python3 -m venv .venv
```

Если используется команда `python`, то:

```bash
python -m venv .venv
```

### Windows

```powershell
py -m venv .venv
```

Если используется команда `python`, то:

```powershell
python -m venv .venv
```

После выполнения команды в проекте появится папка `.venv`.

---

## 4. Активация виртуального окружения

Активацию нужно делать каждый раз, когда ты снова открываешь терминал для работы с проектом.

### macOS и Linux

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate.bat
```

Если окружение активировалось, в начале строки терминала обычно появится `(.venv)`.

---

## 5. Если Windows не даёт активировать окружение

В PowerShell может появиться ошибка из-за политики выполнения скриптов.

Тогда запусти PowerShell от имени обычного пользователя и выполни:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

После этого снова активируй окружение:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 6. Проверка, что окружение работает

После активации проверь Python.

### macOS и Linux

```bash
which python
python --version
```

### Windows

```powershell
where python
python --version
```

Путь к Python должен указывать на папку `.venv`.

---

## 7. Установка зависимостей проекта

Если в проекте есть файл `requirements.txt`, установи зависимости:

```bash
python -m pip install -r requirements.txt
```

Если проект учебный и не требует сторонних библиотек, этот шаг можно пропустить.

---

## 8. Запуск проекта

После активации окружения можно запускать проект:

```bash
python main.py
```

---

## 9. Выход из виртуального окружения

Чтобы выйти из окружения, выполни:

```bash
deactivate
```

---

## 10. Краткая шпаргалка

### macOS и Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

### Windows CMD

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python main.py
```
