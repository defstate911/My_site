from flask import render_template, request, redirect, url_for

from app import app

personal_data = []

@app.route("/", methods=["GET", "POST"])

def index():
#использует метод POST, так как информация будет отправляться. Request method сравнивает данные с HTTP-запросом.
    if request.method == 'POST':
        #функция request.form извлекает значение из соответствующих полей
        name_user = request.form.get('name_user')
        city_user = request.form.get('city_user')
        hobby_user = request.form.get('hobby_user')
        year_user = request.form.get('year_user')

        #создаёт условие для проверки наличия данных в полях title и content
        if name_user and city_user and city_user and year_user:
            personal_data.append({'name_user': name_user, 'city_user': city_user, 'hobby_user': hobby_user, 'year_user': year_user})
            #использует для обновления страницы и предотвращения повторной отправки формы.
            return redirect(url_for('index'))

    #возвращает отрендеренный шаблон с переданными данными постов
    return render_template('site_anketa.html', personal_data=personal_data)
