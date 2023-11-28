#en la bash:
# pip install flask
 
from flask import Flask, render_template, request, redirect, url_for
import  os  
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir,'src', 'templates')

#incializa flask
app = Flask(__name__, template_folder = template_dir)

#Rutas de aplicacion
@app.route('/')
def home():    
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    #convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()    
    return render_template('/index.html', data=insertObject)

@app.route('/user', methods=['POST'])
def add_user():
    id = request.form['id']
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    if username and name and password:
        cursor=db.database.cursor()
        sql = "INSERT INTO users (id, username, name, password) VALUES (%s,%s, %s, %s)"
        data = (id, username, name, password)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home')) 

@app.route('/delete/<string:id>')
def delete(id):
    cursor=db.database.cursor()
    sql = "DELETE FROM users WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home')) 

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    #id = request.form['id']
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    if username and name and password:
        cursor=db.database.cursor()
        sql = "UPDATE users SET username=%s, name = %s, password = %s WHERE id = %s"
        data = (username, name, password, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=4000)
