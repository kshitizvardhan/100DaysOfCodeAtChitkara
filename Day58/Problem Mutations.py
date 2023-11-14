def mutate_string(string, position, character):
    string_out= string[:position]+character+string[position+1:]
    return string_out
