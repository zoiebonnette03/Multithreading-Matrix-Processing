Multithreading matrix processing in Python for Concepts of Programming class. 

Take in a large matrix and alters data based loosely on Conway's Game of Life algorithm:
- A live cell dies if it has 0, 1, 4, 6, or 8 alive neighbors
- A dead cell becomes alive if it has 2, 4, 6, or 8 alive neighbors
Dead cells are denoted as '.' while alive cells are 'O'

Utilized Texas Tech's High Performance Computing Center to run using a Professor provided grading script. 

Runtime summary for different size matrices and processes:
quanah:/project3$ cat full_timing. log
Run Time Results:
100x100 - 1 process: 			    4.076358571 seconds
100x100 - 2 processes: 			  1.737369919 seconds
100x100 - 4 processes:			  1.282572122 seconds
100x100 - 8 processes:			  1.648781257 seconds
100x100 - 16 processes:			  2.696761900 seconds
100x100 - 32 processes:			  4.769030670 seconds
1000x1000 - 1 process: 			  313.062224337 seconds
1000×1000 - 2 processes:		  201.814996608 seconds
1000x1000 - 4 processes:		  155.246603184 seconds
1000×1000 - 8 processes:		  157.491126220 seconds
1000x1000 - 16 processes: 		220.765658158 seconds
1000x1000 - 32 processes: 		326.056936178 seconds
10000×10000 - 9 processes:		18676.773668914 seconds
10000x10000 - 18 processes:		24236.267076728 seconds
10000x10000 - 36 processes:		34693.621358001 seconds

Note: Runtime is fastest on 4-8 processes since I send each process a full matrix. The fix would be sending each matrix only the portion of each matrix it needs. 
