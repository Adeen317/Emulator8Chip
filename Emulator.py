
#input
self.key_inputs = [0]*16

#Output
self.display_buffer = [0]*32*64 # 64*32

#Memory
self.memory = [0]*4096 # max 4096

#Registers
self.gpio = [0]*16 # 16 zeroes
self.sound_timer = 0
self.delay_timer = 0
self.index = 0
self.stack = []
