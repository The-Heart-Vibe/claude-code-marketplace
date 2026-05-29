"""market_size — TAM / SAM / SOM + key market stats.

Toolkit question: "Jak duży jest rynek, który wcześniej zdefiniowaliście?
Jakie wolumeny osiąga? Jakie są kluczowe wartości liczbowe?"
"""
from ._base import dispatch

build = dispatch("stat_pair")
