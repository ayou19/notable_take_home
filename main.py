input = "Patient presents today with several issues. Number one BMI has increased by 10% since their last visit. Number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn’t improved for last 4 weeks."

phrase_indicators = ["number one", 
                    "number two", 
                    "number three", 
                    "number four",
                    "number five",
                    "number six",
                    "number seven",
                    "number eight",
                    "number nine"]

word_to_number = {"number one": 1, 
                    "number two": 2, 
                    "number three": 3, 
                    "number four": 4,
                    "number five": 5,
                    "number six": 6,
                    "number seven": 7,
                    "number eight": 8,
                    "number nine": 9}

next_phrase = "number next"

# first run for one list
def transcribe(input):
    output = ""
    # check to see if input contains a starting phrase indicator
    if input:
        for ind_num in range(len(phrase_indicators)):
            if phrase_indicators[ind_num] in input.lower():
                indicator = phrase_indicators[ind_num]
                # val of key is the first list_num
                list_num = word_to_number[indicator]
                # split string between starting indicator and everything else
                start_indicator_index = input.lower().index(indicator)
                output += input[:start_indicator_index]
                output += "\n"+str(list_num)+"."
                input = input[start_indicator_index + len(indicator):]
                while next_phrase in input.lower():
                    # print new line next number
                    start_indicator_index = input.lower().index(next_phrase)
                    list_num += 1
                    # split string and add before part
                    output += input[:start_indicator_index]
                    output += "\n"+str(list_num)+"."
                    cap = input[start_indicator_index + len(next_phrase): start_indicator_index + len(next_phrase)+2].upper()
                    input = cap + input[start_indicator_index + len(next_phrase)+2:]
                output += input
        return output
    else:
        return input

print(transcribe(input))