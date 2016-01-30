import time
from dinit import max_flow, max_flow_print
import numpy as np

def run(do_print):
	if do_print:
		t0=time.clock()
		ID=0
		while ID<100:
			max_flow_print(ID)
			ID+=1
		td=time.clock() - t0
		td=td/100
		f2 = open('runtime.txt', 'w')
		f2.write('Dinit: '+str(td)+' seconds\n')
		f2.close()
	else:
		t0=time.clock()
		ID=0
		while ID<100:
			f0=open('graph_flow_'+str(ID)+'.txt','r')
			l=np.loadtxt(f0)
			print(l==max_flow(ID))
			ID+=1
			f0.close
		td=time.clock() - t0
		td=td/100
		f2 = open('runtime.txt', 'w')
		f2.write('Dinit: '+str(td)+' seconds\n')
		f2.close()
		
#renvoie true quand c'est ok pour chaque graphe :
run(False)
