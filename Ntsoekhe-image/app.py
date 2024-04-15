from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/enternew")
def enternew():
    return render_template("patient.html")

@app.route("/addrec", methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            fname = request.form['fname']
            lname = request.form['lname']
            dob = request.form['dob']
            nationalId = request.form['nationalId']
            gender = request.form['gender']
            phone = request.form['phone']
            email = request.form['email']
            address = request.form['address']
            illness = request.form['illness']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO patients (fname, lname, dob, nationalId, gender, phone, email, address, illness) VALUES (?,?,?,?,?,?,?,?,?)",
                            (fname, lname, dob, nationalId, gender, phone, email, address, illness))
                con.commit()
                msg = "New patient successfully added to our database"
        except:
            con.rollback()
            msg = "Error in the INSERT"
        finally:
            con.close()
            return render_template('result.html', msg=msg)

@app.route('/list')
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM patients")
    rows = cur.fetchall()
    con.close()
    return render_template("list.html", rows=rows)

@app.route("/edit", methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
        try:
            id = request.form['id']
            con = sqlite3.connect("database.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT rowid, * FROM patients WHERE rowid = ?", (id,))
            rows = cur.fetchall()
        except:
            id = None
        finally:
            con.close()
            return render_template("edit.html", rows=rows)

@app.route("/editrec", methods=['POST', 'GET'])
def editrec():
    if request.method == 'POST':
        try:
            rowid = request.form['rowid']
            fname = request.form['fname']
            lname = request.form['lname']
            dob = request.form['dob']
            nationalId = request.form['nationalId']
            gender = request.form['gender']
            phone = request.form['phone']
            email = request.form['email']
            address = request.form['address']
            illness = request.form['illness']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("UPDATE patients SET fname=?, lname=?, dob=?, nationalId=?, gender=?, phone=?, email=?, address=?, illness=? WHERE rowid=?",
                            (fname, lname, dob, nationalId, gender, phone, email, address, illness, rowid))
                con.commit()
                msg = "Patient details successfully edited"
        except:
            con.rollback()
            msg = "Error in the Edit"
        finally:
            con.close()
            return render_template('result.html', msg=msg)

@app.route("/delete", methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        try:
            rowid = request.form['id']
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("DELETE FROM patients WHERE rowid=?", (rowid,))
                con.commit()
                msg = "Patient successfully deleted from our database"
        except:
            con.rollback()
            msg = "Error in the DELETE"
        finally:
            con.close()
            return render_template('result.html', msg=msg)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
