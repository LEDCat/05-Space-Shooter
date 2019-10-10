import sys, logging, open_color, arcade, random, time

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Untitled Wolf Game"

#GAME DEFINE
STARTING_LOCATION = (400,100)

class Animate(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.frequency = 1 #update every second        
        self.timer = time.time()
        running = ['Wolf_Run_1','Wolf_Run_2','Wolf_Run_3','Wolf_Run_4','Wolf_Run_5','Wolf_Run_6']
        self.runRange = len(running)-1
        for e in running:
            texture = arcade.load_texture("assets/emote/Wolf_Run_{0}.png".format(e), scale=1)
            self.textures.append(texture)
        whichTexture = random.randint(0,self.runRange)
        self.set_texture(whichTexture)

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("assets/Wolf/Wolf_Run_1.png", 0.5)
        (self.center_x, self.center_y) = STARTING_LOCATION


class Window(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(open_color.white)

        self.animal_list = arcade.SpriteList()

        #
        self.set_mouse_visible(True)
        arcade.set_background_color(open_color.green_4)
        self.player = Player()
        self.score = 0


    def setup(self):
        self.animal_sprite = arcade.Sprite("assets/Wild Animals/Wolf/Wolf_Run.png", 0.5)
        self.animal_sprite.center_x = 400
        self.animal_sprite.center_y = 300
        self.animal_list.append(self.animal_sprite)
        #pass 

        now = time.time()
        #update once per minute
        if (now - self.timer) >= self.frequency:
            self.timer = time.time()
            whichTexture = random.randint(0,self.emoteRange)
            self.set_texture(whichTexture)
        #pass

    def update(self, delta_time):
        self.animal_list.update()
        

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.animal_list.draw()
        self.player.draw()



    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            print("Left")
        elif key == arcade.key.RIGHT:
            print("Right")
        elif key == arcade.key.UP:
            print("Up")
        elif key == arcade.key.DOWN:
            print("Down")

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        pass


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()