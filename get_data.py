def get():
    pride_and_prejudice_text = open('Pride_and_Prejudice.txt', 'r').read()

    pride_and_prejudice_text = pride_and_prejudice_text.replace('\n', ' ')
    pride_and_prejudice_text = pride_and_prejudice_text.replace('Mr.', 'Mr')
    pride_and_prejudice_text = pride_and_prejudice_text.replace('Ms.', 'Ms')
    pride_and_prejudice_text = pride_and_prejudice_text.replace('Mrs.', 'Mrs')

    return pride_and_prejudice_text
