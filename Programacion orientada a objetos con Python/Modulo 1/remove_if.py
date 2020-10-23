# -*- coding: utf-8 -*-

def call_cost_calculate(call):
    cost = 0
    if call.is_local():
        cost = calculate_local_cost_of(call)
    elif call.is_national():
        cost = calculate_national_cost_of(call)
    elif call.is_international():
        cost = calculate_international_cost_of(call)
    return cost


class CallCostCalculator(object):

    @classmethod
    def to_handle(klass, call):
        # codigo que busca el CallCostCalculator correspondiente
    def calculate(self):
        raise NotImplementedError("Subclass Responsability")
    

class LocalCallCostCalculator(object):
    def calculate(self):
        # codigo de calculate_local_cost_of


class NationalCallCostCalculator(object):
    def calculate(self):
        # codigo de calculate_national_cost_of


class InternationalCallCostCalculator(object):
    def calculate(self):
        # codigo de calculate_international_cost_of


cost_calculator = CallCostCalculator.to_handle(call)
cost_calculator.calculate()