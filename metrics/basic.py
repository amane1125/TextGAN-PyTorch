# -*- coding: utf-8 -*-
# @Author       : William
# @Project      : TextGAN-william
# @FileName     : basic.py
# @Time         : Created at 2019-05-14
# @Blog         : http://zhiweil.ml/
# @Description  :
# Copyrights (C) 2018. All Rights Reserved.

from abc import abstractmethod


class Metrics:
    def __init__(self, name='Metric', wight=1):
        self.name = name
        # represents effect on final score
        # ex.: self-bleu has weight = -1 (less is better)
        # bleu has weight = 1 (more is better)
        # weights needed for combined metric evaluation
        self.weight = weight
        self.in_use = False
        self.metric_value_with_current_state = None

    def get_score(self):
        if not self.in_use:
            return 0

        if self.metric_value_with_current_state is not None:
            return self.metric_value_with_current_state

        self.metric_value_with_current_state = self.calculate_metric()
        return self.metric_value_with_current_state

    @abstractmethod
    def calculate_metric(self)

    @abstractmethod
    def reset(self):
        pass

    def _reset(self):
        self.metric_value_with_current_state = None
