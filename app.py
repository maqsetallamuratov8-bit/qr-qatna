from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# Waqtsha maǵlıwmatlar bazası (Keleshekte bunı SQLite yamasa MySQL qılamız)
qatnasiw_tizimi = []

@app.route('/')
def index():
    # Tiykarǵı betti ashiw
    return render_template('index.html')

@app.route('/saqlaw', methods=['POST'])
def saqlaw():
    # Frontendten kelgen QR kod mag'liwmatin qabillaw
    data = request.get_json()
    student_id = data.get('student_id')

    # Házirgi waqıttı alıw
    waqit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Maǵlıwmattı saqlaw
    qatnasiw_tizimi.append({'student': student_id, 'waqit': waqit})
    print(f"Qatnastı: {student_id} | Waqtı: {waqit}")

    return jsonify({
        'status': 'success', 
        'message': f'{student_id} tabıslı dizimge alındı!'
    })

if __name__ == '__main__':
    app.run(debug=True)