#include <stdio.h>

void useful_function_1() {
    asm("pop %rax; ret");
}

void useful_function_2() {
    asm("mov %rax, %rdi; ret");
}

int main() {
    printf("Hello, ROPgadget!\n");
    useful_function_1();
    useful_function_2();
    return 0;
}

