from flask import Flask, render_template, request,url_for,redirect,session
import os
from dotenv import load_dotenv
import os
# print("secret key",secrets.token_hex(32))  # Copy the generated secret key

load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
print(f"Loaded Secret Key: {app.secret_key}")
class Questions:
    q_id = -1
    question = ""
    option1 = ""
    option2 = ""
    option3 = ""
    correctOption = -1

    def __init__(self, q_id, question, option1, option2, option3, correctOption):
        self.q_id = q_id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.correctOption = correctOption

    def get_correct_option(self):
        if self.correctOption == 1:
            return self.option1
        elif self.correctOption == 2:
            return self.option2
        elif self.correctOption == 3:
            return self.option3


q1 = Questions(1, " What is the pH of a 0.001 M solution of HCl?", "1", "3", "4", 1)
q2 = Questions(2, "Which of the following elements is a noble gas?", "oxygen", "nitrogen", "helium", 3)
q3 = Questions(3, "The chemical formula of methane is:", "CH₄", "CH₃", "C₂H₆",1 )
q4 = Questions(4, "Which organ is responsible for the production of insulin in the human body?", "liver", "pancreas", "stomach", 2)
q5 = Questions(5, "Which of the following is the largest planet in our solar system?", "jupiter", "satern", "mars", 1)
q6 = Questions(6, "Which of the following is the unit of electric current?", "volt", "ampere", "ohms", 2)
q7 = Questions(7, "The process of respiration in plants mainly occurs through:", "stomata", "roots", "xylem", 1)
q8 = Questions(8, "Which of the following is NOT a type of RNA?", "mRNA", "tRNA", "DNA",3)
q9 = Questions(9, "What is the atomic number of carbon?", "8", "7", "6", 3)
q10 = Questions(10, "The velocity of sound in air at 0°C is approximately:", "300 m/s", "330 m/s", "400 m/s", 2)
q11 = Questions(11, "In which of the following processes is energy released?", "Melting of ice", "Respiration", "Evaporation of water", 2)
q12 = Questions(12, "The DNA structure was discovered by:", "Watson and Crick", "Mendel", "Darwin", 1)
q13 = Questions(13, "Which of the following vitamins is produced by the body when exposed to sunlight?", "Vitamin A", "Vitamin C", "Vitamin D", 3)
q14 = Questions(14, "The electric field is measured in:", " Newtons", "Volts per meter", "Amperes", 2)
q15 = Questions(15, " Which gas makes up the majority of Earth's atmosphere?", "Nitrogen", "Carbon dioxide", "Oxygen", 1)
q16 = Questions(16, " The smallest unit of life is:", "Atom", "Organ", "Cell", 3)
q17 = Questions(17, "Which of the following is the primary function of white blood cells?", "Transport oxygen", " Fight infections", "Clot blood", 2)
q18 = Questions(18, "Which of the following laws is associated with the force of gravity?", "Newton's First Law", "Coulomb's Law", "Law of Universal Gravitation", 3)
q19 = Questions(19, "Which of the following elements is a halogen?", "Nitrogen", " Fluorine", "Oxygen", 2)
q20 = Questions(20, "Which of the following is a function of the liver?", "Producing bile", "Filtering blood", "Both B and C", 3)


questions_list = [q1, q2, q3 ,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20]


q21= Questions(21,"Choose the correct sentence:","She is knowing the answer.","She knows the answer","She know the answer.", 2 )
q22= Questions(22,"Which is the correct form of the verb?  \nBy the time we arrive, they _____ already left.","will have","had","have",1  )
q23= Questions(23,"Choose the correct form of the verb:\nShe ____ to the store yesterday","went","go","goes", 1 )
q24= Questions(24," Fill in the blank with the correct preposition:\nThey arrived ____ the airport late","to","at ","in",2  )
q25= Questions(25,"Choose the correct article:\nShe is ____ engineer.","a","the","an",3  )
q26= Questions(26,"Which sentence is correct?","I have been to the movie yesterday.","I am going to the movie yesterday.","I went to the movie yesterday.", 3 )
q27= Questions(27, "Fill in the blank with the correct form of the verb:\nI ____ (never/see) such a beautiful sight before","never saw","have never seen","had never seen",2)
q28= Questions(28,"Choose the correct verb form:\nBy the time we arrive, they ____ (finish) the meeting","will have finished"," finish","will finish",1  )
q29= Questions(29,"hoose the correct word:\nHe is very ____ at solving problems."," good","well","better", 1 )
q30= Questions(30,"Fill in the blank with the correct form of the adjective:\nThis is the ____ movie I have ever watched","good","better","best",3  )
q31= Questions(31," Choose the correct form:\nThey ____ to the park when it started raining"," went","were going","had gone",2  )
q32= Questions(32, "Choose the correct form of the verb:\nI ____ him at the party last night."," saw"," was seeing","see", 1)
q33= Questions(33, "Choose the correct modal verb:\nYou ____ wear a seatbelt while driving.","may","must","should", 2)
q34= Questions(34,"Choose the correct pronoun:\nThis is the book ____ I borrowed last week.","which","who","that",1  )
q35= Questions(35,"Fill in the blank with the correct form:\n She is more ____ than her sister","intelligent","most intelligent","more intelligent", 3 )
q36= Questions(36,"Choose the correct option:\nBy next week, she ____ (finish) the project","finishes","will have finished","will finish", 2 )
q37= Questions(37,"Choose the correct relative clause:\n The man ____ is my uncle","where","which","who", 3 )
q38= Questions(38,"Fill in the blank:\nIt’s important to ____ your homework on time","make","take","do", 3 )
q39= Questions(39,"Choose the correct form of the verb:\nI ____ (read) a book when she called me","read","was reading","will read", 2 )
q40= Questions(40, "Fill in the blank with the correct form:\nIf I ____ (be) you, I would take the job offer","were","was","am",1 )

questions_list2 = [q21, q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33,q34,q35,q36,q37,q38,q39,q40]
@app.route("/")
def home():
    return render_template("home.html") 

@app.route('/contactus')
def contact_us():
    return render_template('contactus.html')  # Contact Us page
@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')  # About Us page

users = {}  # Temporary storage for registered users

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        test_choice = request.form["test_choice"]  # Capture the selected test

        # Check if passwords match
        if password != confirm_password:
            return "Passwords do not match. Please try again."

        # Check if username already exists
        if username in users:
            return "Username already exists. Please choose a different username."

        # Store user credentials and test choice in the users dictionary
        users[username] = {"email": email, "password": password, "test_choice": test_choice}

        # Save user details in session
        session["username"] = username
        session["email"] = email
        session["test_choice"] = test_choice

        # Redirect to the registration success page
        return redirect(url_for("registration_success"))

    return render_template("register.html")


@app.route("/registration_success")
def registration_success():
    username = session.get("username")
    email = session.get("email")
    test_choice = session.get("test_choice")
    if not username or not email:
        return redirect(url_for("register"))  # Redirect if session data is missing
    return render_template(
        "registration_success.html",
        username=username,
        email=email,
        test_choice=test_choice
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Validate user credentials
        if username in users and users[username]["password"] == password:
            # Save user details in session
            session["username"] = username
            session["email"] = users[username]["email"]

            # Check the test choice from session and redirect to the quiz page
            test_choice = users[username]["test_choice"]  # Retrieve the test choice
            return redirect(url_for("show_test", test=test_choice))

        return "Invalid username or password. Please try again."

    return render_template("login.html")



@app.route('/test/<test>', methods=['GET'])
def show_test(test):
    if test == 'ielts':
        return render_template('ielts.html')  # Render IELTS test page
    elif test == 'mdcat':
        return render_template('quiz.html')  # Render MDCAT test page
    else:
        return redirect(url_for('home'))  # Redirect if no valid test is selected

@app.route("/test/mdcat")
def quiz():
    if "username" not in session:
        return redirect(url_for("login.html"))  # Redirect to login if not logged in
    return render_template("quiz.html", questions_list=questions_list)
@app.route("/submitquiz", methods=["POST"])
def submit_quiz():
    correct_count = 0
    total_questions = len(questions_list)
    results = []

    for question in questions_list:
        question_id = str(question.q_id)
        selected_option = request.form.get(f"option_{question_id}")
        correct_option = question.get_correct_option()
        
        # Check and track if the answer is correct
        is_correct = selected_option == correct_option
        results.append({
            "question": question.question,
            "selected": selected_option,
            "correct": correct_option,
            "is_correct": is_correct
        })
        
        if is_correct:
            correct_count += 1

    # Retrieve user data from the session
    username = session.get("username", "Guest")
    email = session.get("email", "Not Provided")
    
    return render_template(
        "quiz_result.html", 
        correct_count=correct_count, 
        total_questions=total_questions, 
        results=results, 
        username=username, 
        email=email
    )

def get_ielts_questions():
    print("Fetching IELTS Questions")
    return questions_list2

@app.route("/test/ielts")
def ielts():
    print("IELTS Route Accessed")
    if "username" not in session:
        return redirect(url_for("login"))  # Redirect to login route if not logged in

    # Fetch the IELTS questions from the global list
    questions_list2 = get_ielts_questions()  # Ensure this returns the correct list (questions_list2)
    print("Questions List 2:", questions_list2)  # Print the list to check

    return render_template("ielts.html", questions_list2=questions_list2)

@app.route('/submitielts', methods=['POST'])
def submit_ielts():
    if "username" not in session:
        return redirect(url_for('login'))

    # Get user answers from the form
    user_answers = {}
    for question in questions_list2:
        user_answers[question.q_id] = request.form.get(f"option_{question.q_id}")

    # Compare user answers with correct answers and prepare the results
    correct_count = 0
    results = []
    for question in questions_list2:
        user_answer = user_answers.get(question.q_id)
        correct_answer = question.get_correct_option()

        is_correct = (user_answer == correct_answer)
        if is_correct:
            correct_count += 1

        results.append({
            'question': question.question,
            'selected': user_answer,
            'correct': correct_answer,
            'is_correct': is_correct,
        })

    # Prepare additional details like the user's name and email
    username = session.get('username')
    email = session.get('email')
    total_questions = len(questions_list2)

    # Render the results page and pass all the necessary information
    return render_template('quiz_result.html', 
                           username=username, 
                           email=email, 
                           correct_count=correct_count, 
                           total_questions=total_questions, 
                           results=results)

@app.route("/logout")
def logout():
    session.clear()  # Clear all session data (logout user)
    return redirect(url_for("home"))  # Redirect to home or login page after logout

if __name__ == "__main__":
    app.run(debug=True)  