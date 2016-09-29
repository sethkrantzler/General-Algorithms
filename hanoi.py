import copy
pastStates = []
systemState = []
completedState = []

def towerSolver():
	print "Please enter the number of blocks: "
	blocks = int(raw_input())
	print "Please enter the number of pegs: "
	rows = int(raw_input())
	global pastStates
	counter = 1
	pastStates = []
	topBlocks = []
	global systemState
	systemState = []
	completedState = []
	stuckCounter = -2
	sourceT = [x for x in xrange(1,blocks+1)]

	emptyT = [0 for x in xrange(1,blocks+1)]
	systemState.append(copy.deepcopy(sourceT))
	for row in xrange(0,rows-1):
		systemState.append(copy.deepcopy(emptyT))
		completedState.append(copy.deepcopy(emptyT))
	completedState.append(copy.deepcopy(sourceT))


	lastPegMoved = blocks

	complete = False

	def topBlockFinder():
		topBlocks = []
		for i in xrange(0,len(systemState)):
			for j in xrange(0,len(systemState[i])):
				if j == len(systemState[i])-1:
					topBlocks.append(systemState[i][j]);
				elif systemState[i][j] == 0:
					continue
				else:
					topBlocks.append(systemState[i][j])
					break
		return topBlocks



	def hasLegalMove(blockToCheck, topBlocks):
		hasLegalMoveAnswer = 'nlm'
		global systemState
		for i in xrange(0,len(topBlocks)):
			if topBlocks[i] == blockToCheck:
				continue
			elif topBlocks[i] < blockToCheck and  topBlocks[i]!= 0:
				continue
			else:
				testState = copy.deepcopy(systemState)
				for j in xrange(0,len(topBlocks)):
					if topBlocks[j] == blockToCheck:
						for z in xrange(0,len(systemState[j])):
							if systemState[j][z] == blockToCheck:
								testState[j][z]= 0
								break
						break

				if topBlocks[i]== 0:
					testState[i][-1] = blockToCheck
				else:
					for c in xrange(0,len(systemState[i])):
						if systemState[i][c+1] == topBlocks[i]:
							testState[i][c] = blockToCheck
							break
				moveExists = False
				for x in xrange(0, len(pastStates)):
					if pastStates[x] == testState:
						moveExists = True
					else:
						continue
				if not moveExists:
					systemState = testState
					return "We made a move"


		return hasLegalMoveAnswer



	def towerMover():
		topBlocks = topBlockFinder()
		didMove = False
		global systemState
		global stuckCounter
		for i in xrange(0,len(topBlocks)):
			if topBlocks[i] == 0:
				continue
			else:
				blockToMove = topBlocks[i]
				if hasLegalMove(blockToMove, topBlocks) != 'nlm':
					didMove = True
					stuckCounter = -1
					break
				else:
					continue
		if not didMove:
			systemState = copy.deepcopy(pastStates[stuckCounter -1 ])
			stuckCounter-=2

	print "----------------INITIAL TOWER------------------"
	towerHeader = ""
	towerDisplay = ""
	for tower in xrange(0,rows):
		towerHeader += "Tower %r " %(tower + 1)
	print towerHeader
	for c in xrange(0,len(systemState[0])):
		for d in xrange(0, rows):
			towerDisplay+= "%r \t" %(systemState[d][c])
			if d == rows-1:
				print towerDisplay
				towerDisplay = ""
	while not complete:
		pastStates.append(copy.deepcopy(systemState))
		towerMover()
		if systemState == completedState:
			complete = True
		print "----------------MOVE %r------------------" %(counter)
		print towerHeader
		for a in xrange(0,len(systemState[0])):
			for b in xrange(0, rows):
				towerDisplay+= "%r \t" %(systemState[b][a])
				if b == rows-1:
					print towerDisplay
					towerDisplay = ""
		counter+=1

while True:
	towerSolver()
