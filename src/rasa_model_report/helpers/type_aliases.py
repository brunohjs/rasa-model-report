number = int | float
intent = dict[str, number | str | None]
entity = dict[str, number | dict[str, number] | None]
nlu_payload = dict[str, intent | list[intent] | str | number | None]
