from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Remote',
  },
  {
    'id': 3,
    'title': 'Full Stack Developer',
    'location': 'Kolkata, India',
    'salary': 'Rs. 20,00,000'
  },
  {
    'id': 4,
    'title': 'Backend Developer',
    'location': 'Pune, India',
    'salary': 'Rs. 12,00,000'
  },
]


@app.route("/")
def hello_naukri():
  return render_template('home.html', Jobs=jobs, company_name='Naukri')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(jobs)


if __name__ == '__main__':
  # print('its working')
  app.run(host='0.0.0.0', debug=True)
