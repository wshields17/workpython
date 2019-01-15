import QuantLib as ql

maturity_date = ql.Date(18, 1, 2019)
spot_price = 155
strike_price = 155
volatility = 0.20 # the historical vols for a year
dividend_rate =  0.0
option_type = ql.Option.Call

risk_free_rate = 0.02
day_count = ql.Actual365Fixed()
calendar = ql.UnitedStates()

calculation_date = ql.Date(10,1,2019)
ql.Settings.instance().evaluationDate = calculation_date

payoff = ql.PlainVanillaPayoff(option_type, strike_price)
exercise = ql.AmericanExercise(calculation_date,maturity_date)
american_option = ql.VanillaOption(payoff, exercise)

spot_handle = ql.QuoteHandle(
    ql.SimpleQuote(spot_price)
)
flat_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, risk_free_rate, day_count)
)
dividend_yield = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, dividend_rate, day_count)
)
flat_vol_ts = ql.BlackVolTermStructureHandle(
    ql.BlackConstantVol(calculation_date, calendar, volatility, day_count)
)
bsm_process = ql.BlackScholesMertonProcess(spot_handle, dividend_yield, flat_ts, flat_vol_ts)

#european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
#bs_price = european_option.NPV()
#print ("The theoretical price is ", bs_price)

def binomial_price(bsm_process, steps):
    binomial_engine = ql.BinomialVanillaEngine(bsm_process, "crr", steps)
    american_option.setPricingEngine(binomial_engine)
    
    return american_option.NPV()
steps = int(input('Steps  '))
bpr = binomial_price(bsm_process,steps)
print("the binomial price is ", bpr)    