from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)

# ROUTES
@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('users.html', users=User.get_all())

@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create', methods=['POST'])
def create():
    # data = {
    #     'first_name': request.form['first_name'],
    #     'last_name': request.form['last_name'],
    #     'email': request.form['email']
    # }
    User.save(request.form)
    print(request.form)
    return redirect('/users')

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    return render_template('edit_user.html', user=User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data = {
        'id': id
    }
    return render_template('show_user.html', user=User.get_one(data))    

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)    
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data = {
        'id': id
    }
    User.destroy(data)
    return redirect('/users')

# @app.route('/users/<int:id>/update')
# def view_page(id):
#     data = {
#         'id': id
#     }
#     return render_template('edit.html', users=Users.show_user(data))

# @app.route('/users/<int:id>/update', methods=["POST"])
# def edit(id):
#     data = {
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'email': request.form['email'],
#         'id': id
#     }
#     Users.edit_user(data)
#     return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)