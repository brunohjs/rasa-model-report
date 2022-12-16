from typing import Dict
from typing import List
from typing import Union

number = Union[int, float]
intent = Dict[str, Union[number, str, None]]
entity = Dict[str, Union[number, Dict[str, number], None]]
nlu_payload = Dict[str, Union[intent, List[intent], str, number, None]]
