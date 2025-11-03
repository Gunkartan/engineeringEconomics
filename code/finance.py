import numpy as np
import numpy_financial as npf

class Finance:
    def npv(self, quarterly_rate: float, cash_flows: list[int]) -> float:
        return npf.npv(quarterly_rate, cash_flows)
    
    def irr_quarterly(self, cash_flows: list[int]) -> float:
        return npf.irr(cash_flows)
    
    def irr_annually(self, irr_quarterly: float) -> float:
        m = 4

        return m * ((1 + irr_quarterly) ** (1 / m) - 1)
    
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
    net_cash_flows = [-1326, 288, 955, 2321, -482, 610, 669, 1500, -877, -847, 790]
    cash_flows = [initial_investment] + net_cash_flows
    annual_rate = 0.1
    quarterly_rate = annual_rate / 4
    cumulative_cash = np.cumsum(cash_flows)
    finance = Finance()
    npv = finance.npv(quarterly_rate, cash_flows)
    irr_quarterly = finance.irr_quarterly(cash_flows)
    irr_annually = finance.irr_annually(irr_quarterly)
    payback_quarter = finance.payback_period(cumulative_cash)
    payback_fractional = finance.fractional_payback(cumulative_cash, payback_quarter, cash_flows)
    print(f'The NPV is {npv:.3f} million USD.')
    print(f'The quarterly IRR is {irr_quarterly:.3f}.')
    print(f'The annual IRR is {irr_annually:.3f}.')
    print(f'The payback period is {payback_quarter} quarters.')
    print(f'The fractional payback period is {payback_fractional:.3f} quarters.')