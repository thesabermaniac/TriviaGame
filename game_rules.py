class Questions:

    def __init__(self, question, answers, user_input, correct_answer):
        self.__question = question
        self.__answers = answers
        self.__user_input = user_input
        self.__correct = correct_answer

    def read_question(self, file):
        self.__question = file.readline()

    def read_answer(self, file):
        self.__answers = []
        for x in range(4):
            q = file.readline()
            self.__answers.append(q)

    def read_correct(self, file):
        self.__correct = file.readline()

    def set_question(self, question):
        self.__question = question

    def set_answers(self, answers):
        self.__answers = answers

    def set_user_input(self, user_input):
        self.__user_input = user_input

    def set_correct(self, correct):
        self.__correct = correct

    def get_question(self):
        return self.__question

    def get_answers(self):
        return self.__answers

    def get_user_input(self):
        return self.__user_input

    def get_correct(self):
        return self.__correct

    def check_correct(self):
        if int(self.__correct) == int(self.__user_input):
            return True

    def __str__(self):
        return self.__question + '\n' + self.__answers


class Game:

    def __init__(self, file):
        self.__player_names = []
        self.__player_scores = []
        self.__START_SCORE = 0
        self.__file = file
        self.__question = ''
        self.__answers = ''
        self.__user_input = 0
        self.__correct = 0
        self.__my_questions = Questions(self.__question, self.__answers, self.__user_input, self.__correct)

    def set_file(self, file):
        self.__file = file

    def get_file(self):
        return self.__file

    def start_game(self):
        for x in range(2):
            player_name = input("Player " + str(x+1) + " what's your name? ")
            self.__player_names.append(player_name)
            self.__player_scores.append(self.__START_SCORE)

    def ask_questions(self):
        for x in range(len(self.__player_names)):
            print("OK,", self.__player_names[x], "your turn.")
            for y in range(5):
                input("Press Enter to display the next question.")
                self.__my_questions.read_question(self.__file)
                print(self.__my_questions.get_question())
                self.__my_questions.read_answer(self.__file)
                answers = self.__my_questions.get_answers()
                for z in answers:
                    print(z)
                user = int(input("Enter the correct answer (1-4): "))
                self.__my_questions.set_user_input(user)
                self.__my_questions.read_correct(self.__file)
                self.__my_questions.get_correct()
                if self.__my_questions.check_correct():
                    print("Correct!")
                    self.__player_scores[x] += 20
                else:
                    print("Incorrect")
                print()

    def display_scores(self):
        winner = self.__player_scores.index(max(self.__player_scores))
        for x in range(len(self.__player_scores)):
            print(self.__player_names[x], ": ", self.__player_scores[x], "/100", sep='')
        if self.__player_scores[0] == self.__player_scores[1]:
            print("Both players are tied")
        else:
            print(self.__player_names[winner], "wins!")
