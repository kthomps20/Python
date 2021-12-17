import mingus.extra.LilyPond as LilyPond
from mingus.containers import Bar

b = Bar()
bar = LilyPond.from_Bar(b)
LilyPond.to_png(bar, "my_first_bar")