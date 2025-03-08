from flask import render_template, request, redirect, url_for, session
from app import app

app.secret_key = 'supersecretkey'  # Needed for session management

@app.route('/')
def home():
    session['correct'] = 0
    session['incorrect'] = 0
    return render_template('index.html')

@app.route('/question1')
def question1():
    return render_template('question1.html')

@app.route('/question1_feedback', methods=['POST'])
def question1_feedback():
    question1 = request.form['question1']
    correct_answer = '32 BBY - 19 BBY'
    if question1 == correct_answer:
        feedback_title = "Correct!"
        feedback_message = f"The answer was {correct_answer}."
        session['correct'] += 1
    else:
        feedback_title = "Nope!"
        feedback_message = f"The correct answer was {correct_answer}."
        session['incorrect'] += 1
    return render_template('feedback1.html', feedback_title=feedback_title, feedback_message=feedback_message)

@app.route('/question2')
def question2():
    return render_template('question2.html')

@app.route('/question2_feedback', methods=['POST'])
def question2_feedback():
    question2 = request.form['question2']
    correct_answer = 'Red 5'
    if question2 == correct_answer:
        feedback_title = "Correct!"
        feedback_message = f"The answer was {correct_answer}."
        session['correct'] += 1
    else:
        feedback_title = "Nope!"
        feedback_message = f"The correct answer was {correct_answer}."
        session['incorrect'] += 1
    return render_template('feedback2.html', feedback_title=feedback_title, feedback_message=feedback_message)

@app.route('/question3')
def question3():
    return render_template('question3.html')

@app.route('/question3_feedback', methods=['POST'])
def question3_feedback():
    question3 = request.form['question3']
    correct_answer = 'Coruscant'
    if question3 == correct_answer:
        feedback_title = "Correct!"
        feedback_message = f"The answer was {correct_answer}."
        session['correct'] += 1
    else:
        feedback_title = "Nope!"
        feedback_message = f"The correct answer was {correct_answer}."
        session['incorrect'] += 1
    return render_template('feedback3.html', feedback_title=feedback_title, feedback_message=feedback_message)

@app.route('/question4')
def question4():
    return render_template('question4.html')

@app.route('/question4_feedback', methods=['POST'])
def question4_feedback():
    question4 = request.form['question4']
    correct_answer = 'Constantine the Great'
    if question4 == correct_answer:
        feedback_title = "Correct!"
        feedback_message = f"The answer was {correct_answer}."
        session['correct'] += 1
    else:
        feedback_title = "Nope!"
        feedback_message = f"The correct answer was {correct_answer}."
        session['incorrect'] += 1
    return render_template('feedback4.html', feedback_title=feedback_title, feedback_message=feedback_message)

@app.route('/question5')
def question5():
    return render_template('question5.html')

@app.route('/question5_feedback', methods=['POST'])
def question5_feedback():
    question5 = request.form['question5']
    correct_answer = 'Trajan'
    if question5 == correct_answer:
        feedback_title = "Correct!"
        feedback_message = f"The answer was {correct_answer}."
        session['correct'] += 1
    else:
        feedback_title = "Nope!"
        feedback_message = f"The correct answer was {correct_answer}."
        session['incorrect'] += 1
    return render_template('feedback5.html', feedback_title=feedback_title, feedback_message=feedback_message)

@app.route('/question6')
def question6():
    return render_template('question6.html')

@app.route('/question6_feedback', methods=['POST'])
def question6_feedback():
    question6 = request.form['question6']
    correct_answer = 'Concrete'
    if question6 == correct_answer:
        feedback_title = "Correct!"
        feedback_message = f"The answer was {correct_answer}."
        session['correct'] += 1
    else:
        feedback_title = "Nope!"
        feedback_message = f"The correct answer was {correct_answer}."
        session['incorrect'] += 1
    return render_template('feedback6.html', feedback_title=feedback_title, feedback_message=feedback_message)

@app.route('/question7')
def question7():
    return render_template('question7.html')

@app.route('/question7_feedback', methods=['POST'])
def question7_feedback():
    question7 = request.form['question7']
    correct_answer = '476 AD'
    if question7 == correct_answer:
        feedback_title = "Correct!"
        feedback_message = f"The answer was {correct_answer}."
        session['correct'] += 1
    else:
        feedback_title = "Nope!"
        feedback_message = f"The correct answer was {correct_answer}."
        session['incorrect'] += 1
    return render_template('feedback7.html', feedback_title=feedback_title, feedback_message=feedback_message)

@app.route('/question8')
def question8():
    return render_template('question8.html')

@app.route('/question8_feedback', methods=['POST'])
def question8_feedback():
    question8 = request.form['question8']
    correct_answer = 'Demetrious Johnson'
    if question8 == correct_answer:
        feedback_title = "Correct!"
        feedback_message = f"The answer was {correct_answer}."
        session['correct'] += 1
    else:
        feedback_title = "Nope!"
        feedback_message = f"The correct answer was {correct_answer}."
        session['incorrect'] += 1
    return render_template('feedback8.html', feedback_title=feedback_title, feedback_message=feedback_message)

@app.route('/question9')
def question9():
    return render_template('question9.html')

@app.route('/question9_feedback', methods=['POST'])
def question9_feedback():
    question9 = request.form['question9']
    correct_answer = 'Alex Pereira'
    if question9 == correct_answer:
        feedback_title = "Correct!"
        feedback_message = f"The answer was {correct_answer}."
        session['correct'] += 1
    else:
        feedback_title = "Nope!"
        feedback_message = f"The correct answer was {correct_answer}."
        session['incorrect'] += 1
    return render_template('feedback9.html', feedback_title=feedback_title, feedback_message=feedback_message)

@app.route('/submit_quiz')
def submit_quiz():
    correct = session.get('correct', 0)
    incorrect = session.get('incorrect', 0)
    return render_template('results.html', correct=correct, incorrect=incorrect)