from flask import Flask, render_template, request, url_for

app=Flask(__name__)

@app.route( '/', methods = [ 'GET', 'POST' ] )
def index():
    bmi=''
    if  request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height')) 
        bmi = round(weight/(height**2), 2)
    return render_template('index.html', bmi=bmi)

if __name__=='__main__':
    app.run()
