def test_func():
    # 🚨 Don't change the code below 👇
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")
    # 🚨 Don't change the code above 👆
    
    #Write your code below this line 👇
    combined_string = name1 + name2
    lower_case_string = combined_string.lower()
    t = lower_case_string.count("t")
    r = lower_case_string.count("r")
    u = lower_case_string.count("u")
    e = lower_case_string.count("e")
    true = t+r+u+e
    l = lower_case_string.count("l")
    o = lower_case_string.count("o")
    v = lower_case_string.count("v")
    e = lower_case_string.count("e")
    love = l+o+v+e
    love_score = int(str(true)+str(love))
    if (love_score < 10) or (love_score > 90):
      print(f"your love_score is {love_score}, you go together as coke and mentos.")
    elif(love_score >= 40) and (love_score <=50):
      print(f"your love_score is {love_score}, you are alright together.")
    else:
      print(f"Your score is {love_score}.")
    
    
    
    
    
    
    
    
    
    
    #Write your code above this line 👆
    # 🚨 Do NOT modify the code below this line 👇
    
    
    with open('testing_copy.py', 'w') as file:
      file.write('def test_func():\n')
      with open('main.py', 'r') as original:
        f2 = original.readlines()[0:45]
        for x in f2:
