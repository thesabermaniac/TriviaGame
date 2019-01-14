import game_rules


def main():
    file = open('trivia.txt', 'r')
    my_game = game_rules.Game(file)
    my_game.start_game()
    my_game.ask_questions()
    my_game.display_scores()


main()
