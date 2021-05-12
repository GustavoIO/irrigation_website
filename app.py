from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on')
def zoneOn():
    zone = request.args.get('zone')
    return "ok"

@app.route('/off')
def zoneOff():
    zone = request.args.get('zone')
    return "ok"

@app.route('/logs')
def logs():
    logFile = open('/home/pi/irrigation/log', 'r')
    content = logFile.read()
    logFile.close()
    return content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
