from datetime import date
from staticsd.documentatie import ADVISER_HELPERS


def build_subject(data):
    year_start = data["today"].year % 100
    maturity_num = int(data["maturity"].replace("Y", ""))
    year_end = year_start + maturity_num

    ow = " / ".join(data.get("underlyings", []))

    subject = f"Documentatie {data['issuer']} {data['product']}"
    if ow:
        subject += f" {ow}"
    subject += f" {year_start} - {year_end}"

    if data.get("isin"):
        subject += f" – {data['isin']}"

    return subject


def greeting(trades):
    if len(trades) == 1:
        first_name = trades[0]["adviser"].split(" ")[0]
        return f"Hi {first_name},"
    return "Hi all,"


def build_rtd_list(data):
    rows = []
    for t in data["trades"]:
        price = t.get("price") or "100"
        rows.append(
            f"<li>{data['currency']} {t['amount']} @{price}% voor {t['adviser']}</li>"
        )

    return (
        "<ul style='padding-left:20px; margin-top:0; margin-bottom:0;'>"
        + "".join(rows)
        + "</ul>"
    )


def derive_cc_from_trades(trades):
    cc = set()
    for t in trades:
        helper = ADVISER_HELPERS.get(t["adviser"])
        if helper:
            cc.add(helper)
    return sorted(cc)


def build_body(data):
    trades = data["trades"]
    adviser_count = len(trades)

    greet = greeting(trades)
    have_text = "Je hebt" if adviser_count == 1 else "Jullie hebben"

    eid_url = (
        "https://api.priiphub.com/hub/priip/document"
        f"?documentType=pdf&identifier={data['isin']}"
        "&country=NL&language=NL&response=document"
    )

    rtd_list = build_rtd_list(data)
    vlk_code = data["vlk_code"]
    sender = data["sender_name"]
    product = data["product"]

    # ---------------- PRODUCT CASES ----------------
    if "Trigger" in product:
        product_name = "Trigger Note"
        brochure = (
            "https://markets.vanlanschotkempen.com/uploadedfiles/Documents/"
            "FvL%2025205%20BRO%20SP%20Trigger%20Notes.pdf"
        )
        video = "https://vimeo.com/765679154"

        video_html = (
            f"Link naar Trigger Note video: "
            f"<a href='{video}'>Hoe werkt een Trigger note?</a><br>"
        )

    elif "Memory" in product:
        product_name = "Memory Coupon Note"
        brochure = (
            "https://markets.vanlanschotkempen.com/uploadedfiles/Documents/"
            "FvL%2025329%20BRO%20Memory%20Coupon%20Notes.pdf"
        )
        video_html = ""

    else:
        product_name = "Index Garantie Note"
        brochure = (
            "https://markets.vanlanschotkempen.com/uploadedfiles/Documents/"
            "FvL%2025326%20BRO%20Index%20Garantie%20Notes.pdf"
        )
        video = "https://vimeo.com/765678480"

        video_html = (
            f"Link naar Index Garantie Note video: "
            f"<a href='{video}'>Hoe werkt een Garantie note?</a><br>"
        )

    # ---------------- HTML BODY ----------------
    body_html = f"""
<html>
<body style="font-family:Segoe UI; font-size:11pt">
<p>{greet}</p>

<p>{have_text} onlangs voor een klant het maatwerkproduct aangekocht.</p>

<p>
Hierbij de generieke {product_name} brochure, het inlegvel, de Final Terms
en een link naar het Essentiële-informatiedocument voor deze Maatwerk Note.
</p>

<p>
De Final Terms, inlegvel, de generieke {product_name} brochure en een link
naar het Essentiële-informatiedocument kunnen met de begeleidende brief
van Van Lanschot naar de klant worden gestuurd.
</p>

<div style="margin:0; padding:0;">
{video_html}
Link naar {product_name} brochure:
<a href="{brochure}">Brochure {product_name}</a><br>
Link naar het EID:
<a href="{eid_url}">{eid_url}</a>
</div>

<br>

<p>Graag onderstaande trades RTD inleggen:</p>
{rtd_list}

<br>

<p>De VL code is: <b>{vlk_code}</b></p>

<p>Groet,<br>{sender}</p>
</body>
</html>
"""

    return body_html
