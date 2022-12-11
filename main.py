from flask import Flask, render_template, request

app = Flask(__name__)

def proccess_data(field_x: str = "", field_y: str = "") -> tuple:
    field_x = field_x if field_x else "lunes martes miercoles jueves viernes"
    field_y = field_y if field_y else "10 22 63 14 89"
    return (
        field_x,
        field_y,
        field_x.split(" "),
        field_y.split(" "),
    )

@app.route('/', methods=["GET", "POST"])
def index():
    '''
    Página principal
    '''
    if request.method == "POST":
        field_x, field_y, data_x, data_y = proccess_data(
            field_x=request.form["axisX"],
            field_y=request.form["axisY"]
        )
    else:
        field_x, field_y, data_x, data_y = proccess_data()
    return render_template(
        'index.html',
        field_x=field_x,
        field_y=field_y,
        data_x=data_x,
        data_y=data_y,
    )


if __name__ == '__main__':
    app.run(debug=True)
