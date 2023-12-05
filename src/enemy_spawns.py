from sprites.enemies import Enemy1

class Enemy_Spawns:
	def __init__(self):
		self.wave_count = 0

	def spawn(self, current_time):
		#Wave 1
		if current_time > 0 and self.wave_count == 0:
			self.wave_count += 1
			return self.arrangement1()			
		#Wave 2
		if current_time > 5000 and self.wave_count == 1:
			self.wave_count += 1
			return self.arrangement1()
		#Wave 3
		if current_time > 7000 and self.wave_count == 2:
			self.wave_count += 1
			return self.arrangement2()
		#Wave 4
		if current_time > 10000 and self.wave_count == 3:
			self.wave_count += 1
			return self.arrangement3()
		#Wave 5
		if current_time > 12000 and self.wave_count == 4:
			self.wave_count += 1
			return self.arrangement1()
		#Wave 6
		if current_time > 14000 and self.wave_count == 5:
			self.wave_count += 1
			return self.arrangement2()
		#Wave 7
		if current_time > 17000 and self.wave_count == 6:
			self.wave_count += 1
			return self.arrangement4()
		#Wave 8
		if current_time > 20000 and self.wave_count == 7:
			self.wave_count += 1
			return self.arrangement3()
		#Wave 9
		if current_time > 22000 and self.wave_count == 8:
			self.wave_count += 1
			return self.arrangement5()
		#Wave 10
		if current_time > 25000 and self.wave_count == 9:
			self.wave_count += 1
			return self.arrangement6()
		#Wave 11
		if current_time > 30000 and self.wave_count == 10:
			self.wave_count += 1
			enemies = self.arrangement2() + self.arrangement5()
			return enemies
		#Wave 12
		if current_time > 32000 and self.wave_count == 11:
			self.wave_count += 1
			return self.arrangement7()
	
	#Slow sides, fast middle
	def arrangement1(self):
		enemy_list = [
			Enemy1(20, 0, 2),
			Enemy1(460, 0, 2),
			Enemy1(170, -500, 1),
			Enemy1(310, -500, 1)
			]
		return enemy_list

	#2 Lanes side-to-side
	def arrangement2(self):
		enemy_list = [
			Enemy1(-60, 400, 3),
			Enemy1(582, 500, 4),
			Enemy1(-260, 400, 3),
			Enemy1(782, 500, 4),
			Enemy1(-460, 400, 3),
			Enemy1(982, 500, 4)
		]
		return enemy_list

	#Slow wide line
	def arrangement3(self):
		enemy_list = [
			Enemy1(20, 0, 2),
			Enemy1(460, 0, 2),
			Enemy1(145, 0, 2),
			Enemy1(335, 0, 2)
		]
		return enemy_list

	#2 in a row fast sides, 2 slow middle
	def arrangement4(self):
		enemy_list = [
			Enemy1(0, 0, 1),
			Enemy1(440, 0, 1),
			Enemy1(0, -150, 1),
			Enemy1(440, -150, 1),
			Enemy1(232, 0, 2),
			Enemy1(232, -150, 2)
		]
		return enemy_list

	#Small fast arrow
	def arrangement5(self):
		enemy_list = [
			Enemy1(250, 0, 1),
			Enemy1(210, -40, 1),
			Enemy1(290, -40, 1)
		]
		return enemy_list
	
	#Slow big arrow
	def arrangement6(self):
		enemy_list = [
			Enemy1(250, 0, 2),
			Enemy1(210, -40, 2),
			Enemy1(290, -40, 2),
			Enemy1(330, -80, 2),
			Enemy1(170, -80, 2)
		]
		return enemy_list
	
	#Slow sides line 2 following
	def arrangement7(self):
		enemy_list = [
			Enemy1(190, 0, 1),
			Enemy1(270, 0, 1),
			Enemy1(310, 0 , 2),
			Enemy1(150, 0, 2),
			Enemy1(190, -30, 2),
			Enemy1(270, -30, 2),
		]
		return enemy_list