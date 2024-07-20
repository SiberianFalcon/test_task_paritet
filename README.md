![Static Badge](https://img.shields.io/badge/Python-gray)  ![Static Badge](https://img.shields.io/badge/Django_Rest_Framework-red?style=flat)  ![Static Badge](https://img.shields.io/badge/Vue.Js-teal)


# Это тестовое задание для фирмы Paritet
## Запуск backend
### На проекте используются пакетные менеджеры Poetry и npm, по этому, если они не установлены на Вашем устройстве то, установите их самостоятельно.
* После исполнения функции ``` git clone https://github.com/SiberianFalcon/test_task_paritet.git ``` в месте исполнения команды появится папка с проектом.
* Далее нужно перейти в папку проекта командой ``` cd test_task_paritet ```.
* Из корневой папки проекта можно запускать бекенд. Для начала нужно установить зависимости. Напишите в терминале ``` poetry shell ``` далее ``` poetry install ```.
* После установки зависимостей нужно подготовить базу данных и выполнить миграции. Сделайте это командой ``` python manage.py makemigrations ``` и ``` python manage.py migrate ```.
* Дальше нам потребуется три терминальных окна: Первое - для написания команд в терминал, Второе - для запуска бекенда, Третье - для запуска фронтенда.
* Во втором терминальном окне выполняем команду ``` python manage.py runserver ```. Бэкенд запущен.


## Запуск frontend

* Если Вы следовали инструкциям выше, то должны находиться в корневой папке проекта. Напишите в первом терминальном окне команду ``` cd frontend ```.
* Сейчас вы перешли в папку где находиться графическая часть проекта и для того чтобы она заработала для неё нужны отдельные зависимости. Чтобы их получить нужно написать в терминале ``` npm install ```. Это займёт около двух минут.
* После установки всех зависимостей мы можем запустить графическую часть проекта. Перейдите в третье терминальное окно и выполните команду ``` npm run serve ```.

  
## Пользование проектом

Сейчас проект работает исключительно локально и между фронтендом и бекендом сняты CORS ограничения для создания возможности взаимодействия на одном устройстве. Это всё ещё два отдельных проекта в одном, но они работают!
чтобы начать пользоваться проектом и посмотреть что я смог сделать впервые пользуясь Vue.js (до этого я о нём только слышал) откройте свой браузер и в адресную строку введите ``` http://localhost:8080/ ```.

Перед вами будет большое текстовое окно, кнопка "выбрать фото" и "Опубликовать пост". Здесь необходимо ввести текст с любым содержимым, будь то описание картинки или несвязный набор букв, а также, 
нажать на кнопку "выбрать фото" и с компьютера выбрать любое изображение. Текст и фото обязательный для заполнения (потому что я так захател и без чего-то одного выглядит куцо). Далее, жмём на кнопку "Опубликовать пость".

Когда на сайте появилась хоть одна публикация, то под ней будет кнопка "Удалить пост", которая, собственно говоря, удаляет пост =)

# Итог:
* За время написания тестового проекта я изучил и впервые поработал с технологией Vue.Js и она мне показалась удобной и занимательной
* Повторил пользование HTML тегами и настройку стилей графических объектов
* Реализовал функционал описанный в техническом задании к тестовому проекту
# Трудности:
* Есть некоторая проблема с прогрузкой фото крупнее 2.5MB  
