import os, os.path

for i in range(0, 20):
	p = f"./template/ex{i:02d}"
	if not os.path.exists(p):
		os.mkdir(p)