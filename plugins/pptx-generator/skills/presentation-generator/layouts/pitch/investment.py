"""investment — Round size, instrument, allocation.

Toolkit question: "Ile pieniędzy zbieracie i co oferujecie w zamian? W jaki
sposób zebrane przez Was fundusze zostaną wykorzystane?"
"""
from ._base import dispatch

build = dispatch("stat_pair")
