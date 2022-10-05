from typing import Callable, Iterable

# import heuristic implementations here
from .count import event_count, message_count
from .ratio import average_message_length, message_to_command_ratio
from .zhu import avg_num_words_between_commands, num_participants

# register heuristic implementations here
__all__ = (
    "event_count",
    "message_count",
    "message_to_command_ratio",
    "average_message_length",
    "avg_num_words_between_commands",
    "num_participants",
)

# typing helpers
Heuristic = Callable[[Iterable[dict]], int | float]
