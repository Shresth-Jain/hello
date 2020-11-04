def fix(A,len):
	for i in range(0,len):
		if(A[i]!=-1 and A[i]!=i):
			x=A[i];
			while(A[x]!=-1 and A[x]!=x):
				y=A[x]
				A[x]=x
				x=y
			A[x]=x;
			if(A[i]!=i):
				A[i]=-1;

#Driver function
A=[-1,-1,6,1,9,3,2,-1,4,-1]
fix(A,len(A))
for i in range(0,len(A)):
	print(A[i],end=',')

		
