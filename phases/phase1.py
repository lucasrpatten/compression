"""
    Contains the phase1 class
"""

from itertools import combinations
from collections import Counter
from functools import lru_cache
import time

# import numpy as np

from .Phase import Phase


class Phase1(Phase):
    """
        First phase - English Analysis and Linguistics
    """

    def __init__(self, original_text):
        initial_time = time.time()
        Phase.__init__(self, original_text)
        self.text = original_text
        self.frequencies = self.generic_frequency()
        self.top1000 = self.frequencies.most_common(1000)
        self.identifiers = self.find_available_identifiers()
        self.top1k_saved_space = self.space_saved(tuple(self.top1000))
        self.top_substrings = self.all_substrings()
        self.top_space_saved = self.space_saved(tuple(self.top_substrings.most_common(10000)))
        total_time = time.time() - initial_time
        print(f"Phase 1 initialization completed in {total_time:.3f} seconds")

    def generic_frequency(self, min_length=4):
        """
        Find the generic (regular) frequency of words in the text

        Returns:
            Counter: list of the most common words and their frequencies
        """
        words = (i for i in self.text.split() if len(i) >= min_length)
        most_common = Counter(words)
        return most_common

    def find_available_identifiers(self):
        """
        Finds available identifiers that aren't in the default text

        Returns:
            filter[str]: List of the unused identifiers
        """
        ascii_characters = (chr(i) for i in range(256))
        unused = (''.join(i) for i in combinations(ascii_characters, 3))
        unused = filter(lambda x:  x not in self.text, unused)
        return unused

    def space_saved(self, to_calc):
        """
        Find which replacement words would save the most space

        Args:
            to_calc (tuple[tuple[Unknown, int]], required): Tuple of tuples of strings and ints

        Returns:
            list[tuple[Unknown, int]]: List of tuples formatted as (string, saved_space)
        """
        space_saved = ((v, (len(v)-3)*i-(len(v)+4)) for v, i in to_calc)
        space_saved = sorted(space_saved, key=lambda x: x[1], reverse=True)
        return space_saved

    def all_substrings(self, min_length=4, max_length=16):
        """
        Get all the substrings that are contained in the text between the min_length and max_length

        Args:
            min_length (int, optional): Minimum Substring Length. Defaults to 4.
            max_length (int, optional): Maximum Substring Length. Defaults to 16.

        Returns:
            Counter: Counter of substrings in string
        """
        get_substr = (self.text[i:i+length] for length in range(min_length, max_length + 1)
                      for i in range(len(self.text) - length + 1))
        substrings = Counter(get_substr)
        return substrings
