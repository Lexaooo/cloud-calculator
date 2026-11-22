from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            operation = request.form["operation"]

            if operation == "add":
                result = a + b
            elif operation == "sub":
                result = a - b
            elif operation == "mul":
                result = a * b
            elif operation == "div":
                if b == 0:
                    error = "Деление на ноль невозможно"
                else:
                    result = a / b
            else:
                error = "Неизвестная операция"

        except (ValueError, KeyError):
            error = "Введите корректные числа"

    return render_template(
        "index.html",
        result=result,
        error=error
    )

if __name__ == "__main__":
    app.run()