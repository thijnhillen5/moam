# gui_inputs/documentatie.py
from .common import InputField
from .common_inputs import COMMON_FIELDS

FIELDS = COMMON_FIELDS + [
    InputField("maturity", "Maturity", "dropdown"),
    InputField("underlying", "Underlying", "text"),
    InputField("trades", "Trades", "multiselect"),
]