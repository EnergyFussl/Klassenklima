import shlex
import subprocess

def gettemp():
	i=0
	while 1:
		cmd="gatttool -b 54:6C:0E:4D:97:85 --char-write-req -a 0x0027 -n 01"
		args = shlex.split(cmd)
		try:
			subprocess.run(args,timeout=1)
		except subprocess.TimeoutExpired:
			print("time out connection")
		cmd="gatttool -b 54:6C:0E:4D:97:85 --char-read -a 0x0024"
		args = shlex.split(cmd)
		try:
			tryvar = subprocess.run(args, timeout=1)
			outputgattby=subprocess.check_output(args)
			outputgatt=outputgattby.decode("utf-8")
			trash,raw_temp_data=outputgatt.split(":")
			raw_temp_bytes = raw_temp_data.split()
			raw_ambient_temp = int( '0x'+ raw_temp_bytes[3]+ raw_temp_bytes[2], 16)
			ambient_temp_int = raw_ambient_temp >> 2 & 0x3FFF
			ambient_temp_celsius = float(ambient_temp_int) * 0.03125
			if ambient_temp_celsius == 0:
				print("warning: no var from Ti")
				i=i+1
			else:
				return(ambient_temp_celsius)
		except subprocess.TimeoutExpired:
			print("time out while getting data")
			i=i+3
		if i>10:
			print("TI is not or badly connected")
			return-1
def gethum():
        i=0
        while 1:
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-write-req -a 0x002F -n 01"
                args = shlex.split(cmd)
                try:
                        subprocess.run(args,timeout=1)
                except subprocess.TimeoutExpired:
                        print("time out connection")
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-read -a 0x002C"
                args = shlex.split(cmd)
                try:
                        tryvar = subprocess.run(args, timeout=1)
                        outputgattby=subprocess.check_output(args)
                        outputgatt=outputgattby.decode("utf-8")
                        trash,raw_hum_data=outputgatt.split(":")
                        raw_hum_bit = raw_hum_data.split()
                        raw_hum_data = int( '0x'+ raw_hum_bit[3]+ raw_hum_bit[2], 16)
                        raw_hum_data &= ~0x0003
                        hum = (float(raw_hum_data) / 65536)*100
                        if hum == 0:
                                print("warning: no var from Ti")
                                i=i+1
                        else:
                                return(hum)
                except subprocess.TimeoutExpired:
                        print("time out while getting data")
                        i=i+3
                if i>10:
                        print("TI is not or badly connected")
                        return-1
def getbar():
        i=0
        while 1:
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-write-req -a 0x0037 -n 01"
                args = shlex.split(cmd)
                try:
                        subprocess.run(args,timeout=1)
                except subprocess.TimeoutExpired:
                        print("time out connection")
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-read -a 0x0034"
                args = shlex.split(cmd)
                try:
                        tryvar = subprocess.run(args, timeout=1)
                        outputgattby=subprocess.check_output(args)
                        outputgatt=outputgattby.decode("utf-8")
                        trash,raw_bar_byte=outputgatt.split(":")
                        raw_bar_str = (raw_bar_byte.split())
                        raw_bar_data = int(('0x'+raw_bar_str[5])+(raw_bar_str[4])+raw_bar_str[3],16)
                        bar = raw_bar_data/100.0
                        if bar == 0:
                                print("warning: no var from Ti")
                                i=i+1
                        else:
                                return(bar)
                except subprocess.TimeoutExpired:
                        print("time out while getting data")
                        i=i+3
                if i>10:
                        print("TI is not or badly connected")
                        return-1
def getlux():
        i=0
        while 1:
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-write-req -a 0x0047 -n 01"
                args = shlex.split(cmd)
                try:
                        subprocess.run(args,timeout=1)
                except subprocess.TimeoutExpired:
                        print("time out connection")
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-read -a 0x0044"
                args = shlex.split(cmd)
                try:
                        tryvar = subprocess.run(args, timeout=1)
                        outputgattby=subprocess.check_output(args)
                        outputgatt=outputgattby.decode("utf-8")
                        trash,raw_lux_data=outputgatt.split(":")
                        raw_lux_list = raw_lux_data.split()
                        raw_lux_int=int('0x'+raw_lux_list[1]+raw_lux_list[0],16)
                        m = raw_lux_int & 0x0FFF
                        e = (raw_lux_int & 0xF000) >> 12;
                        if e==0:
                                e=1
                        else:
                                e=2<<(e-1)
                        lux=m * (0.01 * e)
                        if lux == 0:
                                print("warning: no var from Ti")
                                i=i+1
                        else:
                                return(lux)
                except subprocess.TimeoutExpired:
                        print("time out while getting data")
                        i=i+3
                if i>10:
                        print("TI is not or badly connected")
                        return-1
def getbty():
        i=0
        while 1:
                cmd="gatttool -b 54:6C:0E:4D:97:85 --char-read -a 0x001E"
                args = shlex.split(cmd)
                try:
                        tryvar = subprocess.run(args, timeout=1)
                        outputgattby=subprocess.check_output(args)
                        outputgatt=outputgattby.decode("utf-8")
                        trash,raw_bty_byte=outputgatt.split(":")
                        raw_bty_str = (raw_bty_byte.split())
                        raw_bty_data=('0x'+raw_bty_str[0])
                        bty=int(raw_bty_data,16)
                        if bty == 0:
                                print("warning: no var from Ti")
                                i=i+1
                        else:
                                return(bty)
                except subprocess.TimeoutExpired:
                        print("time out while getting data")
                        i=i+3
                if i>10:
                        print("TI is not or badly connected")
                        return-1
print(gettemp())
print(gethum())
print(getbar())
print(getlux())
print(getbty())
