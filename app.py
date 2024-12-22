
from flask import Flask, request, render_template_string, url_for

app = Flask(__name__)

# Base HTML template with a class photo and comment form
PAGE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Internet Hall of Fame - World's Coolest Class</title>
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 40px;
            background-color: #f0f4f8;
            min-height: 100vh;
        }
        .page-container {
            max-width: 1600px;
            margin: 0 auto;
            padding: 20px;
        }
        .hall-of-fame {
            background-color: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        .title-section {
            text-align: center;
            margin-bottom: 10px;
        }
        h1 {
            color: #2d3748;
            font-size: 78px;
            margin: 0;
            padding: 0;
        }
        h2 {
            color: #4a5568;
            font-weight: 500;
            font-size:20px;
            margin: 10px 0 0 0;
        }
        .photo-container {
            background-color: #f8fafc;
            border-radius: 15px;
            max-width: 1600px;
            max-height: 1200px;
            overflow: hidden;
        }
        .class-photo {
            max-width: 1600px;
            max-height: 1200px;
            width: 100%;
            height: auto;
            object-fit: contain;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .comment-section {
            background-color: #f8fafc;
            padding: 30px;
            border-radius: 15px;
            margin-top: 30px;
        }
        .comment-section h3 {
            color: #2d3748;
            margin-top: 0;
        }
        textarea {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            font-size: 16px;
            resize: vertical;
            box-sizing: border-box;
        }
        textarea:focus {
            outline: none;
            border-color: #4299e1;
            box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.1);
        }
        .submit-button {
            padding: 12px 25px;
            background-color: #4299e1;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.2s ease;
        }
        .submit-button:hover {
            background-color: #3182ce;
        }
        .latest-message {
            margin-top: 30px;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .latest-message h4 {
            color: #2d3748;
            margin-top: 0;
        }
    </style>
</head>
<body>
    <div class="page-container">
        <div class="hall-of-fame">
            <div class="title-section">
                <h1>🏆 Internet Hall of Fame 🏆</h1>
                <h2>Presenting: The World's Coolest Class!</h2>
            </div>
            
            <div class="photo-container">
                <img class="class-photo" src="{{ url_for('static', filename='class.jpg') }}" alt="World's Coolest Class">
            </div>

            <div class="comment-section">
                <h3>Leave a Message for the Cool Class</h3>
                <form method="POST">
                    <textarea name="message" rows="4" placeholder="Share your thoughts..."></textarea><br>
                    <input type="submit" value="Post Message" class="submit-button">
                </form>
                
                <div class="latest-message">
                    <h4>Latest Message:</h4>
                    {{ message | safe }}
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    if request.method == 'POST':
        # Vulnerable: directly inserting user input without sanitization
        message = request.form.get('message', '')
    return render_template_string(PAGE_TEMPLATE, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
