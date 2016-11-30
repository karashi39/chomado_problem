#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""the confirmation exam she tried."""

import random


class ConfirmExam(object):
    """object class of the confirmation exam."""

    correct_answers = []
    questions_num = 10
    options_num = 4
    try_get_score_cnt = 0

    def __init__(self):
        """define question data and param for exam."""
        for i in xrange(self.questions_num):
            correct_option = int(random.random() * self.options_num)
            self.correct_answers.append(correct_option)

    def get_score(self, user_answers):
        """take answer list from user and return score."""
        score = 0
        self.try_get_score_cnt += 1
        if len(user_answers) != self.questions_num:
            return 0
        for i in range(self.questions_num):
            u_ans = user_answers[i]
            c_ans = self.correct_answers[i]
            if u_ans == c_ans:
                score += 1
        return score

    def get_correct_answers(self):
        """return list of correct answers."""
        return self.correct_answers

    def get_try_get_score_cnt(self):
        """return how many tried get_score."""
        return self.try_get_score_cnt
