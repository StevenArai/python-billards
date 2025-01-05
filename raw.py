import pygame
import pymunk
import random

class Ball:
    def __init__(self, index, position, color):
        self.index = index
        self.mass = 20
        self.radius = 25
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, self.moment)
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.elasticity = 0.98
        self.body.position = position
        self.color = color
        self.texture= pygame.image.load("assets/texture/balls/{0:d}.png".format(self.index)).convert_alpha()
        self.show = True

    def draw(self, screen):
        #pygame.draw.circle(screen, self.color, (self.body.position.x, self.body.position.y), self.radius)
        if self.show:
            screen.blit(self.texture, (self.body.position.x - self.radius, self.body.position.y - self.radius))

    def apply_impulse(self, impulse):
        self.body.apply_impulse_at_local_point(impulse)

class Wall:
    def __init__(self, start, end, space):
        self.space = space
        self.shape = pymunk.Segment(self.space.static_body, start, end, 10)
        self.shape.elasticity = 0.8
        self.space.add(self.shape)

    def draw(self, screen):
        pygame.draw.line(screen, (127, 50, 0), self.shape.a, self.shape.b, 10)

class BilliardTable:
    def __init__(self, screen, space):
        self.screen = screen
        self.space = space
        self.balls = []
        self.balls_dropped = [] #balls dropped this scene
        self.ball_right = None #None FullC HalfC
        self.walls = []
        self.create_balls()
        self.create_walls()
        self.title= pygame.image.load("assets/texture/title.png").convert_alpha()
        self.collision_ball_sound = pygame.mixer.Sound("assets/sounds/collision.wav")
        self.collision_side_sound = pygame.mixer.Sound("assets/sounds/side-collision.wav")
        pygame.mixer.music.load("assets/music/netzach.wav")
        pygame.mixer.music.play(99999)
        pygame.mixer.music.set_volume(0.3)
        self.collision_handler = space.add_collision_handler(0, 0)
        self.collision_handler.begin = self.collision_callback

    def reset(self):
        self.balls_dropped = [] #balls dropped this scene
        self.ball_right = None
        row_positions = [
            [(self.screen.get_width() / 2 - 150, self.screen.get_height() / 2)],  
            [(self.screen.get_width() / 2 - 100, self.screen.get_height() / 2 - 25),
             (self.screen.get_width() / 2 - 100, self.screen.get_height() / 2 + 25)],  
            [(self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 - 50),
             (self.screen.get_width() / 2 - 50, self.screen.get_height() / 2),
             (self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 + 50)],  
            [(self.screen.get_width() / 2, self.screen.get_height() / 2 - 75),
             (self.screen.get_width() / 2, self.screen.get_height() / 2 - 25),
             (self.screen.get_width() / 2, self.screen.get_height() / 2 + 25),
             (self.screen.get_width() / 2, self.screen.get_height() / 2 + 75)],  
            [(self.screen.get_width() / 2 + 50, self.screen.get_height() / 2 - 100),
             (self.screen.get_width() / 2 + 50, self.screen.get_height() / 2 - 50),
             (self.screen.get_width() / 2 + 50, self.screen.get_height() / 2),
             (self.screen.get_width() / 2 + 50, self.screen.get_height() / 2 + 50),
             (self.screen.get_width() / 2 + 50, self.screen.get_height() / 2 + 100)]
        ]

        for i in range(0, 16):
            if i == 0:  # White ball
                ball_position = (self.screen.get_width() / 2 - 300, self.screen.get_height() / 2)
            else:
                # Assign position based on ball index
                if i == 1:
                    ball_position = row_positions[0][0]
                elif 2 <= i <= 3:
                    ball_position = row_positions[1][i - 2]
                elif 4 <= i <= 6:
                    ball_position = row_positions[2][i - 4]
                elif 7 <= i <= 10:
                    ball_position = row_positions[3][i - 7]
                elif 11 <= i <= 15:
                    ball_position = row_positions[4][i - 11]
                ball_position = ball_position[0] + 300, ball_position[1]

            self.balls[i].body.position = ball_position
            self.balls[i].show = True
            self.balls[i].body.velocity = (0, 0)

    def collision_callback(self, arbiter, space, data):
        # 获取参与碰撞的两个物体的速度
        body1_velocity = arbiter.shapes[0].body.velocity
        body2_velocity = arbiter.shapes[1].body.velocity
        # 计算相对速度的大小
        relative_velocity = body1_velocity - body2_velocity
        speed = relative_velocity.length*0.0005+0.1  # 获取速度的大小
        #self.collision_sound.play()
        channel = pygame.mixer.find_channel()
        channel.set_volume(speed)
        if(isinstance(arbiter.shapes[1],pymunk.shapes.Segment)):
            channel.play(self.collision_side_sound)

        else:
            channel.play(self.collision_ball_sound)

        return True

    def create_balls(self):
        ball_colors = [(255, 255, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 127, 0),
                      (255, 0, 0), (0, 0, 255), (0, 255, 0), (127, 0, 255), (255, 127, 127),
                      (255, 255, 127), (255, 0, 127), (0, 255, 127), (0, 127, 255),
                      (127, 255, 0), (127, 127, 255)]

        row_positions = [
            [(self.screen.get_width() / 2 - 150, self.screen.get_height() / 2)],  
            [(self.screen.get_width() / 2 - 100, self.screen.get_height() / 2 - 25),
             (self.screen.get_width() / 2 - 100, self.screen.get_height() / 2 + 25)],  
            [(self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 - 50),
             (self.screen.get_width() / 2 - 50, self.screen.get_height() / 2),
             (self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 + 50)],  
            [(self.screen.get_width() / 2, self.screen.get_height() / 2 - 75),
             (self.screen.get_width() / 2, self.screen.get_height() / 2 - 25),
             (self.screen.get_width() / 2, self.screen.get_height() / 2 + 25),
             (self.screen.get_width() / 2, self.screen.get_height() / 2 + 75)],  
            [(self.screen.get_width() / 2 + 50, self.screen.get_height() / 2 - 100),
             (self.screen.get_width() / 2 + 50, self.screen.get_height() / 2 - 50),
             (self.screen.get_width() / 2 + 50, self.screen.get_height() / 2),
             (self.screen.get_width() / 2 + 50, self.screen.get_height() / 2 + 50),
             (self.screen.get_width() / 2 + 50, self.screen.get_height() / 2 + 100)]
        ]

        for i in range(0, 16):
            if i == 0:  # White ball
                ball_position = (self.screen.get_width() / 2 - 300, self.screen.get_height() / 2)
            else:
                # Assign position based on ball index
                if i == 1:
                    ball_position = row_positions[0][0]
                elif 2 <= i <= 3:
                    ball_position = row_positions[1][i - 2]
                elif 4 <= i <= 6:
                    ball_position = row_positions[2][i - 4]
                elif 7 <= i <= 10:
                    ball_position = row_positions[3][i - 7]
                elif 11 <= i <= 15:
                    ball_position = row_positions[4][i - 11]
                ball_position = ball_position[0] + 300, ball_position[1]

            color = ball_colors[i]
            ball = Ball(i, ball_position, color)
            self.balls.append(ball)
            self.space.add(ball.body, ball.shape)

    def create_walls(self):
        wall_positions = [
            [(self.screen.get_width() / 2 + 50, self.screen.get_height() / 2 - 250),
             (self.screen.get_width() / 2 + 500 - 70, self.screen.get_height() / 2 - 250)],
            [(self.screen.get_width() / 2 - 500 + 70, self.screen.get_height() / 2 - 250),
             (self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 - 250)],
            [(self.screen.get_width() / 2 + 500, self.screen.get_height() / 2 - 250 + 70),
             (self.screen.get_width() / 2 + 500, self.screen.get_height() / 2 + 250 - 70)],
            [(self.screen.get_width() / 2 + 500 - 70, self.screen.get_height() / 2 + 250),
             (self.screen.get_width() / 2 + 50, self.screen.get_height() / 2 + 250)],
            [(self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 + 250),
             (self.screen.get_width() / 2 - 500 + 70, self.screen.get_height() / 2 + 250)],
            [(self.screen.get_width() / 2 - 500, self.screen.get_height() / 2 + 250 - 70),
             (self.screen.get_width() / 2 - 500, self.screen.get_height() / 2 - 250 + 70)],
        ]

        for pos in wall_positions:
            wall = Wall(pos[0], pos[1], self.space)
            self.walls.append(wall)

    def draw(self):
        # Draw billiard table
        pygame.draw.rect(self.screen, (0, 127, 0), (self.screen.get_width() / 2 - 500, self.screen.get_height() / 2 - 250, 1000, 500))

        # Draw holes (pockets)
        pockets = [
            (self.screen.get_width() / 2 - 500, self.screen.get_height() / 2 - 250),
            (self.screen.get_width() / 2 - 500, self.screen.get_height() / 2 + 250),
            (self.screen.get_width() / 2 + 500, self.screen.get_height() / 2 - 250),
            (self.screen.get_width() / 2 + 500, self.screen.get_height() / 2 + 250),
            (self.screen.get_width() / 2, self.screen.get_height() / 2 - 250),
            (self.screen.get_width() / 2, self.screen.get_height() / 2 + 250)
        ]
        for pocket in pockets:
            pygame.draw.circle(self.screen, (0, 0, 0), pocket, 30)

        # Draw walls
        for wall in self.walls:
            wall.draw(self.screen)

        # Draw balls
        for ball in self.balls:
            ball.draw(self.screen)

        self.screen.blit(self.title, (0,0))



class GUI:
    class GUIElement:
        def __init__(self, screen):
            self.screen = screen
            self.open = False
            self.openrate = 0  # (0~100)
            self.sigma = 0.1

        def interpolate(self):
            if self.open:
                if self.openrate < 100:
                    self.openrate += (100.1 - self.openrate) * self.sigma
                self.openrate = min(self.openrate, 100)
            else:
                if self.openrate > 0:
                    self.openrate -= (100.1 - self.openrate) * self.sigma
                self.openrate = max(self.openrate, 0)

        def draw(self):
            self.interpolate()


    class FreeBall(GUIElement):
        def __init__(self, screen):
            super().__init__(screen)
            self.surface = pygame.Surface((screen.get_width(), screen.get_height()),pygame.SRCALPHA)
            self.sigma = 0.1

        def interpolate(self):
            if self.open:
                if self.openrate < 100:
                    self.openrate += (100.1 - self.openrate) * self.sigma
                self.openrate = min(self.openrate, 100)
            else:
                if self.openrate > 0:
                    self.openrate += (-0.1 - self.openrate) * self.sigma
                self.openrate = max(self.openrate, 0)
        
        def avaliable(self, pos):
            for ball in self.balls[1:]:
                ball_pos = ball.body.position
                min_dist = 50
                if (ball_pos[0] - pos[0]) ** 2 + (ball_pos[1] - pos[1]) ** 2 < min_dist ** 2:
                    return False
            return True

        def draw(self, mouse_pos, mouse_state, balls):
            self.balls = balls
            super().draw()
            if self.openrate > 0:
                ret_val = False
                color = (0, 0, 255)
                mouse_pos_new = (min(max(mouse_pos[0], 0), self.screen.get_width()),min(max(mouse_pos[1], 0), self.screen.get_height()))

                if self.avaliable(mouse_pos_new):
                    color = (0, 255, 255)
                    if mouse_state == 1 and self.open:
                        ret_val = True
                        self.open = False
                else:
                    color = (255, 0, 0)
                self.surface.fill((0, 0, 0, 0))
                self.surface.set_alpha(self.openrate/100*500-256)
                pygame.draw.circle(self.surface, color, mouse_pos_new, 25+(1-self.openrate/100)*1280, int((125-self.openrate)))
                self.screen.blit(self.surface, (0, 0))
                return ret_val
        
    
    class SceneChange(GUIElement):
        def __init__(self, screen):
            super().__init__(screen)
            self.text1 = None
            self.text2 = None
            self.font1 = pygame.font.Font("assets/fonts/leefont.ttf", 82)
            self.font2 = pygame.font.Font("assets/fonts/leefont.ttf", 32)
            self.sigma = 0.08
            self.scene_sound = pygame.mixer.Sound("assets/sounds/scene.wav")
            self.background = pygame.image.load("assets/texture/scene_change.png").convert_alpha()
            self.surface = pygame.Surface((screen.get_width(), screen.get_height()),pygame.SRCALPHA)

        def change(self, text1, text2):
            self.surface.fill((0, 0, 0, 0))
            channel = pygame.mixer.find_channel()
            channel.set_volume(1)
            channel.play(self.scene_sound)
            self.text1 = text1
            self.text2 = text2
            self.open = True
            self.surface.blit(self.background, (0, 0))

            text1_rendered=self.font1.render(text1, True, (208, 187, 151))
            text1_rect=text1_rendered.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 5))
            self.surface.blit(text1_rendered,text1_rect)

            text2_rendered=self.font2.render(text2, True, (184, 255, 249))
            text2_rect=text2_rendered.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 100))
            self.surface.blit(text2_rendered,text2_rect)


        def draw(self):
            super().draw()  # 这里只更新状态

            if self.open and self.openrate == 100:
                #sleep(0.5)
                self.open = False  # 完全展开后关闭


            if self.openrate > 0:
                #print(f"UI interpolation with factor: {self.openrate}")  
                self.surface.set_alpha(self.openrate/100*500-256)
                w_factor = 2-(self.openrate / 100)
                h_factor = w_factor
                screen_w= self.screen.get_width()
                screen_h = self.screen.get_height()
                x_pos = (screen_w*self.openrate/100 - self.surface.get_width()) / 2
                y_pos = (screen_h*self.openrate/100 - self.surface.get_height()) / 2 
                #self.screen.blit(pygame.transform.scale(self.surface, (screen_w * w_factor, screen_h * h_factor)), (x_pos, y_pos))
                self.screen.blit(pygame.transform.smoothscale(self.surface, (screen_w * w_factor, screen_h * h_factor)), (x_pos, y_pos))


    class ScoreBoard(GUIElement):
        def __init__(self, screen):
            super().__init__(screen)
            self.roland_texture = pygame.image.load("assets/texture/figure/roland.png").convert_alpha()
            self.netzach_texture = pygame.image.load("assets/texture/figure/netzach.png").convert_alpha()
            self.roland_dark_texture = pygame.image.load("assets/texture/figure/roland_dark.png").convert_alpha()
            self.netzach_dark_texture = pygame.image.load("assets/texture/figure/netzach_dark.png").convert_alpha()
            self.pebox_texture = pygame.image.load("assets/texture/pe-box.png").convert_alpha()  
            self.active_player = "roland"
            self.roland_right = None #"FullC" or "HalfC"
            self.netzach_right = None #"FullC" or "HalfC"
            self.font = pygame.font.Font("assets/fonts/leefont.ttf", 36)

        def opposite_color(self, color):
            if color == "FullC":
                return "HalfC"
            elif color == "HalfC":
                return "FullC"
            else:
                return None
            
        def clear_ball_right(self):
            self.roland_right = None
            self.netzach_right = None

        def set_ball_right(self, ball_right):
            if self.active_player == "roland":
                self.roland_right = ball_right
                self.netzach_right = self.opposite_color(ball_right)
            elif self.active_player == "netzach":
                self.netzach_right = ball_right
                self.roland_right = self.opposite_color(ball_right)

        def change_player(self):
            if self.active_player == "roland":
                self.active_player = "netzach"
            elif self.active_player == "netzach":
                self.active_player = "roland"
            
        def get_ball_right(self, player):
            if player == "roland":
                ball_right = self.roland_right
            elif player == "netzach":
                ball_right = self.netzach_right
            return ball_right

        def get_ball_count(self, player, balls):
            ball_right = self.get_ball_right(player)
            if ball_right == "FullC":
                return sum(1 for ball in balls if ball.index in range(1, 8) and ball.show)
            elif ball_right == "HalfC":
                return sum(1 for ball in balls if ball.index in range(9, 16) and ball.show)
            else:
                return '-'

        def draw(self, balls):
            super().draw()
            self.screen.blit(pygame.transform.flip(self.pebox_texture,True,False), (120, self.screen.get_height() - self.pebox_texture.get_height()))
            self.screen.blit(self.pebox_texture, (self.screen.get_width() - self.pebox_texture.get_width() - 120, self.screen.get_height() - self.pebox_texture.get_height()))
            roland_count_rendered=self.font.render(str(self.get_ball_count("roland",balls)), True, (208, 0, 0))
            self.screen.blit(roland_count_rendered,(120+78, self.screen.get_height() - self.pebox_texture.get_height()+40)) 
            netzach_count_rendered=self.font.render(str(self.get_ball_count("netzach",balls)), True, (208, 0, 0))
            self.screen.blit(netzach_count_rendered,(self.screen.get_width() - self.pebox_texture.get_width() - 120+42, self.screen.get_height() - self.pebox_texture.get_height()+40))
            if self.active_player == "roland":
                self.screen.blit(self.roland_texture, (-100, 300))
                self.screen.blit(self.netzach_dark_texture, (self.screen.get_width() - self.netzach_texture.get_width() + 80, 300))
            elif self.active_player == "netzach":
                self.screen.blit(self.roland_dark_texture, (-100, 300))
                self.screen.blit(self.netzach_texture, (self.screen.get_width() - self.netzach_texture.get_width() + 80, 300))

            if(self.get_ball_right(self.active_player) == "FullC"):
                color_now="全色球"
            elif(self.get_ball_right(self.active_player) == "HalfC"):
                color_now="半色球"
            else:
                color_now="获取球权"
            color_now_rendered=self.font.render(color_now, True, (184, 255, 249))
            color_now_rect=color_now_rendered.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 300))
            self.screen.blit(color_now_rendered,color_now_rect)
            


    class Arbiter:
        @staticmethod
        def has_black(balls):
            return any(ball.index == 8 for ball in balls)
        
        @staticmethod
        def has_white(balls):
            return any(ball.index == 0 for ball in balls)
        
        @staticmethod
        def first_color(balls):
            for ball in balls:
                if ball.index in range (1, 8):
                    return "FullC"
                
                if ball.index in range (8, 16):
                    return "HalfC"

            return None
        
        @staticmethod
        def opposite_color(color):
            if color == "FullC":
                return "HalfC"
            elif color == "HalfC":
                return "FullC"
            else:
                return None


    def __init__(self, screen):
        self.screen = screen
        self.scene_change = self.SceneChange(screen)
        self.score_board = self.ScoreBoard(screen)
        self.free_ball = self.FreeBall(screen)
        self.scene_counter = 1
        self.mouse_pos = (0,0)

    def draw(self, billiard_table, now_state,last_state,mouse_pos,mouse_state):
        self.mouse_pos = mouse_pos
        self.mouse_state = mouse_state
        if self.free_ball.draw(self.mouse_pos, self.mouse_state, billiard_table.balls):
            billiard_table.balls[0].body.position = self.mouse_pos
            billiard_table.balls[0].body.velocity = (0,0)
            billiard_table.balls[0].show = True

        balls_dropped = billiard_table.balls_dropped
        ball_right = billiard_table.ball_right
        has_black = self.Arbiter.has_black
        has_white = self.Arbiter.has_white
        first_color = self.Arbiter.first_color
        opposite_color = self.Arbiter.opposite_color
        prompt_text=("出现错误： 未经处理的异常")
        if last_state=={}:
            print("scene start!")
            self.scene_change.change("第1幕", "开球， 分出球权")
        
        elif not now_state['ball_moving'] and last_state['ball_moving']:
            print("balls_dropped: ", list(ball.index for ball in balls_dropped))
            print("ball_right: ", ball_right)
            if ball_right == None:
                if balls_dropped == []:
                    #exchange
                    prompt_text=("无球进洞， 交换球权")
                    self.score_board.change_player()

                elif has_black(balls_dropped):
                    #reset
                    prompt_text=("黑8进洞， 重新开局")
                    self.score_board.clear_ball_right()
                    billiard_table.reset()
                    self.scene_counter = 0

                elif has_white(balls_dropped):
                    #exchange & free ball
                    prompt_text=("白球进洞， 交换球权， 自由球")
                    self.score_board.change_player()
                    self.free_ball.open = True

                else:
                    first_dropped = first_color(balls_dropped)
                    billiard_table.ball_right = first_dropped
                    if first_dropped == "FullC": #exchange & free ball
                        prompt_text=("全色球进洞， 球权归于该色球")
                        self.score_board.set_ball_right("FullC")

                    elif first_color(balls_dropped) == "HalfC":
                        prompt_text=("半色球进洞， 球权归于该色球")
                        self.score_board.set_ball_right("HalfC")

                    else:
                        prompt_text=("出现错误： 未经处理的异常")

            elif ball_right == "FullC" or ball_right == "HalfC":
                if balls_dropped == []:
                    #exchange
                    prompt_text=("无球进洞， 交换球权")
                    self.score_board.change_player()
                    billiard_table.ball_right = opposite_color(ball_right)

                elif has_black(balls_dropped):
                    #reset
                    prompt_text=("黑8进洞， 重新开局")
                    self.score_board.clear_ball_right()
                    self.score_board.change_player()
                    billiard_table.reset()
                    self.scene_counter = 0

                elif has_white(balls_dropped):
                    #exchange & free ball
                    prompt_text=("白球进洞， 交换球权， 自由球")
                    self.score_board.change_player()
                    billiard_table.ball_right = opposite_color(ball_right)
                    self.free_ball.open = True

                elif first_color(balls_dropped) == ball_right:
                    #keep
                    prompt_text=("同色球进洞， 球权保持")

                else: #exchange & free ball
                    prompt_text=("异色球进洞， 交换球权， 自由球")
                    self.score_board.change_player()
                    billiard_table.ball_right = opposite_color(ball_right)
                    self.free_ball.open = True

            else:
                prompt_text=("出现错误： 未经定义的情形")

            self.scene_counter += 1
            print(f"scene change! \"{prompt_text}\"")
            self.scene_change.change(f"第{self.scene_counter}幕", prompt_text)
            billiard_table.balls_dropped.clear()

 
        self.scene_change.draw()
        self.score_board.draw(billiard_table.balls)


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.set_num_channels(128)
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)
        self.space.damping = 0.5  # friction
        self.billiard_table = BilliardTable(self.screen, self.space)    
        self.gui = GUI(self.screen)
        self.mouse_state = [False, False]
        self.mouse_last_pos = (0, 0)
        self.mouse_pos = (0, 0)
        self.last_state={}

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            #pfb = pf()
            self.billiard_table.draw()
            now_state=self.update_physics(self.billiard_table.balls_dropped)
            self.gui.draw(self.billiard_table,now_state,self.last_state,self.mouse_pos,self.mouse_state[1])
            self.handle_input(now_state,self.last_state)
            self.last_state=now_state
            pygame.display.flip()
            self.screen.fill((0, 28, 0))
            #pygame.draw.rect(self.screen, (0, 28, 0, 1), (0, 0, self.screen.get_width(), self.screen.get_height()))
            #print("Cycle cost %f sec" % (pf()-pfb))

        pygame.quit()

    def handle_input(self, now_state, last_state):
        self.mouse_state[1] = self.mouse_state[0]
        self.mouse_state[0] = pygame.mouse.get_pressed()[0]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.billiard_table.balls[0].apply_impulse((0, -1000))
        if keys[pygame.K_s]:
            self.billiard_table.balls[0].apply_impulse((0, 1000))
        if keys[pygame.K_a]:
            self.billiard_table.balls[0].apply_impulse((-1000, 0))
        if keys[pygame.K_d]:
            self.billiard_table.balls[0].apply_impulse((1000, 0))

        self.mouse_pos = pygame.mouse.get_pos()
        if self.mouse_state[0] and not self.mouse_state[1]:
            self.mouse_last_pos = self.mouse_pos
        if self.mouse_state[0] and not now_state["ball_moving"]:
            pygame.draw.aaline(self.screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             (self.billiard_table.balls[0].body.position.x - (self.mouse_last_pos[0] - pygame.mouse.get_pos()[0]),
                              self.billiard_table.balls[0].body.position.y - (self.mouse_last_pos[1] - pygame.mouse.get_pos()[1])),
                             self.billiard_table.balls[0].body.position, 1)

        if not self.mouse_state[0] and self.mouse_state[1] and not now_state["ball_moving"]:
            line = ((self.mouse_last_pos[0] - pygame.mouse.get_pos()[0]) * 50,
                    (self.mouse_last_pos[1] - pygame.mouse.get_pos()[1]) * 50)
            self.billiard_table.balls[0].apply_impulse(line)

    def update_physics(self,balls_dropped):
        # Minimum velocity threshold
        MIN_VELOCITY = 100
        ball_moving = False
        stage_clear = True

        for ball in self.billiard_table.balls:
            velocity = ball.body.velocity.length
            #Damping friction
            if velocity < MIN_VELOCITY:
                ball.body.velocity = (ball.body.velocity[0]*0.9,ball.body.velocity[1]*0.9)

            position = ball.body.position
            #Out of bounds
            if ball.show and ((position[0] < self.screen.get_width() / 2 - 500) or (position[0] > self.screen.get_width() / 2 + 500) or \
                    (position[1] < self.screen.get_height() / 2 - 250) or (position[1] > self.screen.get_height() / 2 + 250)):
                ball.show = False
                balls_dropped.append(ball)

            #balls are moving
            if ball.show and velocity > 100:
                ball_moving = True  

            #stage cleared
            if ball.show:
                stage_clear = False 
            
        white_ball = self.billiard_table.balls[0]  
        self.dt = self.clock.tick(120) / 1000.0
        self.space.step(self.dt)

        return {"ball_moving": ball_moving, "stage_clear": stage_clear}


game = Game()
game.run()