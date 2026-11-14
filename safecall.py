from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check-audio', methods=['POST'])
def check_audio():
    data = request.json
    amplitude = data.get('amplitude', 0)
    
    # Порог күшейтілді (1500): енді сервер ұсақ шулар мен бөлме дыбыстарын топырлатып елемейді.
    # Тек телефон динамигі сияқты қатты дыбыс қана өткізіледі.
    if amplitude < 1500:
        return jsonify({"alert": False})
    
    print(f"НАСТОЯЩИЙ МОШЕННИК! Амплитуда: {amplitude}")
    return jsonify({"alert": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
