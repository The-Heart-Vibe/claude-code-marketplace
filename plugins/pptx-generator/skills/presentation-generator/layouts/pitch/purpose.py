"""purpose — Company purpose / mission statement slide.

Toolkit question: "Jaki konkretny problem rynkowy chcecie rozwiązać waszym
produktem lub usługą?"

Default layout: main_point (a single bold mission statement reads strongest).
"""
from ._base import dispatch

build = dispatch("main_point")
