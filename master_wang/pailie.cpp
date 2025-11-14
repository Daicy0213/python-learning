
#include <stdio.h>

#define MAX 20

int c[MAX] = { 0 };
int M, N;

void print();
void comp(int);

int main()
{
	printf("Please input N M = ");
	scanf("%d %d", &N, &M);
	printf("N = %d, M = %d\n", N, M);

	comp(1);

	return 0;
}
void print()
{
	int i;
	for (i = 0; i < M; i++)
	{
		printf("%d ", c[i + 1]);
	}
	printf("\n");
}
void comp(int m)
{
	if (m == M + 1)
	{
		print();
	}
	else
	{
		for (c[m] = c[m - 1] + 1; c[m] <= N - M + m; c[m]++)
		{
			comp(m + 1);
		}
	}
}
