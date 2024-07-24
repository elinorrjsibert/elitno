   def check_profanity(text):
       return profanity_check.predict([text])[0]

   text = "This is a sample sentence with profanity."
   contains_profanity = check_profanity(text)
   print(contains_profanity)  # Output: True
   