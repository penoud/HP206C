import PyBCM2835

class HPC206:
	COMMAND_ADC_CONV_PT_4096 = 0x40
	COMMAND_ADC_CONV_T_4096 = 0x42
	COMMAND_ADC_CONV_PT_2048 = 0x44
	COMMAND_ADC_CONV_T_2048 = 0x46
	COMMAND_ADC_CONV_PT_1024 = 0x48
	COMMAND_ADC_CONV_T_1024 = 0x4A
	COMMAND_ADC_CONV_PT_512 = 0x4C
	COMMAND_ADC_CONV_T_512 = 0x4E
	COMMAND_ADC_CONV_PT_256 = 0x50
	COMMAND_ADC_CONV_T_256 = 0x52
	COMMAND_ADC_CONV_PT_128 = 0x54
	COMMAND_ADC_CONV_T_128 = 0x56
	COMMAND_READ_PT = 0x10
	COMMAND_READ_AT = 0x11
	COMMAND_READ_P = 0x30
	COMMAND_READ_A = 0x31
	COMMAND_READ_T = 0x32
	COMMAND_ANA_CAL = 0x28
	COMMAND_SOFT_RESET = 0x06
	COMMAND_READ_REG_MASK = 0x80
	COMMAND_WRITE_REG_MASK = 0xC0

	CONVERSION_RATE = 4096
	
	def __init__(self):
		if not (PyBCM2835.init()):
			raise EnvironmentError("Cannot initialize BCM2835.")
		PyBCM2835.i2c_begin()
		PyBCM2835.i2c_setSlaveAddress(0xEC)

		PyBCM2835.delay(100)
	def setConversionRate(self,value):
		if((value==4096) or (value==2048) or (value==1024) or (value==512) or (value==256) or (value==128)):
			CONVERSION_RATE=value
		else:
			print "Error: invalid conversion rate, valid are (4096,2048,1024,512,256,128)"
	def startPTConversion(self):
		if(CONVERSION_RATE==4096):
			PyBCM2835.i2c_write(chr(self.COMMAND_ADC_CONV_PT_4096),1)			
			PyBCM2835.delay(150)
		else if(CONVERSION_RATE==2048): 
			PyBCM2835.i2c_write(chr(self.COMMAND_ADC_CONV_PT_2048),1)			
			PyBCM2835.delay(75)
		else if(CONVERSION_RATE==1024): 
			PyBCM2835.i2c_write(chr(self.COMMAND_ADC_CONV_PT_1024),1)			
			PyBCM2835.delay(50)
		else if(CONVERSION_RATE==512): 
			PyBCM2835.i2c_write(chr(self.COMMAND_ADC_CONV_PT_512),1)			
			PyBCM2835.delay(25)
		else if(CONVERSION_RATE==256): 
			PyBCM2835.i2c_write(chr(self.COMMAND_ADC_CONV_PT_256),1)			
			PyBCM2835.delay(16)
		else if(CONVERSION_RATE==128): 
			PyBCM2835.i2c_write(chr(self.COMMAND_ADC_CONV_PT_128),1)			
			PyBCM2835.delay(10)
		else:
			print "Error, unknown conversion rate"
			return 0
	def readPressure(self):
		PyBCM2835.i2c_write(chr(self.COMMAND_READ_P),1)	
		data=""+chr(0)+chr(0)+chr(0)
		PyBCM2835.i2c_read(data,3)
		return data
	def readTemp(self):
		PyBCM2835.i2c_write(chr(self.COMMAND_READ_T),1)	
		data=""+chr(0)+chr(0)+chr(0)
		PyBCM2835.i2c_read(data,3)
		return data
	def readReg(self,register):
		PyBCM2835.i2c_write(chr(self.COMMAND_READ_REG | (register & 0x3F)),1)		
		data=""+chr(0)
		PyBCM2835.i2c_read(data,1)
		return int(ord(data[0]))
	def writeReg(self,register,value):
		PyBCM2835.i2c_write(chr(self.COMMAND_WRITE_REG | (register & 0x3F))+chr(value),2)	
	
	def softReset(self):
		PyBCM2835.i2c_write(chr(self.COMMAND_SOFT_RESET),1)
