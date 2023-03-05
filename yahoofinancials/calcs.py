def eps(price_data, pe_ratio):
    if price_data is not None and pe_ratio is not None:
        return price_data / pe_ratio
    else:
        return None


def num_shares_outstanding(cur_market_cap, today_low, today_high, price_type, current):
    if cur_market_cap is not None:
        if price_type == 'current' and current is not None:
            today_average = current
        elif price_type == 'current' or today_high is None or today_low is None:
            return None
        else:
            today_average = (today_high + today_low) / 2
        return cur_market_cap / today_average
    else:
        return None
