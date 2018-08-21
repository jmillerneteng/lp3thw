import exsh;

def main():

	var1=exsh.clicmd("show ports stack-ports rxerrors no-refresh | i 1", capture=True)
	var1=str(var1)
	var1=var1.split()
	var1=int(var1[2])

	if var1>0:
		var5=exsh.clicmd("create log message \"RX errors are present on stack-port 1\"")
        var5=exsh.clicmd("clear counters port stack-ports")
	else:
		pass

if __name__ == "__main__":
	try:
		main()
	except SystemExit:
		pass