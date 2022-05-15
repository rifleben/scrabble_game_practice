letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


letters_to_points = {letters: points for letters, points in zip(letters, points)}

letters_to_points[" "] = 0


def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letters_to_points.get(letter, 0)
    return point_total


player_to_words = {"player1": ['BLUE', 'TENNIS', 'EXIT'], "wordNerd": ['EARTH', 'EYES', 'MACHINE'],
                   "Lexi Con": ['ERASER', 'BELLY', 'HUSKY'], "Prof Reader": ['ZAP', 'COMA', 'PERIOD']}

player_to_points = {}


def play_word(player, word):
    player_to_words[player].append(word)


def update_points_total():
    for player, words in player_to_words.items():
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
