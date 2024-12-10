def inversare_sir(sir):
    if len(sir) > 0:
        return sir[-1] + inversare_sir(sir[:-1])
    return sir
