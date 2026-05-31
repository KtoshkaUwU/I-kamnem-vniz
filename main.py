import spritePro as s
import random


class GameScreen(s.Scene):
    def __init__(self):
        super().__init__()
        self.bg = s.Sprite('room.jpg', pos=s.WH_C, size=s.WH, scene=self)
        self.player = s.Sprite('astolfo.png', pos=(100, 300), size=(50, 50), scene=self)
        self.player_body = s.add_physics(self.player, s.PhysicsConfig(bounce=0.8))

        self.pipes = []
        # self.mini_players = []
        self.spawn_timer = s.Timer(2.0, self.spawn_pipes, repeat = True, scene=self)
        self.spawn_pipes()
        # self.spawn_mini_player()
        self.is_game_over = False
        s.physics.set_gravity(980)
        s.physics.set_bounds(s.pygame.Rect(0,0, 400, 600))

    def update(self,dt):

        if self.is_game_over:
            if s.input.was_pressed(s.pygame.K_y):
                s.restart_scene()
            return
        if s.input.was_pressed(s.pygame.K_SPACE) or s.input.was_mouse_pressed(1):
            self.player_body.velocity.y = -400.6769

        if s.input.was_pressed(s.pygame.K_d):
            self.player_body.velocity.x = +6900.6769
        if s.input.was_pressed(s.pygame.K_a):
            self.player_body.velocity.x = -6900.6769
        if s.input.was_pressed(s.pygame.K_s):
            self.player_body.velocity.y = +6900.6769
        if s.input.was_pressed(s.pygame.K_w):
            self.player_body.velocity.y = -6900.6769
        
        if s.input.was_pressed(s.pygame.K_r):
            self.player_body.velocity.y = 0
            self.player_body.velocity.x = 0
        
        # if s.input.was_pressed(s.pygame.K_e):
        #     self.spawn_player()


        for pipe in self.pipes:
            pipe.x -= 200 * s.dt
            if self.player.collides_with(pipe):
                self.trigger_game_over()

        for pipe in self.pipes[:]:
            if pipe.x < -100:
                pipe.kill()
                self.pipes.remove(pipe)
        if self.player.y > s.WH[1] or self.player.y < 0:
            self.trigger_game_over()
    
    def trigger_game_over(self):
        if self.is_game_over:
            return
        self.is_game_over = True
        self.player_body.velocity.y = 0
        s.TextSprite('Игра окончена.', pos=s.WH_C, font_size=40, color=(255,255,255), scene=self, sorting_order=30)
        s.TextSprite('Нажмите Y для рестарта', pos=(s.WH_C[0], s.WH_C[1]+50), font_size=20, color=(255,255,255), scene=self, sorting_order=30)

    def spawn_pipes(self):
        gap_y = random.randint(200,400)
        gap_size = 180
        pipe_x = 450

        top = s.Sprite('Femboy_flag.png', pos=(pipe_x, gap_y - gap_size/2 - 300), size=(80, 600), scene=self, sorting_order = 5)
        top.angle = 180
        bottom = s.Sprite('Femboy_flag.png', pos=(pipe_x, gap_y + gap_size/2 + 300), size=(80, 600), scene=self, sorting_order = 5)

        self.pipes.extend([top,bottom])
    
    # def spawn_mini_player(self):
    #     mini_player = s.Sprite('astolfo.png', pos=(self.player_body.velocity.x, self.player_body.velocity.y), size=(30, 30), scene=self)
    #     mini_player_body = s.add_physics(self.mini_player, s.PhysicsConfig(bounce=0.9))

    #     self.mini_players.extend([mini_player])


if __name__ == '__main__':
    s.run(scene=GameScreen, size=(400, 600), title='i kamnem vniz.jpg', fps=69)
