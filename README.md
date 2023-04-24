# Weather Analytics API

Sample API project using the squirrels framework.

## Setup

First, create the virtual environment for the project with the necessary libraries installed.

```bash
pip install pipenv
pipenv install -r requirements.txt
```

Next, create a squirrels database profile.

```bash
squirrels set-profile weather_db --values sqlite /./data/seattle_weather.db "" ""
```

Test that it works!

```bash
squirrels run --debug
```
