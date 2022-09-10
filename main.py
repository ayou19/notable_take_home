input = "Patient presents today with several issues. Number one BMI has increased by 10% since their last visit. Number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn’t improved for last 4 weeks."

starting_phrase_indicators = {"number one": 1, 
                    "number two": 2, 
                    "number three": 3, 
                    "number four": 4,
                    "number five": 5,
                    "number six": 6,
                    "number seven": 7,
                    "number eight": 8,
                    "number nine": 9}

next_phrase_indicator = "number next"

# first run for one list
def transcribe(input):
    output = ""
    # check to see if input contains a starting phrase indicator
    # val of key is the first list_num
    # if yes,
        # split string between starting indicator and everything else
        # add before starting str to output
        # while str is not empty
            # check for next phrase indicator
            # if yes,
                # print new line next number
                # split string and add before part
            # if no,
                # add final part of str
    # if no,
        # print out the input
    print(input)