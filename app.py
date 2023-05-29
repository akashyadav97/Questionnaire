from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        score = 0
        
        name = request.form['name'].title()

        response1 = request.form['response1']
        if response1 == "4":
            score += 2
        elif response1 == "3":
            score += 1

        response2 = request.form['response2']
        if response2 == "2":
            score += 2
        elif response2 == "1":
            score += 1

        response3 = request.form['response3']
        if response3 == "2":
            score += 2
        elif response3 == "1":
            score += 1

        response4 = request.form['response4']
        if response4 == "2":
            score += 2
        elif response4 == "1":
            score += 1

        return render_template('result.html', name=name, score=score)

    return render_template('questionnaire.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

