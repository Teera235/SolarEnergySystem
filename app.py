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
        RealDay = int(request.form['RealDay'])

        SunHours = 4  # คุณสามารถกำหนดค่าเริ่มต้นหรือใช้ค่าคงที่ตามที่คุณต้องการ
        Efficiency = 0.9  # คุณสามารถกำหนดค่าเริ่มต้นหรือใช้ค่าคงที่ตามที่คุณต้องการ

        AllTime = SystemSize * SunHours * FtCost * Efficiency * RealDay
        PayBackTime = TotalCost / AllTime

        result = f"เวลาคืนทุน: {round(PayBackTime, 1)} ปี"
    except ValueError:
        result = "ค่าไม่ถูกต้อง กรุณาป้อนตัวเลขที่ถูกต้อง"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
