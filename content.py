from aiogram.utils.formatting import as_list, as_marked_section, Bold
from config import url


about_pochtmen = (
    "Почтмен - это интуитивно понятное и легко настраиваемое приложение, разработанное для владельцев малых веб-сайтов."
     "\n\nНаше приложение позволяет вам создавать и управлять формами обратной связи <strong>без необходимости написания собственного бэкенда.</strong>"
     "\n\nМы сделали процесс создания форм простым и доступным даже для тех, кто не имеет опыта в веб-разработке."
)

func_list = as_list(
    as_marked_section(
        Bold("Основной функционал Почтмен:\n"),
        "Быстрое создание форм\n",
        "Простота интерграции АПИ Почтмен\n",
        "Уведомления в реальном времени\n",
        "Готовый HTML, CSS и JS код\n",
        marker="🔹",
    ))

success_subscribe = "Вы успешно подписались на рассылку уведомлений с ваших форм!"

success_unsubscribe = "Вы успешно отписались от наших уведомлений!"

welcome_text = (f'Добро пожаловать в Почтмен-бот!\n\nДля того чтобы подписаться на рассылку уведомлений нажмите'
                f' <strong>Профиль</strong>.\n\nДля подробной информации о Почтмене нажмите <strong>О сервисе</strong>.')

profile_text = "<strong>Профиль</strong>\n\nЗдесь вы можете подписаться на уведомления, а так же отписаться от них."


contacts_text = (f'<strong>Наши контакты:</strong>'
                 f'\n\n{url}\npochtmen@mail.ru'
                 f'\n\nПишите на нашу почту для технической поддержки!')