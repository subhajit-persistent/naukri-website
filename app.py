from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return 'hello worlds'


if __name__ == '__main__':
  # print('its working')
  app.run(host='0.0.0.0', debug=True)
