from flask import Flask, render_template_string, request 

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def info():
    name = request.args.get('name')
    template = "hello " + name
    return render_template_string(template)

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

 
     