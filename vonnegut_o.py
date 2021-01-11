class Vonnegut:
	# Eredeti cím*Megjelenési adatok*Megjelenés éve*Magyar fordítás
	def __init__(self, ec, ma, ev, mf):
		self.e_cim = ec
		self.adatok = ma
		self.ev = int(ev)
		self.forditas = mf.replace("\n", "")
def vonnegut():
	file = open("vonnegutB.txt",encoding="utf-8")
	file.readline()
	lines = file.readlines()
	for line in lines:
		adat = line.strip()
		adat2 = adat.split("*")
	print("\tElbeszélések száma: ", len(lines))
	return len(lines)
