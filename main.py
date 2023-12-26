import random


class Question:
    q_num = 10
    opt = ["A", "B", "C", "D"]
    challenge_cnt = 0
    passed = False

    def __init__(self) -> None:
        self.ans = [self.opt[random.randint(0, 3)] for i in range(self.q_num)]

    def answer(self) -> int:
        ans = list(input().replace(" ", ""))
        while not self.validate_ans(ans):
            print("your answers are not valid")
            ans = list(input().replace(" ", ""))
        self.challenge_cnt += 1
        score = self.score(ans)
        print(f"your score is {score}")
        self.set_passed(score)
        return score

    def set_passed(self, score: int) -> None:
        self.passed = self.q_num == score
        if self.passed:
            print(f"You passed the test on your {self.challenge_cnt} challenge!")

    def validate_ans(self, ans: list | None) -> bool:
        if not ans:
            return False
        if len(ans) != self.q_num:
            return False
        for a in ans:
            if a not in self.opt:
                return False
        return True

    def score(self, ans: list) -> int:
        return sum(1 for i in range(self.q_num) if ans[i] == self.ans[i])


def main() -> None:
    question = Question()
    try:
        while not question.passed:
            question.answer()
    except KeyboardInterrupt:
        print(f"\ncorrect answer is {''.join(question.ans)}")


if __name__ == "__main__":
    main()
