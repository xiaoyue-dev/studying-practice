/*
 * Author: xiaoyue-dev 
 * Date: 2026-11-16 (整理上传时间)
 * Course: C Language Basics
 * Description: 这是一个计算非负整数阶乘的程序。
 *              主要功能包括：读取用户输入、递归计算阶乘、输出计算结果。
 *              技术点：使用了函数递归调用、无符号整型(unsigned int)和标准输入输出。
 */
#include <stdio.h>
unsigned int getfactorial (unsigned int n);// 函数声明：计算无符号整数的阶乘
int main ()
{
	unsigned int n;
	scanf("%u",&n);
	printf("%u",getfactorial(n));
}
/**
 * 递归计算阶乘函数
 * @param n 要计算阶乘的非负整数
 * @return n 的阶乘值（n!）
 */
unsigned int getfactorial (unsigned int n)
{
	unsigned int result;
	if(n==1)
		result=1;
	else
		result=n*getfactorial(n-1);
	return result;
}
