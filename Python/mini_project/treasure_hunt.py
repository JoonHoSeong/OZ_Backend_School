import random

# 게임 초기화
def initialize_game(n:int) :
    player_position = [random.randint(0,n-1), random.randint(0,n-1)]
    treasure_position = [random.randint(0,n-1),random.randint(0,n-1)]
    return treasure_position, player_position

# 플레이어 이동
def move_player(board_size, treasure_position,player_position, direction):
    if direction.upper() in ['N', 'S', 'W', 'E'] :
        if direction.upper() == 'N' and player_position[0] > 0:
            player_position[0] -= 1
        elif direction.upper() == 'S' and player_position[0] < board_size-1:
            player_position[0] += 1
        elif direction.upper() == 'W' and player_position[1] > 0:
            player_position[1] -= 1
        elif direction.upper() == 'E' and player_position[1] < board_size-1:
            player_position[1] += 1
        else :
           print('해당 방향으로 이동할 수 없습니다. 다른 방향을 선택해 주세요')
           return -1
        print(f"{direction}방향으로 이동하였습니다.")
        print(f"보물까지 남은 거리는 {calculate_distance(treasure_position, player_position)} 입니다.")
    return player_position

# 거리 계산
def calculate_distance(treasure_position, player_position):
    return abs(treasure_position[0]-player_position[0])+abs(treasure_position[1]-player_position[1])


# 게임 실행
def play_game(board_size):
    move_num = 0
    treasure_position, player_position = initialize_game(board_size)
    while treasure_position != player_position :
        while True :
            try :
                direction = input('이동하고자 하는 방향을 입력해 주세요(N,S,E,W) :').upper()
                if direction not in ['N', 'S', 'E', 'W'] :
                    print('방향을 잘 못 입력하셨습니다. 다시 입력해 주세요.(N,S,W,E)')
                    continue
                break
            except :
                print('방향을 잘 못 입력하셨습니다. 다시 입력해 주세요.(N,S,W,E)')
        if move_player(board_size,treasure_position,player_position,direction) == -1 :
            continue
        move_num += 1
    print(f"총 {move_num}번의 욺직임으로 보물을 발견했습니다! 축하합니다!")
        
# 게임 보드 크기 설정 및 게임 시작
if __name__ == "__main__":
    board_size = 5  # 보드 크기를 5x5로 설정
    play_game(board_size) 