from app import app

# set to false when deploying to prod
app.debug = False
if __name__ == '__main__':
   app.run()
