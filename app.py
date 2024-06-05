import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    print("Path to index.html:", os.path.join(app.root_path, 'templates', 'index.html'))
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        TotalCost = float(request.form['TotalCost'])
        SystemSize = float(request.form['SystemSize'])
        FtCost = float(request.form['FtCost'])

        SunHours = 4
        Efficiency = 0.9
        RealDay = 360 

        AllTime = SystemSize * SunHours * FtCost * Efficiency * RealDay
        PayBackTime = TotalCost / AllTime 

        result = f"Your PayBackTime: {round(PayBackTime, 1)} years"
    except ValueError:
        result = "Invalid input. Please enter a valid number."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
