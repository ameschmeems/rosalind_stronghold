def mendel(x: int, y: int, z: int) -> float:
	#chance of recessive
    total = x+y+z
    twoRecess = (z/total)*((z-1)/(total-1))
    twoHetero = (y/total)*((y-1)/(total-1))
    heteroRecess = (z/total)*(y/(total-1)) + (y/total)*(z/(total-1))

    recessProb = twoRecess + twoHetero*1/4 + heteroRecess*1/2
    return (1 - recessProb)
