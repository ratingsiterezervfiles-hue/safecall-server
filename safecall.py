from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check-audio', methods=['POST'])
def check_audio():
    data = request.json
    amplitude = data.get('amplitude', 0)

    # Облачный фильтр: егер дыбыс 350-ден төмен болса - мусор
    if amplitude < 350:
        return jsonify({"alert": False})

    print(f"Күмәнді дыбыс тіркелді! Амплитуда: {amplitude}")
    return jsonify({"alert": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
