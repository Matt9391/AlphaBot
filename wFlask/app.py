from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('forward') == 'w':
            print("wwwwwwwwwwwwwwwwwww")
        elif  request.form.get('backward') == 's':
            print("ssssssssssssssssssss")
        elif  request.form.get('left') == 'a':
            print("aaaaaaaaaaaaaaaaaaaa")
        elif  request.form.get('right') == 'd':
            print("dddddddddddddddddddd")
        else:
            print("Unknown")
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')