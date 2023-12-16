import random
import sys

Q_NUM = 10
OPT = ["A", "B", "C", "D"]


def random_correct_answers() -> list:
    return [OPT[random.randint(0, 3)] for i in range(Q_NUM)]

def validate_ans(ans: list) -> bool:
    if len(ans) != Q_NUM:
        return False
    for a in ans:
        if not a in OPT:
            return False
    return True

def input_ans() -> list:
    ans = list(input().replace(" ", ""))
    valid = validate_ans(ans)
    while not valid:
        print("your answers are not valid")
        ans = list(input().replace(" ", ""))
        valid = validate_ans(ans)
    return ans

def count_correct_answers(l1: list, l2: list) -> int:
    return sum(1 for i in range(Q_NUM) if l1[i] == l2[i])

def main(debug: bool = False) -> None:
    correct_ans = random_correct_answers()
    challenge_cnt = 1
    if debug:
        print(f"charange {challenge_cnt}")
    user_ans = input_ans()
    correct_cnt = count_correct_answers(correct_ans, user_ans)
    passed = (correct_cnt == Q_NUM)
    while not passed:
        print(f"your score is {correct_cnt}")
        if debug:
            print("debug" + "-" * 20)
            print(f"your answers\t{user_ans}")
            print(f"correct answers\t{correct_ans}")
            print("debug" + "-" * 20)
            print(f"charange {challenge_cnt}")
        challenge_cnt += 1
        user_ans = input_ans()
        correct_cnt = count_correct_answers(correct_ans, user_ans)
        passed = (correct_cnt == Q_NUM)
        
    print(f"You passed the test on your {challenge_cnt} challenge!")


if __name__ == '__main__':
    try:
        debug = bool(len(sys.argv) > 1 and bool(sys.argv[1]))
        main(debug)
    except KeyboardInterrupt:
        pass
