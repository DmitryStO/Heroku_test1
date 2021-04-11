from flask import Flask, request, url_for
import os

app = Flask(__name__)


@app.route('/')
def index():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <h1> Любимый лицей <h1>
                            <img src="https://i.ibb.co/DbZMCPs/hideme.png">
                             <h3>             пока данную задачу никто не решил, все в твои силах<h3>
                           
                          </body>
                         <!https://bit.ly/3sTtpy0>
                        </html>'''


@app.route('/home')
def index():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <h1> Любимый лицей <h1>
                            <img src="https://i.ibb.co/DbZMCPs/hideme.png">
                             <h3>             пока данную задачу никто не решил, все в твои силах<h3>

                          </body>
                         <!https://bit.ly/2Qhlso8>
                        </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>

                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета притендента на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname"  placeholder="Введите Фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите Имя" name="name">
                                    <option></option>
                                    <input type="postadres" class="form-control" id="postadres" placeholder="Введите адрес почты" name="postadres">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Среднее Спецальное</option>
                                          <option>Высшее</option>
                                          <option>Другое</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у вас есть професии?</label>
                                       <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="1" value="1">
                                          <label class="form-check-label" for="1">
                                            инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="2" value="2">
                                          <label class="form-check-label" for="2">
                                            пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="3" value="3">
                                          <label class="form-check-label" for="3">
                                            строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="4" value="4">
                                          <label class="form-check-label" for="4">
                                            экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="5" value="5">
                                          <label class="form-check-label" for="5">
                                            врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="6" value="6">
                                          <label class="form-check-label" for="6">
                                            инженер по терраформированию
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="7" value="7">
                                          <label class="form-check-label" for="7">
                                            климатолог
                                          </label>

                                        <option></option>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>

                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в мисси?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">

                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['postadres'])
        print(request.form['education'])
        print(request.form['job'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        return "Форма отправлена"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='localhost', port=port)