#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> grid;

bool isSafe(vector<vector<int>>& grid,int row,int col){
	bool enemy = false;
	int N = grid.size();

	/*Debido a que las reinas se posicionan de izquierda a derecha
	no hay necesidad de revisar hacia adelante en busca de una reina*/

	//revisar hacia la izquierda
	if(col-1 >= 0 && !enemy){
		for(int i=col-1 ; i>=0 && !enemy ; i--){
			if(grid[row][i]){
				enemy = true;
				//puts("a la izquierda");
			}
		}
	}


	//revisar diagonal superior izquierda
	if(row-1 >= 0 && col-1 >= 0 && !enemy){
		int x = row-1;
		int y = col-1;
		while(x >= 0 && y >= 0 && !enemy){
			if(grid[x][y]){
				enemy = true;
				//puts("diagonal superior izquierda");
			}
			x--;
			y--;
		}
	}


	//revisar diagonal inferior izquierda
	if(row+1 < N && col-1 >= 0 && !enemy){
		int x = row+1;
		int y = col-1;
		while(x < N && y >= 0 && !enemy){
			if(grid[x][y]){
				enemy = true;
				//puts("daigonal inferior izquierda");
			}
			x++;
			y--;
		}
	}

	if(enemy){
		return false;
	}else{
		return true;
	}
}

void createGrid(vector<vector<int>>& grid,int N){
	grid.resize(N,vector<int>(N));
}

void showGrid(vector<vector<int>>& grid,int N){
	puts("");
	for(int i=0 ; i<N ; i++){
		for(int j=0 ; j<N ; j++){
			cout << grid[i][j] << " ";
		}
		puts("");
	}
}

bool isSolvable(vector<vector<int>>& grid,int col,int N){
	/*Caso base: si todas las reinas estan situadas*/
	if(col >= N){
		return true;
	}
	/*considerar la columna actual y probar situando
	la reina en todas las filas una por una*/
	for(int i=0 ; i<N ; i++){
		if(isSafe(grid,i,col)){
			grid[i][col] = 1;

			/*recursivamente situar las demas reinas*/
			if(isSolvable(grid,col+1,N)){
				return true;
			}

			/*si situando una reina en grid[i][col] no nos da una
			solucion entonces retirar la reina de esa posicion, haciendo backtracking*/
			grid[i][col] = 0;
		}
	}
	return false;
}

void solve(vector<vector<int>>& grid,int N){
	if(!isSolvable(grid,0,N)){
		puts("no tiene solucion");
	}else{
		puts("si tiene solucion");
	}
}

int main(){
	puts("definir N");
	int N;
	cin >> N;	

	createGrid(grid,N); //crear tablero	
	solve(grid,N);
	showGrid(grid,N);

	return 0;
}