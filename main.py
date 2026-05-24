import spritePro as s

class GameScreen(s.Scene):
    def __init__(self):
        super().__init__()
        self.bg = s.Sprite('room.jpg', pos=s.WH_C, size=s.WH, scene=self)
        self.player = s.Sprite('astolfo.png', pos=(100, 300), size=(50, 50), scene=self)
        self.player_body = s.add_physics(self.player, s.PhysicsConfig(bounce=0.8))
        s.physics.set_gravity(980)
        s.physics.set_bounds(s.pygame.Rect(0,0, 400, 600))

    def update(self,dt):
        if s.input.was_pressed(s.pygame.K_SPACE) or s.input.was_mouse_pressed(1):
            self.player_body.velocity.y = -400
s.run(scene=GameScreen, size=(400, 600), title='i kamnem vniz.jpg')