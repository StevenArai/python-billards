Q='assets/fonts/leefont.ttf'
O=print
B=staticmethod
N=max
M=min
L='ball_moving'
K='netzach'
J=range
G='roland'
H=None
F='HalfC'
E='FullC'
D=False
C=True
import pygame as A,pymunk as I,random as P
class R:
	def __init__(B,index,position,color):B.index=index;B.mass=20;B.radius=25;B.moment=I.moment_for_circle(B.mass,0,B.radius);B.body=I.Body(B.mass,B.moment);B.shape=I.Circle(B.body,B.radius);B.shape.elasticity=.98;B.body.position=position;B.color=color;B.texture=A.image.load('assets/texture/balls/{0:d}.png'.format(B.index)).convert_alpha();B.show=C
	def draw(A,screen):
		if A.show:screen.blit(A.texture,(A.body.position.x-A.radius,A.body.position.y-A.radius))
	def apply_impulse(A,impulse):A.body.apply_impulse_at_local_point(impulse)
class S:
	def __init__(A,start,end,space):A.space=space;A.shape=I.Segment(A.space.static_body,start,end,10);A.shape.elasticity=.8;A.space.add(A.shape)
	def draw(B,screen):A.draw.line(screen,(127,50,0),B.shape.a,B.shape.b,10)
class T:
	def __init__(B,screen,space):C=space;B.screen=screen;B.space=C;B.balls=[];B.balls_dropped=[];B.ball_right=H;B.walls=[];B.create_balls();B.create_walls();B.title=A.image.load('assets/texture/title.png').convert_alpha();B.collision_ball_sound=A.mixer.Sound('assets/sounds/collision.wav');B.collision_side_sound=A.mixer.Sound('assets/sounds/side-collision.wav');A.mixer.music.load('assets/music/netzach.wav');A.mixer.music.play(99999);A.mixer.music.set_volume(.3);B.collision_handler=C.add_collision_handler(0,0);B.collision_handler.begin=B.collision_callback
	def reset(A):
		A.balls_dropped=[];A.ball_right=H;E=[[(A.screen.get_width()/2-150,A.screen.get_height()/2)],[(A.screen.get_width()/2-100,A.screen.get_height()/2-25),(A.screen.get_width()/2-100,A.screen.get_height()/2+25)],[(A.screen.get_width()/2-50,A.screen.get_height()/2-50),(A.screen.get_width()/2-50,A.screen.get_height()/2),(A.screen.get_width()/2-50,A.screen.get_height()/2+50)],[(A.screen.get_width()/2,A.screen.get_height()/2-75),(A.screen.get_width()/2,A.screen.get_height()/2-25),(A.screen.get_width()/2,A.screen.get_height()/2+25),(A.screen.get_width()/2,A.screen.get_height()/2+75)],[(A.screen.get_width()/2+50,A.screen.get_height()/2-100),(A.screen.get_width()/2+50,A.screen.get_height()/2-50),(A.screen.get_width()/2+50,A.screen.get_height()/2),(A.screen.get_width()/2+50,A.screen.get_height()/2+50),(A.screen.get_width()/2+50,A.screen.get_height()/2+100)]]
		for B in J(0,16):
			if B==0:D=A.screen.get_width()/2-300,A.screen.get_height()/2
			else:
				if B==1:D=E[0][0]
				elif 2<=B<=3:D=E[1][B-2]
				elif 4<=B<=6:D=E[2][B-4]
				elif 7<=B<=10:D=E[3][B-7]
				elif 11<=B<=15:D=E[4][B-11]
				D=D[0]+300,D[1]
			A.balls[B].body.position=D;A.balls[B].show=C;A.balls[B].body.velocity=0,0
	def collision_callback(E,arbiter,space,data):
		B=arbiter;F=B.shapes[0].body.velocity;G=B.shapes[1].body.velocity;H=F-G;J=H.length*.0005+.1;D=A.mixer.find_channel();D.set_volume(J)
		if isinstance(B.shapes[1],I.shapes.Segment):D.play(E.collision_side_sound)
		else:D.play(E.collision_ball_sound)
		return C
	def create_balls(A):
		F=[(255,255,255),(255,255,0),(255,0,255),(0,255,255),(255,127,0),(255,0,0),(0,0,255),(0,255,0),(127,0,255),(255,127,127),(255,255,127),(255,0,127),(0,255,127),(0,127,255),(127,255,0),(127,127,255)];D=[[(A.screen.get_width()/2-150,A.screen.get_height()/2)],[(A.screen.get_width()/2-100,A.screen.get_height()/2-25),(A.screen.get_width()/2-100,A.screen.get_height()/2+25)],[(A.screen.get_width()/2-50,A.screen.get_height()/2-50),(A.screen.get_width()/2-50,A.screen.get_height()/2),(A.screen.get_width()/2-50,A.screen.get_height()/2+50)],[(A.screen.get_width()/2,A.screen.get_height()/2-75),(A.screen.get_width()/2,A.screen.get_height()/2-25),(A.screen.get_width()/2,A.screen.get_height()/2+25),(A.screen.get_width()/2,A.screen.get_height()/2+75)],[(A.screen.get_width()/2+50,A.screen.get_height()/2-100),(A.screen.get_width()/2+50,A.screen.get_height()/2-50),(A.screen.get_width()/2+50,A.screen.get_height()/2),(A.screen.get_width()/2+50,A.screen.get_height()/2+50),(A.screen.get_width()/2+50,A.screen.get_height()/2+100)]]
		for B in J(0,16):
			if B==0:C=A.screen.get_width()/2-300,A.screen.get_height()/2
			else:
				if B==1:C=D[0][0]
				elif 2<=B<=3:C=D[1][B-2]
				elif 4<=B<=6:C=D[2][B-4]
				elif 7<=B<=10:C=D[3][B-7]
				elif 11<=B<=15:C=D[4][B-11]
				C=C[0]+300,C[1]
			G=F[B];E=R(B,C,G);A.balls.append(E);A.space.add(E.body,E.shape)
	def create_walls(A):
		C=[[(A.screen.get_width()/2+50,A.screen.get_height()/2-250),(A.screen.get_width()/2+500-70,A.screen.get_height()/2-250)],[(A.screen.get_width()/2-500+70,A.screen.get_height()/2-250),(A.screen.get_width()/2-50,A.screen.get_height()/2-250)],[(A.screen.get_width()/2+500,A.screen.get_height()/2-250+70),(A.screen.get_width()/2+500,A.screen.get_height()/2+250-70)],[(A.screen.get_width()/2+500-70,A.screen.get_height()/2+250),(A.screen.get_width()/2+50,A.screen.get_height()/2+250)],[(A.screen.get_width()/2-50,A.screen.get_height()/2+250),(A.screen.get_width()/2-500+70,A.screen.get_height()/2+250)],[(A.screen.get_width()/2-500,A.screen.get_height()/2+250-70),(A.screen.get_width()/2-500,A.screen.get_height()/2-250+70)]]
		for B in C:D=S(B[0],B[1],A.space);A.walls.append(D)
	def draw(B):
		A.draw.rect(B.screen,(0,127,0),(B.screen.get_width()/2-500,B.screen.get_height()/2-250,1000,500));C=[(B.screen.get_width()/2-500,B.screen.get_height()/2-250),(B.screen.get_width()/2-500,B.screen.get_height()/2+250),(B.screen.get_width()/2+500,B.screen.get_height()/2-250),(B.screen.get_width()/2+500,B.screen.get_height()/2+250),(B.screen.get_width()/2,B.screen.get_height()/2-250),(B.screen.get_width()/2,B.screen.get_height()/2+250)]
		for D in C:A.draw.circle(B.screen,(0,0,0),D,30)
		for E in B.walls:E.draw(B.screen)
		for F in B.balls:F.draw(B.screen)
		B.screen.blit(B.title,(0,0))
class U:
	class GUIElement:
		def __init__(A,screen):A.screen=screen;A.open=D;A.openrate=0;A.sigma=.1
		def interpolate(A):
			if A.open:
				if A.openrate<100:A.openrate+=(100.1-A.openrate)*A.sigma
				A.openrate=M(A.openrate,100)
			else:
				if A.openrate>0:A.openrate-=(100.1-A.openrate)*A.sigma
				A.openrate=N(A.openrate,0)
		def draw(A):A.interpolate()
	class FreeBall(GUIElement):
		def __init__(C,screen):B=screen;super().__init__(B);C.surface=A.Surface((B.get_width(),B.get_height()),A.SRCALPHA);C.sigma=.1
		def interpolate(A):
			if A.open:
				if A.openrate<100:A.openrate+=(100.1-A.openrate)*A.sigma
				A.openrate=M(A.openrate,100)
			else:
				if A.openrate>0:A.openrate+=(-.1-A.openrate)*A.sigma
				A.openrate=N(A.openrate,0)
		def avaliable(B,pos):
			for E in B.balls[1:]:
				A=E.body.position;F=50
				if(A[0]-pos[0])**2+(A[1]-pos[1])**2<F**2:return D
			return C
		def draw(B,mouse_pos,mouse_state,balls):
			F=mouse_pos;B.balls=balls;super().draw()
			if B.openrate>0:
				G=D;E=0,0,255;H=M(N(F[0],0),B.screen.get_width()),M(N(F[1],0),B.screen.get_height())
				if B.avaliable(H):
					E=0,255,255
					if mouse_state==1 and B.open:G=C;B.open=D
				else:E=255,0,0
				B.surface.fill((0,0,0,0));B.surface.set_alpha(B.openrate/100*500-256);A.draw.circle(B.surface,E,H,25+(1-B.openrate/100)*1280,int(125-B.openrate));B.screen.blit(B.surface,(0,0));return G
	class SceneChange(GUIElement):
		def __init__(B,screen):C=screen;super().__init__(C);B.text1=H;B.text2=H;B.font1=A.font.Font(Q,82);B.font2=A.font.Font(Q,32);B.sigma=.08;B.scene_sound=A.mixer.Sound('assets/sounds/scene.wav');B.background=A.image.load('assets/texture/scene_change.png').convert_alpha();B.surface=A.Surface((C.get_width(),C.get_height()),A.SRCALPHA)
		def change(B,text1,text2):E=text2;D=text1;B.surface.fill((0,0,0,0));F=A.mixer.find_channel();F.set_volume(1);F.play(B.scene_sound);B.text1=D;B.text2=E;B.open=C;B.surface.blit(B.background,(0,0));G=B.font1.render(D,C,(208,187,151));I=G.get_rect(center=(B.screen.get_width()/2,B.screen.get_height()/2+5));B.surface.blit(G,I);H=B.font2.render(E,C,(184,255,249));J=H.get_rect(center=(B.screen.get_width()/2,B.screen.get_height()/2+100));B.surface.blit(H,J)
		def draw(B):
			super().draw()
			if B.open and B.openrate==100:B.open=D
			if B.openrate>0:B.surface.set_alpha(B.openrate/100*500-256);C=2-B.openrate/100;G=C;E=B.screen.get_width();F=B.screen.get_height();H=(E*B.openrate/100-B.surface.get_width())/2;I=(F*B.openrate/100-B.surface.get_height())/2;B.screen.blit(A.transform.smoothscale(B.surface,(E*C,F*G)),(H,I))
	class ScoreBoard(GUIElement):
		def __init__(B,screen):super().__init__(screen);B.roland_texture=A.image.load('assets/texture/figure/roland.png').convert_alpha();B.netzach_texture=A.image.load('assets/texture/figure/netzach.png').convert_alpha();B.roland_dark_texture=A.image.load('assets/texture/figure/roland_dark.png').convert_alpha();B.netzach_dark_texture=A.image.load('assets/texture/figure/netzach_dark.png').convert_alpha();B.pebox_texture=A.image.load('assets/texture/pe-box.png').convert_alpha();B.active_player=G;B.roland_right=H;B.netzach_right=H;B.font=A.font.Font(Q,36)
		def opposite_color(B,color):
			A=color
			if A==E:return F
			elif A==F:return E
			else:return
		def clear_ball_right(A):A.roland_right=H;A.netzach_right=H
		def set_ball_right(A,ball_right):
			B=ball_right
			if A.active_player==G:A.roland_right=B;A.netzach_right=A.opposite_color(B)
			elif A.active_player==K:A.netzach_right=B;A.roland_right=A.opposite_color(B)
		def change_player(A):
			if A.active_player==G:A.active_player=K
			elif A.active_player==K:A.active_player=G
		def get_ball_right(A,player):
			B=player
			if B==G:C=A.roland_right
			elif B==K:C=A.netzach_right
			return C
		def get_ball_count(C,player,balls):
			A=balls;B=C.get_ball_right(player)
			if B==E:return sum(1 for A in A if A.index in J(1,8)and A.show)
			elif B==F:return sum(1 for A in A if A.index in J(9,16)and A.show)
			else:return'-'
		def draw(B,balls):
			I=balls;super().draw();B.screen.blit(A.transform.flip(B.pebox_texture,C,D),(120,B.screen.get_height()-B.pebox_texture.get_height()));B.screen.blit(B.pebox_texture,(B.screen.get_width()-B.pebox_texture.get_width()-120,B.screen.get_height()-B.pebox_texture.get_height()));L=B.font.render(str(B.get_ball_count(G,I)),C,(208,0,0));B.screen.blit(L,(198,B.screen.get_height()-B.pebox_texture.get_height()+40));M=B.font.render(str(B.get_ball_count(K,I)),C,(208,0,0));B.screen.blit(M,(B.screen.get_width()-B.pebox_texture.get_width()-120+42,B.screen.get_height()-B.pebox_texture.get_height()+40))
			if B.active_player==G:B.screen.blit(B.roland_texture,(-100,300));B.screen.blit(B.netzach_dark_texture,(B.screen.get_width()-B.netzach_texture.get_width()+80,300))
			elif B.active_player==K:B.screen.blit(B.roland_dark_texture,(-100,300));B.screen.blit(B.netzach_texture,(B.screen.get_width()-B.netzach_texture.get_width()+80,300))
			if B.get_ball_right(B.active_player)==E:H='全色球'
			elif B.get_ball_right(B.active_player)==F:H='半色球'
			else:H='获取球权'
			J=B.font.render(H,C,(184,255,249));N=J.get_rect(center=(B.screen.get_width()/2,B.screen.get_height()/2+300));B.screen.blit(J,N)
	class Arbiter:
		@B
		def has_black(balls):return any(A.index==8 for A in balls)
		@B
		def has_white(balls):return any(A.index==0 for A in balls)
		@B
		def first_color(balls):
			for A in balls:
				if A.index in J(1,8):return E
				if A.index in J(8,16):return F
		@B
		def opposite_color(color):
			A=color
			if A==E:return F
			elif A==F:return E
			else:return
	def __init__(A,screen):B=screen;A.screen=B;A.scene_change=A.SceneChange(B);A.score_board=A.ScoreBoard(B);A.free_ball=A.FreeBall(B);A.scene_counter=1;A.mouse_pos=0,0
	def draw(A,billiard_table,now_state,last_state,mouse_pos,mouse_state):
		U='白球进洞， 交换球权， 自由球';T='黑8进洞， 重新开局';S='无球进洞， 交换球权';R='出现错误： 未经处理的异常';M=last_state;B=billiard_table;A.mouse_pos=mouse_pos;A.mouse_state=mouse_state
		if A.free_ball.draw(A.mouse_pos,A.mouse_state,B.balls):B.balls[0].body.position=A.mouse_pos;B.balls[0].body.velocity=0,0;B.balls[0].show=C
		G=B.balls_dropped;I=B.ball_right;N=A.Arbiter.has_black;P=A.Arbiter.has_white;J=A.Arbiter.first_color;K=A.Arbiter.opposite_color;D=R
		if M=={}:O('scene start!');A.scene_change.change('第1幕','开球， 分出球权')
		elif not now_state[L]and M[L]:
			O('balls_dropped: ',list(A.index for A in G));O('ball_right: ',I)
			if I==H:
				if G==[]:D=S;A.score_board.change_player()
				elif N(G):D=T;A.score_board.clear_ball_right();B.reset();A.scene_counter=0
				elif P(G):D=U;A.score_board.change_player();A.free_ball.open=C
				else:
					Q=J(G);B.ball_right=Q
					if Q==E:D='全色球进洞， 球权归于该色球';A.score_board.set_ball_right(E)
					elif J(G)==F:D='半色球进洞， 球权归于该色球';A.score_board.set_ball_right(F)
					else:D=R
			elif I==E or I==F:
				if G==[]:D=S;A.score_board.change_player();B.ball_right=K(I)
				elif N(G):D=T;A.score_board.clear_ball_right();A.score_board.change_player();B.reset();A.scene_counter=0
				elif P(G):D=U;A.score_board.change_player();B.ball_right=K(I);A.free_ball.open=C
				elif J(G)==I:D='同色球进洞， 球权保持'
				else:D='异色球进洞， 交换球权， 自由球';A.score_board.change_player();B.ball_right=K(I);A.free_ball.open=C
			else:D='出现错误： 未经定义的情形'
			A.scene_counter+=1;O(f'scene change! "{D}"');A.scene_change.change(f"第{A.scene_counter}幕",D);B.balls_dropped.clear()
		A.scene_change.draw();A.score_board.draw(B.balls)
class V:
	def __init__(B):A.init();A.mixer.init();A.mixer.set_num_channels(128);B.screen=A.display.set_mode((1280,720));B.clock=A.time.Clock();B.running=C;B.dt=0;B.space=I.Space();B.space.gravity=0,0;B.space.damping=.5;B.billiard_table=T(B.screen,B.space);B.gui=U(B.screen);B.mouse_state=[D,D];B.mouse_last_pos=0,0;B.mouse_pos=0,0;B.last_state={}
	def run(B):
		while B.running:
			for E in A.event.get():
				if E.type==A.QUIT:B.running=D
			B.billiard_table.draw();C=B.update_physics(B.billiard_table.balls_dropped);B.gui.draw(B.billiard_table,C,B.last_state,B.mouse_pos,B.mouse_state[1]);B.handle_input(C,B.last_state);B.last_state=C;A.display.flip();B.screen.fill((0,28,0))
		A.quit()
	def handle_input(B,now_state,last_state):
		D=now_state;B.mouse_state[1]=B.mouse_state[0];B.mouse_state[0]=A.mouse.get_pressed()[0];C=A.key.get_pressed()
		if C[A.K_w]:B.billiard_table.balls[0].apply_impulse((0,-1000))
		if C[A.K_s]:B.billiard_table.balls[0].apply_impulse((0,1000))
		if C[A.K_a]:B.billiard_table.balls[0].apply_impulse((-1000,0))
		if C[A.K_d]:B.billiard_table.balls[0].apply_impulse((1000,0))
		B.mouse_pos=A.mouse.get_pos()
		if B.mouse_state[0]and not B.mouse_state[1]:B.mouse_last_pos=B.mouse_pos
		if B.mouse_state[0]and not D[L]:A.draw.aaline(B.screen,(P.randint(0,255),P.randint(0,255),P.randint(0,255)),(B.billiard_table.balls[0].body.position.x-(B.mouse_last_pos[0]-A.mouse.get_pos()[0]),B.billiard_table.balls[0].body.position.y-(B.mouse_last_pos[1]-A.mouse.get_pos()[1])),B.billiard_table.balls[0].body.position,1)
		if not B.mouse_state[0]and B.mouse_state[1]and not D[L]:E=(B.mouse_last_pos[0]-A.mouse.get_pos()[0])*50,(B.mouse_last_pos[1]-A.mouse.get_pos()[1])*50;B.billiard_table.balls[0].apply_impulse(E)
	def update_physics(A,balls_dropped):
		I=100;F=D;G=C
		for B in A.billiard_table.balls:
			H=B.body.velocity.length
			if H<I:B.body.velocity=B.body.velocity[0]*.9,B.body.velocity[1]*.9
			E=B.body.position
			if B.show and(E[0]<A.screen.get_width()/2-500 or E[0]>A.screen.get_width()/2+500 or E[1]<A.screen.get_height()/2-250 or E[1]>A.screen.get_height()/2+250):B.show=D;balls_dropped.append(B)
			if B.show and H>100:F=C
			if B.show:G=D
		J=A.billiard_table.balls[0];A.dt=A.clock.tick(120)/1e3;A.space.step(A.dt);return{L:F,'stage_clear':G}
W=V()
W.run()