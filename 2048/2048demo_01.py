# while True:
#     print('打印棋盘')
#     code = input('请输入操作》》》：')
#     if code == 'w':
#         print('向上操作')
#     elif code == 's':
#         print('向下操作')
#     elif code == 'a':
#         print('向左操作')
#     elif code == 'd':
#         print('向右操作')
#     elif code == 'r':
#         print('重新开始')
#     elif code == 'q':
#         print('退出')
#     else:
#         print('请输入正确的指令')
import random

class Game:
    def __init__(self):
        self.scores = 0
        self.width = 4
        self.board_list = [[' ' for i in range(self.width)] for i in range(self.width)]
        self.restart()
        self.empty_pieces = []

    def restart(self):
        self.board_list = [[' ' for i in range(self.width)] for i in range(self.width)]
        self.scores = 0
        while True:
            t1 = (random.randint(0, self.width-1), random.randint(0, self.width-1))
            t2 = (random.randint(0, self.width-1), random.randint(0, self.width-1))
            if t1 != t2:
                break
        self.board_list[t1[0]][t1[1]] = random.randrange(2, 5, 2)
        self.board_list[t2[0]][t2[1]] = random.randrange(2, 5, 2)

    #向左合并
    def row_left_merge(self,row):
        temp = []
        for item in row:
            if item != ' ':
                temp.append(item)

        new_row = []
        flag = True
        for i in range(len(temp)):
            if flag:
                if i+1<len(temp) and temp[i] == temp[i+1]:
                    new_row.append(temp[i]*2)
                    self.scores += temp[i]*2
                    flag = False
                else:
                    new_row.append(temp[i])
            else:
                flag = True
        while True:
            if len(new_row) != self.width :
                new_row.append(' ')
            else:
                break
        return new_row

    def move_up(self):
        temp_list = self.turn_left(self.board_list)
        for i in range(self.width):
            temp_list[i] = self.row_left_merge(temp_list[i])
        self.board_list = self.turn_right(temp_list)
        return self.board_list

    def move_down(self):
        temp_list = self.turn_right(self.board_list)
        for i in range(self.width):
            temp_list[i] = self.row_left_merge(temp_list[i])
        self.board_list = self.turn_left(temp_list)
        return self.board_list

    def move_left(self):
        for i in range(self.width ):
            self.board_list[i] = self.row_left_merge(self.board_list[i])

    def move_right(self):
        #倒序排
        temp_list = [row[::-1] for row in self.board_list]
        for i in range(self.width ):
            temp_list[i]  = self.row_left_merge(temp_list[i])
            self.board_list[i] = temp_list[i][::-1]

    def turn_right(self, matrix):
        return [list(x)[::-1] for x in zip(*matrix)]

    def turn_left(self, matrix):
        temp = self.turn_right(self.turn_right(matrix))
        return self.turn_right(temp)

    def is_win(self):
        for i in range(self.width):
            for j in range(self.width):
                if self.board_list[i][j] == 2048:
                    return True

    def is_game_over(self):
        flag = True
        if len(self.is_empty_pieces()) == 0:
            for item in self.board_list:
                for j in range(len(item)-1):
                    if item[j] == item[j+1]:
                        flag = False
                        break

            for item in self.turn_right(self.board_list):
                for j in range(len(item)-1):
                    if item[j] == item[j+1]:
                        flag = False
                        break
        else:
            flag = False
        self.empty_pieces = []
        return flag

    def is_empty_pieces(self):
        for i in range(len(self.board_list)):
            for j in range(len(self.board_list)):
                if self.board_list[i][j] == ' ':
                    self.empty_pieces.append([i,j])
        return self.empty_pieces

    def add_pieces(self):
        self.empty_pieces = self.is_empty_pieces()
        if len(self.empty_pieces) >= 2:
            while True:
                num_1 = random.randint(0, len(self.empty_pieces)-1)
                num_2 = random.randint(0, len(self.empty_pieces)-1)
                t1 = self.empty_pieces[num_1]
                t2 = self.empty_pieces[num_2]
                if t1 != t2:
                    self.empty_pieces = []
                    break
            self.board_list[t1[0]][t1[1]] = random.randrange(2, 5, 2)
            self.board_list[t2[0]][t2[1]] = random.randrange(2, 5, 2)
        elif len(self.empty_pieces) == 1:
            t1 = self.empty_pieces[0]
            self.board_list[t1[0]][t1[1]] = random.randrange(2, 5, 2)
            self.empty_pieces = []

    def start(self):
        while True:
            self.print_game_board()
            code = input('please input operate：')
            if code.lower() == 'w':
                self.move_up()
            elif code.lower() == 's':
                self.move_down()
            elif code.lower() == 'a':
                self.move_left()
            elif code.lower() == 'd':
                self.move_right()
            elif code.lower() == 'r':
                self.restart()
                continue
            elif code.lower() == 'q':
                exit('退出')
            else:
                print('请输入正确的指令')

            self.add_pieces()
            if self.is_win():
                print('游戏得分:%s'%self.scores)
                print('恭喜你，赢得游戏')
                break
            if self.is_game_over():
                self.print_game_board()
                exit('you are fail! gameover!')


    def print_game_board(self):
        game_str = """
        SCORE:{}
        +-----*-----*-----*-----*
        |{: ^5}|{: ^5}|{: ^5}|{: ^5}|
        +-----*-----*-----*-----*
        |{: ^5}|{: ^5}|{: ^5}|{: ^5}|
        +-----*-----*-----*-----*
        |{: ^5}|{: ^5}|{: ^5}|{: ^5}|
        +-----*-----*-----*-----*
        |{: ^5}|{: ^5}|{: ^5}|{: ^5}|
        +-----*-----*-----*-----*
        w(up,s(down),a(left),d(right)
            r(restart),q(exit)
        """.format(self.scores,
                   *self.board_list[0],
                   *self.board_list[1],
                   *self.board_list[2],
                   *self.board_list[3],
                   )
        print(game_str)


if __name__ == '__main__':
    game = Game()
    game.start()
