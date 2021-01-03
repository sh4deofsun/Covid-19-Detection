# covid-19-detection
Scanning for Covid 19 using fuzzy logic

**Dependencies:** Python 3.8.0, Pip, Virtualenv, Poetry

### Create virtual environment 

```sh
git clone https://github.com/sh4deofsun/covid-19-detection.git
cd Covid19Tarama-BulanikMantik
```

### Install depedencies

```sh
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
or 

```sh
poetry install
```

### Start

```sh
$ streamlit run run.py 
```

or 

```sh
$ poetry run streamlit run run.py
```

#### Covid-19 Data Analysis
```sh
$ python data_proc.py 
```

## References:
 - https://github.com/Namerlight/C19-Prediction-via-Symptoms-with-Fuzzy-Logic
 - https://towardsdatascience.com/learn-how-to-create-web-data-apps-in-python-b50b624f4a0e

## Deficiencies:
There are rules that membership functions need to be defined

## Contributors:
<table style="width:100%">
  <tr>
    <td align="center"><a href="https://github.com/asliyigit"><img src="https://avatars3.githubusercontent.com/u/52151047" width="100px;" alt=""/><br /><sub><b>Asli YIGIT </b></sub></a><br />
    </td>
    <td align="center"><a href="https://github.com/sh4deofsun"><img src="https://avatars2.githubusercontent.com/u/17470615" width="100px;" alt=""/><br /><sub><b>Batuhan YALCIN</b></sub></a><br />
    </td>
    </td>
    <td align="center"><a href="https://github.com/mertbilgic"><img src="https://avatars2.githubusercontent.com/u/34304850" width="100px;" alt=""/><br /><sub><b>Mert Bilgiç</b></sub></a><br />
    </td>
  </tr>
</table>