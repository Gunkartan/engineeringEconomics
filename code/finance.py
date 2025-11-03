import numpy as np
import numpy_financial as npf

class Finance:
    def npv(self, quarterly_rate: float, cash_flows: list[int]) -> float:
        return npf.npv(quarterly_rate, cash_flows)
    
    def irr_quarterly(self, cash_flows: list[int]) -> float:
        return npf.irr(cash_flows)
    
    def irr_annually(self, irr_quarterly: float) -> float:
        return (1 + irr_quarterly) ** 4 - 1
    
    def payback_period(self, cumulative_cash: list[int]) -> int:
        payback_quarter = np.argmax(cumulative_cash >= 0)

        if cumulative_cash[-1] < 0:
            return -1
        
        else:
            return payback_quarter
        
    def fractional_payback(self, cumulative_cash: list[int], payback_quarter: int, cash_flows: list[int]) -> float:
        before = cumulative_cash[payback_quarter - 1]
        cf_in_period = cash_flows[payback_quarter]
        fraction = abs(before) / cf_in_period

        return (payback_quarter - 1) + fraction

if __name__ == '__main__':
    initial_investment = -2000
    free_cash_flows = [-1326, 288, 955, 2321]
    cash_flows = [initial_investment] + free_cash_flows
    annual_rate = 0.1
    quarterly_rate = annual_rate / 4
    cumulative_cash = np.cumsum(cash_flows)
    finance = Finance()
    npv = finance.npv(quarterly_rate, cash_flows)
    irr_quarterly = finance.irr_quarterly(cash_flows)
    irr_annually = finance.irr_annually(irr_quarterly)
    payback_quarter = finance.payback_period(cumulative_cash)
    payback_fractional = finance.fractional_payback(cumulative_cash, payback_quarter, cash_flows)
    print(npv)
    print(irr_quarterly)
    print(irr_annually)
    print(payback_quarter)
    print(payback_fractional)