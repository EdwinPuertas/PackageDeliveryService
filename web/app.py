from flask import Flask, render_template, request, send_from_directory
from flask_bootstrap import Bootstrap
from logic.Address import Address
from logic.Person import Person
from logic.Package import Package
from logic.OverweightPackage import OverweightPackage
from logic.StandardPackage import StandardPackage
from logic.ado import ADO


app = Flask(__name__)
bootstrap = Bootstrap(app)
list_packages = list()
aut_code = 0


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title="Home")


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_update/<id_person>', methods=['GET'])
def person_update(id_person):
    return render_template('person_update.html', id_person=id_person)


@app.route('/person_detail', methods=['POST'])
def person_detail():
    ado = ADO()
    op = request.form['op']
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    if op == 'I':
        sql = "INSERT INTO person (idperson, name, last_name) VALUES (%s, %s, %s)"
        values = (int(id_person), first_name, last_name)
        data = ado.dml(sql=sql, val=values, op='I')
    elif op == 'U':
        sql = 'UPDATE person SET name={0}{2}{0}, last_name={0}{3}{0} WHERE idperson={1}'.format('"', int(id_person),
                                                                                                first_name, last_name)
        data = ado.dml(sql=sql, op='U')
    return render_template('person_detail.html', value=data)


@app.route('/person_delete/<id_person>', methods=['GET'])
def person_delete(id_person):
    ado = ADO()
    sql = 'DELETE FROM person WHERE idperson={0}'.format(int(id_person))
    data = ado.dml(sql=sql, op='D')
    return render_template('person_detail.html', value=data)


@app.route('/people')
def people():
    ado = ADO()
    data = ado.query("SELECT idperson, name, last_name FROM gestion_spe.person")
    return render_template('people.html', value=data)


@app.route('/address')
def address():
    ado = ADO()
    data = ado.query("SELECT id, country, city, state, street, floor, apartment, postal FROM gestion_spe.address")
    return render_template('address.html', value=data)


@app.route('/address_add', methods=['GET'])
def address_add():
    return render_template('address_add.html')


@app.route('/address_detail', methods=['GET'])
def address_detail():
    ado = ADO()
    country = request.form['country']
    city = request.form['city']
    state = request.form['state']
    street = request.form['street']
    floor = request.form['floor']
    apartment = request.form['apartment']
    postal = request.form['code']
    sql = "INSERT INTO address (country, city, state, street, floor, apartment, postal) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (str(country), str(city), str(state), str(street), int(floor), int(apartment), int(postal))
    data = ado.dml(sql=sql, val=values, op='I')
    return render_template('address_detail.html', data=data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=False)