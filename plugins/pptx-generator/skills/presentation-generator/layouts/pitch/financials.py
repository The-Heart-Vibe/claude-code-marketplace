"""financials — P&L forecast + key metrics.

Toolkit question: "Jak prezentuje się Wasz model finansowy?"
"""
from ._base import dispatch

build = dispatch("table_grid")
