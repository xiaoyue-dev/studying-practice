/*
 * Author: xiaoyue-dev 
 * Date: 2026-11-16 (整理上传时间)
 * Course: C Language Basics
 * Description: 这段代码实现了数组的循环左移。
 *              它接收一个数组和移动位数 k，
 *              将数组最前面的 k 个元素依次移到数组末尾。
 *              例如，[1, 2, 3, 4, 5] 左移 2 位后变为 [3, 4, 5, 1, 2]。
 */
#include<stdio.h>
#define N 100
void fun(int x[],int n,int k)//实现循环左移操作
{
	int i,t;
	while(k--)
	{
		t=x[0];
		for(i=0;i<n-1;i++)
			x[i]=x[i+1];

		x[n-1]=t;
	}
}
int main()
{
	int a[N],i,n,k;
	printf("输入元素个数n和移动位置k: ");
	scanf("%d%d",&n,&k);
	printf("输入%d个元素: ",n);
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	fun(a,n,k);
	printf("\n");
	for(i=0;i<n;i++)
		printf("%d ",a[i]);
	printf("\n");
	return 0;
}
