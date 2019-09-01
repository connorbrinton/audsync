from abc import ABC, abstractmethod
from typing import Iterable, List, Tuple

import numpy as np


class Synchronizer(ABC):
    @abstractmethod
    def sync(texts: Iterable[str], audio: Tuple[np.ndarray, float]) -> List[Tuple[float, float]]:
        """
        Compute start and end times for each text segment in the given audio.

        Parameters:
            texts: List of text segments which should be aligned to audio.
            audio: Audio loaded by LibROSA to which text should be aligned.

        Returns:
            List of ``(start_time, end_time)`` pairs, one for each text segment in ``texts``.
        """
