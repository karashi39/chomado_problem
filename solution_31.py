#!/user/bin/env python
# -*- encoding:utf-8 -*-
"""try confirmation exam with readable algorithm."""

from confirmation_exam import ConfirmExam


def main():
    """main function."""
    # initialization.
    exam = ConfirmExam()
    q_num = exam.questions_num
    o_num = exam.options_num
    user_answers = []
    for i in xrange(q_num):
        user_answers.append(0)

    # solution.
    for q in xrange(q_num):
        q_correct_answer = -1
        pre_score = -100
        for o in xrange(o_num - 1):
            user_answers[q] = o
            now_score = exam.get_score(user_answers)
            if now_score == pre_score + 1:
                # o is correct answer.
                q_correct_answer = o
            elif now_score == pre_score - 1:
                # 0 is correct answer.
                q_correct_answer = o - 1
            pre_score = now_score
        if q_correct_answer == - 1:
            # last opiton is correct answer.
            q_correct_answer = o_num - 1
        user_answers[q] = q_correct_answer

    # display the result.
    print "this solution derived the correct answer as"
    print user_answers
    print "score is " + str(exam.get_score(user_answers)) + "."
    print "tried " + str(exam.get_try_get_score_cnt()) + " times."

if __name__ == '__main__':
    main()
