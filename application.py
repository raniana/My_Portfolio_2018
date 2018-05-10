from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def showMainPage():
	return render_template('welcome.html')




if __name__ == '__main__':

    
    app.debug = True
    app.run(host='0.0.0.0', port=8000)


