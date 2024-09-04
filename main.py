import random
import json
import os
import math

file_path = 'terms.json'

data = {}

if os.path.exists(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except (json.JSONDecodeError, IOError):
        # File is empty, invalid JSON, or unreadable
        print("JSON file is broken, file was reset")
        data = {"Terms":{},"Definitions":{}}
else:
    data = {}

with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

mode = input("Multiple Choice, Written Mode, Test Mode, or Create New Set? (type exit at any time to exit or restart the program)\n")
print("\n")

def multi():
    if data["Terms"] and data["Definitions"]:
        options = []
        q = random.randint(1, len(data["Terms"]))
        options.append(data["Definitions"][str(q)])

        while len(options) < 4:
            rnd = random.randint(1, len(data["Terms"]))
            if not data["Definitions"][str(rnd)] in options:
                options.append(data["Definitions"][str(rnd)])

        random.shuffle(options)
        ans = input(f"{data["Terms"][str(q)]}\n1. {options[0]}\n2. {options[1]}\n3. {options[2]}\n4. {options[3]}\n\n")


        if ans == "exit":
            r = random.randint(1,100)
            if r == 21:
                print("Excited the program")
            return
        elif int(ans) > 0 and int(ans) < 5 and data["Definitions"][str(q)] == options[int(ans)-1]:
            print("Correct")
        else:
            print(f"Wrong. Correct Answer: {data["Definitions"][str(q)]}")
        print("\n")
        multi()
    else:
        print("The json file is corrupted or broken")

def write():
    if data["Terms"] and data["Definitions"]:
        rnd = random.randint(1, len(data["Terms"]))
        q = input(data["Terms"][str(rnd)] + ": ")

        if q.lower() == data["Definitions"][str(rnd)].lower():
            print("Correct")
        elif q == "exit":
            r = random.randint(1,100)
            if r == 21:
                print("Excited the program")
            return
        else:
            print(f"Incorrect. Correct Answer: {data["Definitions"][str(rnd)]}")
        print("\n")
        write()
    else:
        print("The json file is corrupted or broken")

def test():
    tmode = input("Would you like to test in multiple choice mode or written mode?\n")
    nqs = input("How many questions do you want to have in your test? (There may be repeats of questions sorry)\n")
    print("\n")
    if "mu" in tmode.lower():
        answers = {}
        questions = {}
        num_correct = 0
        for i in range(int(nqs)):
            if data["Terms"] and data["Definitions"]:
                options = []
                q = random.randint(1, len(data["Terms"]))
                options.append(data["Definitions"][str(q)])

                while len(options) < 4:
                    rnd = random.randint(1, len(data["Terms"]))
                    if not data["Definitions"][str(rnd)] in options:
                        options.append(data["Definitions"][str(rnd)])

                random.shuffle(options)
                print(f"Question #{str(i+1)}\n")
                ans = input(f"{data["Terms"][str(q)]}\n1. {options[0]}\n2. {options[1]}\n3. {options[2]}\n4. {options[3]}\n\n")

                if ans == "exit":
                    r = random.randint(1,100)
                    if r == 21:
                        print("Excited the program")
                    return
                elif int(ans) > 0 and int(ans) < 5 and data["Definitions"][str(q)] == options[int(ans)-1]:
                    questions[str(i+1)] = data["Terms"][str(q)]
                    answers[str(i+1)] = f'"{options[int(ans)-1]}" is correct.'
                    num_correct += 1
                else:
                    questions[str(i+1)] = data["Terms"][str(q)]
                    answers[str(i+1)] = f'"{options[int(ans)-1]} is wrong". Correct Answer: {data["Definitions"][str(q)]}'
                print("\n")
            else:
                print("The json file is corrupted or broken")

        print("TEST RESULTS:")
        for i in range(int(nqs)):
            print(f"Question #{i+1}")
            print(questions[str(i+1)])
            print(answers[str(i+1)])
            print("\n")
        print(f"Your score: {math.ceil((num_correct/int(nqs))*100)}% ({num_correct}/{nqs})")

    elif "wr" in tmode.lower():
        answers = {}
        questions = {}
        num_correct = 0
        for i in range(int(nqs)):
            if data["Terms"] and data["Definitions"]:
                rnd = random.randint(1, len(data["Terms"]))
                print(f"Question #{str(i+1)}\n")
                q = input(data["Terms"][str(rnd)] + ": ")

                if q.lower() == data["Definitions"][str(rnd)].lower():
                    questions[str(i+1)] = data["Terms"][str(rnd+1)]
                    answers[str(i+1)] = f'"{q}" is correct.'
                    num_correct += 1
                elif q == "exit":
                    r = random.randint(1,100)
                    if r == 21:
                        print("Excited the program")
                    return
                else:
                    questions[str(i+1)] = data["Terms"][str(rnd+1)]
                    answers[str(i+1)] = f'"{q} is wrong". Correct Answer: {data["Definitions"][str(rnd+1)]}'
                print("\n")
            else:
                print("The json file is corrupted or broken")
        print("TEST RESULTS:")
        for i in range(int(nqs)):
            print(f"Question #{i+1}")
            print(questions[str(i+1)])
            print(answers[str(i+1)])
            print("\n")
        print(f"Your score: {math.ceil((num_correct/int(nqs))*100)}% ({num_correct}/{nqs})")
        

                 
if "mu" in mode.lower():
    multi()
elif "wr" in mode.lower():
    write()
elif "tes" in mode.lower():
    test()
elif "c" in mode.lower():
    new_set_method = input("Would you like to import a JSON file (advanced) or would you like to export a Quizlet set?\n")
    if "import" in new_set_method.lower() or "json" in new_set_method.lower():
        json_input = input("Paste the json below:\n")

        json_path = "terms.json"
        with open(json_path, "w") as file:
            file.write(json_input) 
            print("\nrestart the program")

    elif "quizlet" in new_set_method.lower() or "export" in new_set_method.lower():
        instructions = input('\nINSTRUCTIONS ON HOW TO EXPORT QUIZLET SET\n1. Go to a quizlet set that YOU OWN and click the three dots next to the Share and Edit buttons.\n2. Select "Export"\n3. VERY IMPORTANT: You will see a menu with a bunch of options at the top. Do not mess the following instructions up.\n4. For the "Between term and definition" option, choose Custom and write "@@" in the box.\n5. For the "Between rows" option, choose Custom and write "##" in the box.\n6. Copy the text and paste (use the right click menu instead of Ctrl + V) it right under this text and press enter.\n')
        input_string = instructions

        pairs = input_string.split("##")

        terms = {}
        definitions = {}

        for i, pair in enumerate(pairs, start=1):
            if "@@" in pair:
                term, definition = pair.split("@@")
                terms[str(i)] = term.strip()
                definitions[str(i)] = definition.strip()

        output = {
            "Terms": terms,
            "Definitions": definitions
        }

        json_output = json.dumps(output, indent=4)

        json_path = "terms.json"
        
        with open(json_path, "w") as file:
            file.write(json_output)

        print("\nrestart the program")