first_word = input()
second_word = input()
last_printed_string = first_word

for character_index in range(len(first_word)):
        right_side = first_word[character_index+1:]
        left_side = second_word[:character_index+1]
        new_string = left_side + right_side
        if new_string == last_printed_string:
            continue
        print(new_string)
        last_printed_string = new_string