/*
 * Author: xiaoyue-dev 
 * Date: 2026-11-16 (整理上传日期 )
 * Course: C Language Basics
 * Description: 这是一个基于贪心策略的竞赛胜场统计程序。
 *              主要功能包括：读取两组数据、升序排序、模拟最优对战并计算最大获胜次数。
 *              技术点：使用了冒泡排序算法（bubbleSort）、数组元素移动操作和贪心匹配逻辑。
 */
#include <stdio.h>
#define N 50000
/**
 * 冒泡排序函数：将数组按从小到大排序
 */
void bubbleSort(int list[], int n)
{
	int i,j,t;
	for(i=0;i<n-1;i++)
	{
		for(j=0;j<n-i-1;j++)
		{
			if(list[j]>list[j+1])
			{
				t=list[j];
				list[j]=list[j+1];
				list[j+1]=t;
			}
		}
	}
}

int main ()
{
	int n,u[N]={0},v[N]={0},win=0,i,j,k,l;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{scanf("%d",&u[i]);}
	for(i=0;i<n;i++)
	{scanf("%d",&v[i]);}
     bubbleSort(u,n);
	 bubbleSort(v,n);
	 for(i=0;i<n;i++)
	 {
		 for(j=0;j<n;j++)
		 {
			 if(u[j]>v[i])
			 {
				 win++;
				for(k=j;k<n-1;k++)
				{
					u[k]=u[k+1];
				}
				 break;
			 }
		 }
		 if(j==n)
		 {
			for(l=0;l<n-1;l++)
				{
					u[l]=u[l+1];
				}
		 }
	 }
	 printf("%d",win);
}
