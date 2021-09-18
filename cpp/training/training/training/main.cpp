#include <iostream>
#include <stdio.h>

int main() 
{
	printf("Hi there!\n");
	printf("%d", power(3, 3));

	std::cin.ignore();

	return 0;
}

int power(int x, unsigned p) 
{ 
	int answer;
	while (p--) {
		answer *= x;
	}
	return answer;
}