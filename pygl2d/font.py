#===============================================================================
# This file is part of PyGL2D.
# Copyright (C) 2008 PyMike <pymike93@gmail.com>
# Copyright (C) 2012 Ryan Hope <rmh3093@gmail.com>
#
# PyGL2D is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyGL2D is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyGL2D.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from . import image
import pygame

from OpenGL.GL import *
from OpenGL.GLU import *

class RenderText(object):
    
    def __init__(self, text, color, font):
        """Create a new font render <- return None
        """
        
        self.font = font
        self.text = text
        self.color = color
        self.ren = image.Image(self.font.render(self.text, 1, self.color))
    
    def change_text(self, text, color="default"):
        """Change the font render's text. <- return None
        """
        
        glDeleteTextures([self.ren.texture])
        del self.ren
        if color == "default":
            color = self.color
        self.color = color
        self.text = text
        self.ren = image.Image(self.font.render(self.text, 1, self.color))
    
    def draw(self, pos):
        """Draw the font rendered image. <- return None
        """
        
        self.ren.draw(pos)
    
    def rotate(self, rotation):
        """Rotate the font rendered image. <- return None
        """
        
        self.ren.rotate(rotation)
    
    def scale(self, scale):
        """Scale the font rendered image. <- return None
        """
        
        self.ren.scale(scale)
    
    def colorize(self, r, g, b, a):
        """Color the font rendered image. <- return None
        """
        
        self.ren.colorize(r, g, b, a)
    
    def delete(self):
        """Delete the font rendered image from the memory. <- return None
        """
        
        self.ren.delete()
        del self
    
    def get_width(self):
        """Returns the width of the font rendered image. <- return int
        """
        
        return self.ren.get_width() * self.ren.scalar
    
    def get_height(self):
        """Returns the height of the font rendered image. <- return int
        """
        
        return self.ren.get_height() * self.ren.scalar
    
    def get_rect(self):
        """Get the rect of the font rendered image. <- return rect.Rect
        """
        
        return pygame.rect.Rect(0, 0, self.get_width(), self.get_height())

