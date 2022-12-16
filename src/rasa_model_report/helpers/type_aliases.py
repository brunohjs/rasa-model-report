from typing import Union, Dict, List

number = Union[int, float]
intent = Dict[str, Union[number, str, None]]
entity = Dict[str, Union[number, Dict[str, number], None]]
nlu_payload = Dict[str, Union[intent, List[intent], str, number, None]]
