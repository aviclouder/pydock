from flask import Flask, render_template, request, redirect
from config import get_db_connection

app = Flask(__name__)

# Home route to display data
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users_detail")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', users=users)

# Route to add new data
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        detail = request.form['detail']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users_detail (name, detail) VALUES (%s, %s)", (name, detail))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')
    return render_template('add_data.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
