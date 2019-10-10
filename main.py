import sys, logging, open_color, arcade, random, time

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Untitled Hunter Game"

#GAME DEFINE
NUM_ENEMIES = 5
STARTING_LOCATION = (400,100)
BULLET_DAMAGE = 10
ENEMY_HP = 100
HIT_SCORE = 10
KILL_SCORE = 100


class Bullet(arcade.Sprite):
    def __init__(self, position, velocity, damage):
        ''' 
        initializes the bullet
        Parameters: position: (x,y) tuple
            velocity: (dx, dy) tuple
            damage: int (or float)
        '''
        super().__init__("assets/Arrow.png", 0.5)
        (self.center_x, self.center_y) = position
        (self.dx, self.dy) = velocity
        self.damage = damage

    def update(self):
        '''
        Moves the bullet
        '''
        self.center_x += self.dx
        self.center_y += self.dy

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("assets/ForestRanger.png", 0.5)
        (self.center_x, self.center_y) = STARTING_LOCATION

class Enemy(arcade.Sprite):
    def __init__(self, position):
        '''
        initializes a enemy
        Parameter: position: (x,y) tuple
        '''
        super().__init__()
        self.frequency = 0.2 #update under a second        
        self.timer = time.time()
        running = ['Wolf_Run_2','Wolf_Run_3','Wolf_Run_4','Wolf_Run_5','Wolf_Run_6']
        self.runRange = len(running)-1
        for e in running:
            texture = arcade.load_texture("assets/Wolf/{0}.png".format(e), scale=1)
            self.textures.append(texture)
        whichTexture = random.randint(0,self.runRange)
        self.set_texture(whichTexture)

        self.hp = ENEMY_HP
        (self.center_x, self.center_y) = position
    
    def update(self):
        now = time.time()
        #update once per minute
        if (now - self.timer) >= self.frequency:
            self.timer = time.time()
            whichTexture = random.randint(0,self.runRange)
            self.set_texture(whichTexture)

class Window(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(open_color.white)

        self.enemy_list = arcade.SpriteList()
        self.run_list = arcade.SpriteList()
        #
        self.set_mouse_visible(True)
        arcade.set_background_color(open_color.green_4)
        self.player = Player()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.score = 0

    def setup(self): 
        self.run_sprite = Animate()
        self.run_sprite.center_x = 320
        self.run_sprite.center_y = 360
        self.run_list.append(self.run_sprite)

    def setup(self):
        for i in range(NUM_ENEMIES):
            x = 120 * (i+1) + 40
            y = 500
            wolf = Enemy((x,y))
            self.enemy_list.append(wolf)

    def update(self, delta_time):
        self.enemy_list.update()
        self.run_list.update()
        self.enemy_list.update()

        self.bullet_list.update()
        for e in self.enemy_list:
            damage = arcade.check_for_collision_with_list(e, self.bullet_list)
            for d in damage:
                e.hp = e.hp - d.damage
                d.kill()
                if e.hp < 0:
                    e.kill()
                    self.score = self.score + KILL_SCORE
                else:
                    self.score = self.score + HIT_SCORE
            pass


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.bullet_list.draw()
        self.enemy_list.draw()
        self.run_list.draw()
        self.player.draw()



    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.player.center_x = x
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            x = self.player.center_x
            y = self.player.center_y + 15
            bullet = Bullet((x,y),(0,10),BULLET_DAMAGE)
            self.bullet_list.append(bullet)
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
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()