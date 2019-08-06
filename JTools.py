import pygame
import math
class keyboard:
    def __init__(self, trackKeys):
        keys = {'HELP': 315, 'LSHIFT': 304, 'RSHIFT': 303, 'LESS': 60, 'PAGEUP': 280, 'RCTRL': 305, 'INSERT': 277, 'RIGHTPAREN': 41, 'BACKQUOTE': 96, 'HOME': 278, 'LCTRL': 306, 'RMETA': 309, 'MINUS': 45, 'F9': 290, 'SYSREQ': 317, 'SEMICOLON': 59, 'QUOTE': 39, 'ASTERISK': 42, 'BACKSLASH': 92, 'F7': 288, '0': 48, '2': 50, 'PLUS': 43, '4': 52, 'TAB': 9, '6': 54, '5': 53, 'LEFT': 276, 'RIGHTBRACKET': 93, 'HASH': 35, 'LEFTBRACKET': 91, 'KP_DIVIDE': 267, 'CLEAR': 12, 'PERIOD': 46, 'CAPSLOCK': 301, 'RIGHT': 275, '8': 56, 'SLASH': 47, 'ESCAPE': 27, 'd': 100, 'F1': 282, 'F2': 283, 'b': 98, 'F4': 285, 'GREATER': 62, 'F6': 287, 'f': 102, 'F8': 289, 'h': 104, 'j': 106, 'l': 108, 'n': 110, 'BREAK': 318, 'p': 112, 'r': 114, 't': 116, 'v': 118, 'x': 120, 'z': 122, 'DELETE': 127, 'CARET': 94, 'EXCLAIM': 33, 'RETURN': 13, 'KP_PERIOD': 266, 'F3': 284, 'DOWN': 274, 'COLON': 58, 'BACKSPACE': 8, 'UNDERSCORE': 95, 'PRINT': 316, 'LSUPER': 311, 'KP0': 256, 'KP1': 257, 'KP2': 258, 'KP3': 259, 'KP4': 260, 'KP5': 261, 'KP6': 262, 'KP7': 263, 'KP8': 264, 'KP9': 265, 'QUESTION': 63, 'KP_ENTER': 271, 'RSUPER': 312, '1': 49, '3': 51, 'COMMA': 44, 'PAGEDOWN': 281, '7': 55, '9': 57, 'LALT': 308, 'F5': 286, 'QUOTEDBL': 34, 'PAUSE': 19, 'END': 279, 'SPACE': 32, 'LEFTPAREN': 40, 'MODE': 313, 'DOLLAR': 36, 'EQUALS': 61, 'LMETA': 310, 'POWER': 320, 'AMPERSAND': 38, 'AT': 64, 'MENU': 319, 'F12': 293, 'F13': 294, 'F10': 291, 'F11': 292, 'KP_MINUS': 269, 'F14': 295, 'F15': 296, 'a': 97, 'c': 99, 'KP_PLUS': 270, 'e': 101, 'KP_EQUALS': 272, 'g': 103, 'i': 105, 'k': 107, 'RALT': 307, 'm': 109, 'UP': 273, 'o': 111, 'q': 113, 's': 115, 'u': 117, 'w': 119, 'SCROLLOCK': 302, 'y': 121, 'NUMLOCK': 300, 'KP_MULTIPLY': 268}
        self.track = []
        self.map = {}
        self.keys = {}
        for key in trackKeys:
            self.track.append(key)
            self.map[key] = keys[key]
            self.keys[key] = False
    def updade(self, event):
        if event.type == pygame.KEYDOWN:
            for key in self.track:
                self.keys[key] = event.key == self.map[key] or self.keys[key]
        else:
            if event.type == pygame.KEYUP:
                for key in self.track:
                    self.keys[key] = not(event.key == self.map[key]) and self.keys[key]
class Jdisplay:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color
        self.clock = pygame.time.Clock()
        self.tick()
    def tick(self):
        pygame.display.flip()
        self.clock.tick()
        self.screen.fill(self.color)
def rotate(shape, angle):
    cont = 0
    size = len(shape)
    while cont < size:
        shape[cont] = [math.cos(angle) * shape[cont][0] - math.sin(angle) * shape[cont][1], math.cos(angle) * shape[cont][1] + math.sin(angle) * shape[cont][0]]
        cont = cont + 1
    return shape
def chsize(shape, constant):
    NShape = []
    for edge in shape:
        NShape.append((int(edge[0] * constant), int(constant * edge[1])))
    return NShape
def repos(shape, pos):
    posX = pos[0]
    posY = pos[1]
    cont = 0
    size = len(shape)
    while cont < size:
        shape[cont] = [shape[cont][0] + posX, shape[cont][1] + posY]
        cont = cont + 1
    return shape
def printClass(Class):
	args = dir(Class)
	for arg in args:
		arg = "print(\"" + arg + " = \" + str(Class." + arg + "))"
		exec(arg)
