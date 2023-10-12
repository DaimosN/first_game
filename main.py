"""
ИГРА КРЕСТИКИ-НОЛИКИ.
"""


class Board:
    def __init__(self):
        self.board = [Cell(i) for i in range(1, 10)]  # состояние поля

    def change_cell(self, number, symbol):
        """изменить состояние клетки"""
        if not self.board[number - 1].busy:
            self.board[number - 1].busy = True
            self.board[number - 1].symbol = symbol
            return True
        else:
            print('Похоже, что данная клетка уже занята\nВыберите другую клетку')
            return False

    def check_the_game_status(self):
        """проверить статус игры"""
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                     (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for num in win_coord:
            if self.board[num[0]].busy == self.board[num[1]].busy == self.board[num[2]].busy == True:
                if player_one.symbol == self.board[num[0]].symbol == self.board[num[1]].symbol == self.board[num[2]].symbol:
                    print(f"Победил игрок {player_one.name}")
                    return True
                elif player_two.symbol == self.board[num[0]].symbol == self.board[num[1]].symbol == self.board[num[2]].symbol:
                    print(f"Победил игрок {player_two.name}")
                    return True
        print('Победитель не определен')
        return False  # победителя нет


class Cell:
    def __init__(self, number, symbol='', busy=False):
        self.busy = busy
        self.number = number
        self.symbol = symbol


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        #self.win_count = 0

    def make_move(self):
        """сделать ход"""
        while True:
            try:
                cell_num = int(input('Введите номер клетки которую вы зачеркиваете (от 1 до 9):'))
            except ValueError:
                print('Вы ввели неверный номер')
                return self.make_move()
            return cell_num


class Game:
    def __init__(self, board, player_one, player_two):
        self.board = board
        self.player_one = player_one
        self.player_two = player_two

    def start_one_move(self, player):
        print(f'Ходит игрок {player.name}')
        cell_num = player.make_move()
        if not self.board.change_cell(cell_num, player.symbol):
            return self.start_one_move(player)
        if self.board.check_the_game_status():
            return True
        else:
            return False

    def start_one_game(self):
        pass


board = Board()
player_one = Player('Дмитрий', '*')
player_two = Player('Некто другой', '0')
game = Game(board, player_one, player_two)

count = 0
while True:
    if count % 2 == 0:
        if game.start_one_move(player_one):
            break
    else:
        if game.start_one_move(player_two):
            break
    count += 1


