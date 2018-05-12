
# https://gist.github.com/nhmc/0537027242dd66e47002

def calc_monthly_payment(P, nyear, rate_year_perc):
    """ Find the monthly payments for a loan.
    
    Parameters
    ----------
    P : float
      The loan amount (principle).
    nyear : float
      Length of the loan in years
    rate_year_perc : float
      The yearly interest rate as a percentage (e.g. 5 if 5%).
    
    """
    rate_month = rate_year_perc / 100. / 12.
    nmonth = nyear * 12.
    term = (1 + rate_month)**nmonth
    return P * rate_month * term / (term - 1)
        
        
def calc_amort(P, rate_year_perc, mp, offset, offset_start_year=0, offset_end_year=None):
    """
    Calculate monthly amortizations, with and without an offset.
    
    Parameters
    ----------
    P : float
      Principle (the amount you borrow) in $
    rate_year_perc : float
      Yearly interest rate (percent)
    mp : float
      Monthly payment in $
    offset : float 
      Amount in the offset account in $
    offset_start_year : float (0) 
      The year the offset amount starts
    offset_end_year : float (None)
      The year the offset amount ends
    
    Returns
    -------
    M : dict
    """
    M = {}
    M['rate_year_perc'] = rate_year_perc
    M['rate_year'] = rate_year_perc / 100.
    M['rate_month'] = M['rate_year'] / 12.
    M['P'] = [P]
    M['P_off'] = [P]
    start_off = offset_start_year * 12
    if offset_end_year is None:
        end_off = 1e99
    else:
        end_off = offset_end_year * 12
    # the number of months for the loan to be paid off with an offset. 
    nmonth_offset = 0
    n = 0
    r = M['rate_month']
    paid = 0
    paidoff = 0
    while M['P'][-1] > 0: 
        dP = mp - M['P'][-1] * r
        payment = (mp if M['P'][-1] - dP > 0 else M['P'][-1])
        paid += payment
        M['P'].append(M['P'][-1] - dP)
        if M['P_off'][-1] > 0:
            if start_off < n < end_off:
                dPoff = mp - (M['P_off'][-1] - offset) * r
                nmonth_offset += 1
            else:
                dPoff = mp - M['P_off'][-1] * r
            p = M['P_off'][-1] - dPoff
            if p < 0:
                p = 0
            M['P_off'].append(p)
            payment = (mp if M['P_off'][-1] - dPoff > 0 else M['P_off'][-1])
            paidoff += payment
            
        n += 1
        if n > 1e6:
            s = 'Too many iterations!'
            raise RuntimeError(s)

    M['nmonth'] = n
    M['nyear'] = n / 12.
    M['nyear_offset'] = nmonth_offset / 12.
    M['total_paid_offset'] = paidoff
    M['total_paid'] = paid
    M['monthly_payment'] = mp
    M['offset'] = offset
    return M
    
    
    
if __name__ == '__main__':
    
    print('funcs.py')
    
    