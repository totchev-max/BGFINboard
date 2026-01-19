def run_demo_year(profile, levers):
    gdp = profile["macro"]["gdp_nominal_bn"]
    debt = profile["debt"]["debt_stock_bn"]

    revenues = sum(profile["revenues"].values())
    expenditures = (
        profile["expenditures"]["Admin_wages_total"]
        + profile["expenditures"]["Pensions"]
        + profile["expenditures"]["Capex"]
        + profile["expenditures"]["Other"]
    )

    # --- Apply policy levers ---
    expenditures += profile["expenditures"]["Admin_wages_total"] * (levers["admin_wages_pct"] / 100)
    expenditures += profile["expenditures"]["MON_wages"] * (levers["mon_wages_pct"] / 100)
    expenditures += profile["expenditures"]["Pensions"] * (levers["pensions_pct"] / 100)
    expenditures += levers["capex_bn"]

    if levers["vat_rate_to"] != levers["vat_rate_from"]:
        vat_base = profile["revenues"]["VAT"]
        revenues += vat_base * ((levers["vat_rate_to"] / levers["vat_rate_from"]) - 1)

    deficit = expenditures - revenues

    return {
        "revenues": revenues,
        "expenditures": expenditures,
        "deficit": deficit,
        "deficit_pct": deficit / gdp,
        "debt_pct": debt / gdp
    }
