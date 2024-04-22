import random

def monty_hall_simulation(num_trials: int, switch_door: bool) -> float:
  wins = 0
  for _ in range(num_trials):
    # 3개의 문과 1개의 보상이 있는 문 중에서 무작위로 하나를 선택합니다.
    doors = ['goat'] * 2 + ['car']
    random.shuffle(doors)

    # 참가자가 처음에 선택한 문의 인덱스를 무작위로 선택합니다.
    selected_index = random.randrange(3)

    # 진행자가 선택한 문 중에서 염소가 있는 문을 엽니다.
    remaining_doors = [i for i in range(3) if i != selected_index and doors[i] == 'goat']
    opened_door = random.choice(remaining_doors)

    # 선택을 변경할 경우
    if switch_door:
      remaining_doors = [i for i in range(3) if i != selected_index and i != opened_door]
      selected_index = remaining_doors[0]

    # 만약 참가자가 선택한 문이 자동차라면 승리입니다.
    if doors[selected_index] == 'car':
      wins += 1

  return wins / num_trials

if __name__ == "__main__":
  # 시뮬레이션을 실행하고 결과를 출력합니다.
  num_trials = 10
  switch_door = True  # 참가자가 문을 변경하는 경우
  winning_rate = monty_hall_simulation(num_trials, switch_door)
  print("Changing doors winning rate:", winning_rate)
  
  switch_door = False  # 참가자가 문을 변경하지 않는 경우
  winning_rate = monty_hall_simulation(num_trials, switch_door)
  print("Not changing doors winning rate:", winning_rate)