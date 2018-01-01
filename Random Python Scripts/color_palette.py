#!/usr/bin/env python

from helpers import *

from mobject.tex_mobject import TexMobject
from mobject import Mobject
from mobject.image_mobject import ImageMobject
from mobject.vectorized_mobject import *

from animation.animation import Animation
from animation.transform import *
from animation.simple_animations import *
from animation.playground import *
from topics.geometry import *
from topics.characters import *
from topics.functions import *
from topics.number_line import *
from topics.combinatorics import *
from scene import Scene
from camera import Camera
from mobject.svg_mobject import *
from mobject.tex_mobject import *

from mobject.vectorized_mobject import *

class ColorPalette(Scene):
    def construct(self):
        ## It takes a lot of memory to run a preview of it, so
        ## just running -s is good enough to take a look at the
        ## final image
        
        row = 0
        col = 0
        for key, value in COLOR_MAP.iteritems():            
            # Rectangle for every color
            rect = Square(stroke_width = 0.5,
                          color = DARK_BLUE,
                          fill_opacity = 1,
                          fill_color = value,
                          side_length = 1)
            rect.to_corner(UP+LEFT)
            rect.shift(DOWN * col + RIGHT * row)

            # Text for every color
            text = TextMobject("\\textbf{" + key.replace("_", "\\\\") + "}",
                               stroke_width = 1,
                               color = BLACK);
            text.scale(0.3).next_to(rect, ORIGIN)

            # Draw them
            self.play(DrawBorderThenFill(rect))
            self.play(Write(text))

            # Keep track of rows and cols
            if row == 9:
                col += 1
                row = 0
            else:
                row += 1
