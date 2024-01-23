from flask import Flask, request, jsonify
import subprocess, socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def stress_cpu():
    if request.method == 'GET':
        return jsonify(socket.gethostbyname(socket.gethostname()))
    
    elif request.method == 'POST':
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return jsonify('Success!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
