# gui_inputs/pc_mail.py
from .common import InputField

FIELDS = [
    InputField("product", "Product", "dropdown"),
    InputField("series", "Series", "text"),
    InputField("issuer", "Issuer", "dropdown"),
    InputField("currency", "Currency", "dropdown"),
    InputField("client", "Client", "dropdown"),
    InputField("distributor", "Distributor", "dropdown"),
    InputField("underlyings", "Underlyings", "multiselect"),
]