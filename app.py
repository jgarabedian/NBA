from app import app

# set to false when deploying to prod
app.debug = True
if __name__ == '__main__':
   app.run()
