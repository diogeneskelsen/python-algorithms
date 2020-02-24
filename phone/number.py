def number_to_text(number):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    return switcher.get(number, "Invalid")

def number_term(qty):
    switcher = {
        1: "double",
        2: "triple",
        3: "quadruple",
        4: "quintuple",
        5: "sextuple",
        6: "septuple",
        7: "octuple",
        8: "nonuple",
        9: "decuple"
    }

    return switcher.get(qty, "Invalid")

def read_number(phone_number):
    res = ""
    start = 0
    offset = 0
    data = phone_number[1].split("-")
    count = 0

    for i in range(len(data)):

        offset += int(data[i])
        nums = phone_number[0][start:offset]
        
        for x in range(len(nums)):

            if(nums[x] == nums[x-1]):
                count += 1
            else:
                count = 0

            if(count == 0):
                if(x == (len(nums)-1)):
                    res += number_to_text(int(nums[x])) + " "
                else:
                    if(nums[x] != nums[x+1]):
                        res += number_to_text(int(nums[x])) + " "
            else:
                if(x == (len(nums)-1)):
                    res += number_term(count) + " " 
                    res += number_to_text(int(nums[x])) + " "
                    count = 0
                else:
                    if(nums[x] != nums[x+1]):
                        res += number_term(count) + " " 
                        res += number_to_text(int(nums[x])) + " "
                        count = 0

        start += int(data[i])

    return res

def phone_number(phone_list):
    for i in range(len(phone_list)):
        x = read_number(phone_list[i])
        print("Case #" + str(i+1) + ": " + x)

phone_number([["999999999",  "9"], ["15012233444", "3-4-4"], ["15012233444", "3-3-5"], ["12223", "2-3"], ["2544353234854864102426825493629094429744221828448703587259611510954048582897631523802527480763958", "9-9-5-9-1-11-2-9-5-4-1-10-12-10"]])
#phone_number([["15012233444", "3-3-5"]])