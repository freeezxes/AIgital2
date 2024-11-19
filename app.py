from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create-room')
def create_room():
    return render_template('index1.html')

@app.route('/submit-room', methods=['POST'])
def submit_room():
    # Get data from the form
    room_name = request.form.get('room_name')
    quiz_topic = request.form.get('quiz_topic')
    room_size = request.form.get('room_size')
    question_quantity = request.form.get('question_quantity')
    
    # For demonstration purposes, display the values in the console
    print("Room Name:", room_name)
    print("Quiz Topic:", quiz_topic)
    print("Room Size:", room_size)
    print("Question Quantity:", question_quantity)
    
    # Render a template or redirect to another page
    return render_template('room_summary.html', room_name=room_name, quiz_topic=quiz_topic, room_size=room_size, question_quantity=question_quantity)

if __name__ == '__main__':
    app.run(debug=True)
