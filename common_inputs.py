# gui_inputs/common.py
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class InputField:
    key: str
    label: str
    type: str              # "text", "dropdown", "number", "multiselect"
    values: Optional[List[str]] = None
    required: bool = True



# gui_inputs/common.py
from .common import InputField

# gui_inputs/shared_fields.py

SHARED_FIELDS = [
    InputField("product_type", "Product type", "dropdown"),
    InputField("maturity", "Maturity", "dropdown"),
    InputField("underlying", "Underlying", "text"),
    InputField("currency", "Currency", "dropdown"),
    InputField("issuer", "Issuer", "dropdown"),
]