# NBA using flask

This program does a few different things, and is my first time building something using Flask. So far we can:

1. Scrape the web using beautifulSoup (an easy python library) to get all of the spreads for upcoming NBA games
2. Select a matchup, and then use the nba_api python packages to bring in stats of when those teams play each and  overall stats
3. In the player comparison, select 2 players using Rapid-API, then pull in their season stats using balldontlie.io and visualize using the echarts library

## It is highly recommended to use a virtual environment!

(I use virtualenv)

## You'll want to ensure you have all the dependencies on your virtual env, so run

```
pip install -r requirements.txt
```
Our requirements folder will ensure every environment has the necessary packages
## To start the server and see your changes, run
```
python app.py
```

> If running locally, set the following line in [app.py](./app.py)
> 
> Always set to False when deploying to prod
```python
app.debug = True
```

This will restart the server with every saved change


> Did you install more packages in your venv?
```
pip freeze > requirements.txt
```

## Check out the demo

[Demo](http://app-nba.herokuapp.com/)
