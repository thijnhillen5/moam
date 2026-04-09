# gui_inputs/marketing.py
from .common import InputField

FIELDS = [
    InputField("title", "Mail title", "text"),
    InputField("intro_text", "Intro text", "text"),
    InputField("product_type", "Product type", "dropdown"),
    InputField("issuer", "Issuer", "dropdown"),
    InputField("currency", "Currency", "dropdown"),
    InputField("maturity", "Maturity", "dropdown"),
]