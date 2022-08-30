

from QueryProgram import QueryProgram


if __name__ == "__main__":
    program = QueryProgram()

    user_input = ''
    print('''Available inputs: 
             1. Query ID: Gets set and theme info of that ID.
             2. 'exit': exits the program. ''')

    while user_input != 'exit':
        query_id = input('Input value: ')

        if query_id.lower() == 'exit':
            user_input = 'exit'
        else:
            program.query(query_id)




