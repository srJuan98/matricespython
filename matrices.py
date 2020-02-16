
class Matriz:

	def __init__(self,i,k):
		self.mat=list() 
		self.i=i
		self.k=k
		vector=list() 
		for n in range(0,i+2):
			vector.append("null") 
		
		for j in range(0,k+2):
			self.mat.append(vector)
		

	def  get(self,i,k): 
		fila=self.mat[i] 
		return fila[k] 

	def set(self,i,k,o):
		fila=self.mat[i] 
		fila.__setitem__(k,o)
		self.mat.__setitem__(i,fila) 

	def show(self): 
		for l in range(0,self.i):
			cadena=""
			print("\n") 
			fila=self.mat[l]
			for n in range(0,self.k):
				cadena=cadena+"  "+str(fila[n]) 
			print(cadena)

				














