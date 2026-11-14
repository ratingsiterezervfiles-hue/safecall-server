from flask import Flask, request, jsonify
import time

app = Flask(__name__)

last_trigger_time = 0
hit_count = 0

@app.route('/check-audio', methods=['POST'])
def check_audio():
    global last_trigger_time, hit_count
    data = request.json
    amplitude = data.get('amplitude', 0)
    
    # Егер дыбыс максималды деңгейге жетпесе (одиночный щелчок) - мусор ретінде қабылдамаймыз
    if amplitude < 3800:
        return jsonify({"alert": False})
    
    current_time = time.time()
    
    # Егер қатты дыбыс үздіксіз қайталанып жатса (телефоннан шыққан сөз сияқты)
    if current_time - last_trigger_time < 2.0:
        hit_count += 1
    else:
        hit_count = 1
        
    last_trigger_time = current_time
    
    # Жалғыз шертулерді өткізбеу үшін 2 секунд ішінде кемінде 3 рет қайталануы тиіс
    if hit_count >= 3:
        print(f"МОШЕННИК РАСПОЗНАН! Деңгей: {amplitude}")
        hit_count = 0
        return jsonify({"alert": True})
        
    return jsonify({"alert": False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
