from flask import Flask, render_template, request
import sli_app

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the input from the form
        user_input = request.form['Languages']
        print("Language chosen is", user_input)
        if user_input.upper() in ['ENGLISH']:
            sli_app.main()
        else:
            print("Language yet to be implemented")
            return f'Given Language option [' + user_input + '] -- yet to be implemented'

    return render_template('SLIHome.html')


if __name__ == '__main__':
    app.run(debug=True)