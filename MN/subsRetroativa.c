//IFCE - Engenharia de Computação - 30/08/19
//Cálculo Numérico
//João Feitoza Bisneto

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define EPSILON 0.000001

/*	Se houver memória disponível, a matriz bidimensional de doubles de "l" linhas e
	"c" colunas será alocada e devolvida através de um ponteiro. Caso contrário, 
	ela não aloca esta matriz e devolve um ponteiro nulo. 
*/
double **alocaMatriz(int l, int c){
	double **M;
	int i, j;

	M = malloc(sizeof(double)*l);			// Cria as linhas.
	
	if(M == NULL){							// Falta memória.
		return NULL; 
	}

	for(i=0; i<l; i++){
		M[i] = malloc(sizeof(double)*c);	// Cria as colunas. 
		if(M[i] == NULL){					// Caso alguma coluna não seja alocada:
			for(j=0; j<i; j++){				
				free(M[j]);					// Desaloca as linhas
			}
			free(M);						// Desaloca a matriz
			return NULL;
		}
	}

	return M;
}

//	Lê os valores para a matriz bidimensional de doubles de "l" linhas e "c" colunas.
void leMatriz(double **M, int l, int c){
	int i, j;

	for(i=0; i<l;i++){
		for(j=0; j<c;j++){
			printf("M[%d][%d]: ", i+1, j+1);
			scanf("%lf", &M[i][j]);
		}
	}
}

//	Imprime os valores da matriz bidimensional de doubles de "l" linhas e "c" colunas.
void imprimeMatriz(double **M, int l, int c){
	int i, j;
	
	for(i=0; i<l;i++){
		for(j=0; j<c;j++){
			printf("%10.4lf ", M[i][j]);
		}
		printf("\n");
	}
}

/* 	Recebe M, a matriz aumentada de um SLTS com n variáveis.
	Se o SL for determinado, coloca em x a solução do SL e devolve 0;
	Se for indeterminado, coloca em x uma solução e devolve 1;
	Se for incompatível, devolve 2;

	bi - o somatório for igual a zero, então tem solução.
*/
int subsRetroativa(double **M, int n, double X[]){
	int i, j, tipo = 0;
	double soma;

	for(i=n-1; i>=0; i--){
		soma = 0;
		for(j=i+1; j<n; j++){
			soma = soma + M[i][j] * X[j];
			}
		if(M[i][i] == 0){
			if(M[i][n] - soma < EPSILON){ 						//X[i] é variável livre.
				tipo = 1;
				X[i] = 0;
			}else{ 
				return 2;
			}
		}else{
			X[i] = (M[i][n] - soma) / M[i][i];
		}
	}

	return tipo;
}


int app(){
	int n, i, tipo;
	double **M, *X;

	printf("Quantidade de variaveis: ");
	scanf("%d", &n);

	M = alocaMatriz(n, n+1);
	X = malloc(sizeof(double)*n);

	if(M == NULL || X == NULL){ //Falta de memória
		printf("Problema.\n Falta de memoria.\n");
		return 1;
	}

	leMatriz(M, n, n+1);
	imprimeMatriz(M, n, n+1);

	tipo = subsRetroativa(M, n, X);
	
	if(tipo == 2){ printf("SL INCOMPATIVEL.\n"); }
	else{ 
		printf("SL %sDETERMINADO.\n", tipo?"IN":""); 
		for(i=0; i<n; i++){
			printf("x[%d]: %10.4lf\n", i+1, X[i]);
		}
	}
	return 0;
}

int main(void){
	app();
}
