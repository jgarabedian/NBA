from app import app

# set to false when deploying to prod
app.debug = False
if __name__ == '__main__':
   app.run(host='0.0.0.0')
