import openai

# Define greetings and regards
greetings = ["Hola", "Hola que tal"]
regards = ["Chau", "Nos Vemos", "Abrazo"]
formal_greetings = ["Estimados","Buenas","Buenas tardes"]
formal_regards = ["Saludos cordiales", "Saludos"]

# Initialize the OpenAI API
openai.api_key = "YOUR_API_KEY"

# Function to check if a greeting is present in the text
def has_greeting(text):
    for greeting in greetings:
        if greeting.lower() in text.lower():
            return True
    return False

# Function to check if a regard is present in the text
def has_regard(text):
    for regard in regards:
        if regard.lower() in text.lower():
            return True
    return False

# Function to check if a formal greeting is present in the text
def has_formal_greeting(text):
    for greeting in formal_greetings:
        if greeting.lower() in text.lower():
            return True
    return False

# Function to check if a formal regard is present in the text
def has_formal_regard(text):
    for regard in formal_regards:
        if regard.lower() in text.lower():
            return True
    return False

# Function to calculate points based on behavior
def calculate_points(email):
    points = 0

    # Check greetings and regards
    if not has_greeting(email) or not has_regard(email):
        points += 1

    # Check formal greetings and regards
    if not has_formal_greeting(email) or not has_formal_regard(email):
        points += 2

    # Get the intention of the message from the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="What is the intention of the message?",
        temperature=0.7,
        top_p=0.9,
        fine_tune="text-davinci-001",
        input=email,
    )

    # Check if the intention is formal
    if response["choices"][0]["text"].lower().startswith("formal"):
        points += 1

    return points

# Function to compare two emails
def compare_emails(email1, email2):
    # Get the points for each email
    points1 = calculate_points(email1)
    points2 = calculate_points(email2)

    # Compare the points
    if points1 > points2:
        return 1
    elif points1 < points2:
        return -1
    else:
        return 0

# Example usage
# Input the email of a persona
persona_email = "Estimados, buenas tardes  Espero que todo vaya bien. Saludos cordiales."

# Input the email of a user
user_email = "Hola, como estas? Espero que todo bien. Abrazo"

# Compare the emails
result = compare_emails(persona_email, user_email)

# Print the result
if result == 1:
    print("The emails are from different people.")
elif result == -1:
    print("The emails are from the same person.")
else:
    print("The emails cannot be compared.")