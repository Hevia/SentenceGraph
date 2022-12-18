# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_functional.ipynb.

# %% auto 0
__all__ = ['create_text_nodes']

# %% ../nbs/01_functional.ipynb 2
from typing import List
from .core import TextNode

# %% ../nbs/01_functional.ipynb 3
def create_text_nodes(texts: List[str]) -> List[TextNode]:
    """ Creates a list of TextNodes from a list of strings """
    return [TextNode(count, text) for count, text in enumerate(texts)]
