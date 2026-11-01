questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],

    ["What is the capital of India?", "Mumbai", "Kolkata", "New Delhi", "Chennai", 3],

    ["Who invented the telephone?", "Thomas Edison", "Alexander Graham Bell", "Newton", "Einstein", 2],

    ["Which language is used for web development?", "HTML", "Node", "Java", "All of these", 4],

    ["Which is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Venus", 3],

    ["Who is known as the Father of Computers?", "Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs", 1],

    ["Which animal is known as the King of the Jungle?", "Tiger", "Lion", "Elephant", "Leopard", 2],

    ["How many days are there in a leap year?", "365", "366", "364", "360", 2],

    ["Which gas do plants absorb?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3],

    ["Who developed Python programming language?", "James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup", 2],

    ["Which is the fastest land animal?", "Lion", "Horse", "Cheetah", "Tiger", 3],

    ["Which country is famous for the Eiffel Tower?", "Italy", "Germany", "France", "Spain", 3],

    ["What is the chemical symbol of Gold?", "Ag", "Au", "Fe", "Cu", 2],

    ["How many bits are there in one byte?", "4", "8", "16", "32", 2],

    ["Which is the largest ocean in the world?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],

    ["Who wrote the Indian National Anthem?", "Mahatma Gandhi", "Rabindranath Tagore", "Subhas Chandra Bose", "Jawaharlal Nehru", 2],

    ["Which data structure follows FIFO?", "Stack", "Queue", "Tree", "Graph", 2],

    ["What does CPU stand for?", "Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Processing User", 1],

    ["Which planet is known as the Red Planet?", "Venus", "Mars", "Saturn", "Mercury", 2],

    ["What is the full form of HTML?", "Hyper Text Markup Language", "High Transfer Machine Language", "Hyper Tool Multi Language", "Home Text Markup Language", 1]
]
 
prizes = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 20000000, 30000000, 40000000, 50000000, 70000000]
sum=0
i=0
for question in questions:
    
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")
    
    # check whether the answe is correct or not
    a=int(input("Enter your answer. 1 for a / 2 for b / 3 for c / 4 for d\n"))
    
    if(question[5]==a):
        print("Correct Answer") 
    else:
        print(f"Incorrect , the correct one was{question[5]}")   
        print("Better luck next time")
        break
    print(f"You won {prizes[i]}🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
    i+=1
    
         
     