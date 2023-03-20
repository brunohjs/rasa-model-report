from typing import Dict
from typing import List
from typing import Union


intent = Dict[str, Union[float, str, None]]
entity = Dict[str, Union[float, Dict[str, float], None]]
nlu_payload = Dict[str, Union[intent, List[intent], str, float, None]]
