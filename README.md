<h1 align="center">
  	 Covid-19 Reporter API
</h1>

<p align="center">
  <b>Visualize latest coronavirus information with some filters and history data.</b></br>

<a target="_blank" href="https://covid19-reporter.netlify.app/">View App</a>
</br>

</p>

<p align="center">
  <br><b>Corona virus API for showing number of cases, deaths, recoveries and active patients around the globe </b> 
</p>

# Setup

- Clone the repository `git clone https://github.com/joshuachinemezu/covid19-reporter-api`

## Without Docker

- Install virtualenv https://virtualenv.pypa.io/en/stable/installation.html
- Setup virtualenv `virtualenv venv`
- Activate virtualenv `source venv/bin/activate`
- Install dependencies `pip install -r requirements.txt`
- To start app `python run.py`

## With Docker

- Build image
  - `docker build -t covid-reporter-api:latest .`
    <br/> or
  - `make build`
- Run container
  - `docker run -p 5000:5000 covid-reporter-api`
    <br/>or
  - `make run`

# Technologies

- Python (Flask)
- Pomber Covid API https://github.com/pomber/COVID19
- CoronaStatistics API http://api.coronastatistics.live
- Heroku

## Contributions

- Spread the word
- Give it a star
- Open pull requests

## License

MIT © [Joshua Chinemezu](https://github.com/joshuachinemezu)
