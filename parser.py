import sys
import os
import operator
import math	
from math import log10

class Events(object):
	eventtype='';
	itempressed='';
	xpos = '';
	ypos = '';	

		

if __name__ == "__main__":	
	script_dir = os.path.dirname(__file__)
	rel_path = "clean.txt"
	abs_file_path = os.path.join(script_dir, rel_path)
	eventslist = []
	eventDict = {}

	f=open(abs_file_path, 'r')
	for line in f:
		"""key pressed event"""
		if "key press" in line:
			# print line
			line = f.next()
			line = f.next()
			line = f.next()
			raw_line = line.split()
			keypressed=raw_line[-1]
			event1 = Events();
			event1.eventtype='kp'
			event1.itempressed=keypressed
			eventslist.append(event1)
			eventstr = event1.eventtype+','+keypressed
			if eventstr in eventDict:
				eventDict[eventstr]= eventDict[eventstr] + 1;
			else:
				eventDict[eventstr]= 1;


		elif "key release" in line:
			line = f.next()
			line = f.next()
			line = f.next()
			raw_line = line.split()
			keyrelease=raw_line[-1]
			event2 = Events();
			event2.eventtype='kr'
			event2.itempressed=keyrelease		
			eventslist.append(event2)
			eventstr = event2.eventtype+','+keyrelease
			if eventstr in eventDict:
				eventDict[eventstr]= eventDict[eventstr] + 1;
			else:
				eventDict[eventstr]= 1;


		elif "button press" in line:
			line = f.next()
			line = f.next()
			line = f.next()
			raw_line = line.split()
			mousenumclicked = raw_line[-1]
			line = f.next()
			raw_line = line.split()
			xpos = raw_line[1]
			ypos = raw_line[2]
			event3 = Events()
			event3.eventtype='bp'
			event3.itempressed=mousenumclicked
			event3.xpos = xpos
			event3.ypos = ypos
			eventslist.append(event3)
			eventstr= event3.eventtype + ',' + event3.itempressed + ',' + event3.xpos + ',' + event3.ypos
			if eventstr in eventDict:
				eventDict[eventstr]= eventDict[eventstr] + 1;
			else:
				eventDict[eventstr]= 1;

		elif "button release" in line:
			line = f.next()
			line = f.next()
			line = f.next()
			raw_line = line.split()
			mousenumclicked = raw_line[-1]
			line = f.next()
			raw_line = line.split()
			xpos = raw_line[1]
			ypos = raw_line[2]
			event4 = Events()
			event4.eventtype='br'
			event4.itempressed=mousenumclicked
			event4.xpos = xpos
			event4.ypos = ypos
			eventslist.append(event4)
			eventstr= event4.eventtype + ',' + event4.itempressed + ',' + event4.xpos + ',' + event4.ypos
			if eventstr in eventDict:
				eventDict[eventstr]= eventDict[eventstr] + 1;
			else:
				eventDict[eventstr]= 1;
	
	sorted_events = sorted(eventDict.items(), key=operator.itemgetter(1), reverse=True)
	# print(sorted_events)

	probarray = []
	maxfrequency = sorted_events[0][1]
	# print maxfrequency
	for event in sorted_events:
	 	probarray.append( float(event[1]) /maxfrequency)
	
	heuristicarr=[]	
	for i in range(0,len(probarray)):
		if (probarray[i]==1):
			heuristicarr.append(0)
		else:
			pi = probarray[i]
			hi = ((-1)*pi*log10(pi)) - ((1-pi)*log10((1-pi)))
			heuristicarr.append(hi)

	# print heuristicarr

	htotalold = 0
	releventevents = []
	for i in range(0,len(probarray)):
		partialsum=0
		for j in range(0, i):
			partialsum += heuristicarr[j]
		hcurrent = (1.0)/(i+1)*(partialsum)			
		if (hcurrent >= htotalold):
			releventevents.append(sorted_events[i])
			htotalold = hcurrent		
		else:
			# print hcurrent
			# print htotalold
			break

	print(releventevents)
