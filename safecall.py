from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check-audio', methods=['POST'])
def check_audio():
    data = request.json
    amplitude = data.get('amplitude', 0)
    
    # Порог выставлен на 800: тишину и мелкие шорохи отсекает, 
    # но динамик телефона вплотную пробивает его мгновенно без всяких задержек!
    if amplitude < 800:
        return jsonify({"alert": False})
    
    print(f"МОШЕННИК ОБНАРУЖЕН! Амплитуда: {amplitude}")
    return jsonify({"alert": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
