from flask import Flask
import os
import socket
import argparse

app = Flask(__name__)

color_codes = {
    "blue":   "#7ac8ee",
    "green":  "#9eff9a",
    "pink":   "#f6019d",
    "purple": "#541388",
    "red":    "#ff9a9e",
    "yellow": "#ffca05"
}

default_port = 80

@app.route("/")
def hello():
    html = "<body style="background: { args['color'] };"></body>"
           "<h3>Hello {hostname}!</h3>" \
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Simple webpage with color background.')
  parser.add_argument('-c', '--color', default='blue', help='Webpage background color')
  parser.add_argument('-p', '--port', default=80, type=int, help='Port to listen on')
  parser.parse_args()

  app.run(host='0.0.0.0', port=args['port'])

