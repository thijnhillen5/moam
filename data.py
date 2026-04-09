## kind of input for documentatie mail


from datetime import date

from datetime import date

def build_email_data(common, trades, to, cc):
    return {
        "sender_name": "Thijn",
        "product": common.product_name,
        "isin": common.isin,
        "maturity": common.maturity,
        "currency": common.currency,
        "issuer": common.issuer,
        "underlyings": [common.underlying_index],
        "trades": trades,
        "to": to,
        "cc": cc,
        "today": date.today(),

}


