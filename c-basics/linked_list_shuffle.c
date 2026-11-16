/*
 * Author: xiaoyue-dev
 * Date: 2026-11-16 (整理上传日期)
 * Course: C Language Basics
 * Description: 这是一个链表重排（洗牌）程序。
 *              主要功能包括：读取静态链表、利用快慢指针寻找中点、反转后半段链表以及将两段链表交替合并。
 *              技术点：使用了数组模拟链表（静态链表）、快慢指针算法和链表原地反转与归并操作。
 */
#include <stdio.h>
// 定义节点结构体，模拟链表
struct Node {
    int element; 
    int next;   
};

int main() {
    int n;
    //使用 static 关键字将大数组放入静态存储区，防止栈溢出
    static struct Node arr[5000005] = {0};

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &arr[i].element, &arr[i].next);
    }

    // 【边界处理】如果只有一个节点或为空，直接输出并结束
    if (arr[0].next == -1) {
        printf("%d\n", arr[0].element);
        return 0;
    }

    // --- 第一步：使用快慢指针找到链表中点 ---
    int fast = 0, slow = 0;
    // fast 每次走两步，slow 每次走一步。当 fast 到达末尾时，slow 正好在中点
    while (fast != -1 && arr[fast].next != -1) {
        slow = arr[slow].next;             
        fast = arr[arr[fast].next].next;  
    }

    // --- 第二步：断开链表并反转后半部分 ---
    int second = arr[slow].next; // 保存后半部分链表的头节点下标
    arr[slow].next = -1;         // 断开前半部分和后半部分的连接

    // 反转后半部分链表
    int prev = -1, curr = second;
    while (curr != -1) {
        int next_temp = arr[curr].next; // 暂存下一个节点
        arr[curr].next = prev;          // 当前节点指向前一个（反转操作）
        prev = curr;                    // prev 前移
        curr = next_temp;               // curr 前移
    }
    second = prev; // 更新 second 为反转后的后半部分头节点

    // --- 第三步：交替合并两个链表 ---
    int first = 0; // 前半部分链表的头节点
    // 以后半部分为准循环（因为前半部分长度 >= 后半部分）
    while (second != -1) {
        int temp1 = arr[first].next; 
        int temp2 = arr[second].next; 

        // 执行插入操作：first -> second -> temp1
        arr[first].next = second;
        arr[second].next = temp1;

        // 移动指针到下一轮的位置
        second = temp2;
        first = temp1;
    }

    // --- 第四步：遍历并输出结果 ---
    int cur = 0, foot = 1; 
    while (cur != -1) {
        if (!foot) {
            printf(" "); 
        }
        printf("%d", arr[cur].element);
        foot = 0;
        cur = arr[cur].next; 
    }

    return 0;
}
