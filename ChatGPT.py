
# Author: Diego Munoz Bodden
# This program will answer any of the user's questions regarding the rules of driving on the road by using ChatGPT.



# Importing openai library
import openai

# Reading API key off a text file to keep it hidden
API_File = open(r"API_Key.txt")
API_Key = API_File.read()
API_File.close()

# Activating API key
openai.api_key = API_Key

# Function for calling ChatGPT to generate a response
def ChatGPT(prompt, model="gpt-3.5-turbo"):

    # Array storing user prompt and the parameters by which ChatGPT will give an answer 
    messages = [{"role": "user", "content": prompt},
                {"role": "system", "content": "You are answering user questions related to the rules of driving on the road. Do not answer unrelated questions; instead, " +
                "reply by saying you do not understand the question, and ask them to try again."}]
    
    # Response is generated using the ChatGPT 3.5 model, the message and parameters, and no randomness (0 temperature)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature = 0
    )

    # Response is returned
    return response.choices[0].message["content"]

# While loop for asking if user has any questions, repeating if input is invalid
invalidResponse = True
while (invalidResponse == True):
    
    question = input("\nDo you have any questions about the rules of the road (y/n)? ")

    # If answer to the above question is yes...
    if (question == 'y'):
        
        # User is prompted and ChatGPT response is generated and displayed
        invalidResponse = False
        user_input = input("\nAsk away!\n")
        print("\nGenerating response...")
        ChatGPT_response = ChatGPT(user_input)
        print(ChatGPT_response)

        # While loop for asking if user has any further questions, doubling as a check for if user input for said question is invalid
        invalidResponse2 = True
        furtherQuestions = True
        while (invalidResponse2 == True or furtherQuestions == True):
            
            furtherQuestionsAnswer = input("\nDo you have any further questions (y/n)? ")
            
            # If answer to the above question is yes...
            if (furtherQuestionsAnswer == 'y'):
                
                # Loop will repeat
                invalidResponse2 = False
                furtherQuestions = True

                # User is prompted and ChatGPT response is generated and displayed
                user_input = input("\nAsk away!\n")
                print("\nGenerating response...")
                ChatGPT_response = ChatGPT(user_input)
                print(ChatGPT_response)

            # If answer is no...
            elif (furtherQuestionsAnswer == 'n'):
                
                # Loop will not repeat
                invalidResponse2 = False
                furtherQuestions = False
                
                # User questions part of the program ends
                print("\nAlright. Would you like to continue with your lessons or exit the session?")
            
            else:
                # Loop will repeat, as input was invalid
                invalidResponse2 = True
                print("\nInvalid Response. Try again.\n")

    # If answer to the original question was no...
    elif (question == 'n'):
        
        # Loop will not repeat
        invalidResponse = False
        # User questions part of the program ends
        print("\nAlright. Would you like to continue with your lessons or exit the session?")
        
    else:
        # Loop will repeat, as input was invalid
        invalidResponse = True
        print("\nInvalid Response. Try again.\n")