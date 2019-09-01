from typing import Iterable, List, Tuple

import numpy as np

from .synchronizers import get_synchronizer


def sync(tool_name: str, texts: Iterable[str], audio: Tuple[np.ndarray, float]) -> List[Tuple[float, float]]:
    """
    Compute start and end times for each text segment in the given audio.

    Parameters:
        tool_name: Name of tool to use for forced alignment. Currently supported values include ``"aeneas"``.
        texts: List of text segments which should be aligned to audio.
        audio: Audio loaded by LibROSA to which text should be aligned.

    Returns:
        List of ``(start_time, end_time)`` pairs, one for each text segment in ``texts``.
    """
    # Retrieve synchronizer with given ``tool_name``
    synchronizer = get_synchronizer(tool_name)

    # Use the synchronizer to synchronize the text and the audio
    return synchronizer.sync(texts, audio)
