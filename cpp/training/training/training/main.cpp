#include <iostream>

int power(int x, unsigned p)
{
	int answer;
	if (p == 0) 
	{
		answer = 0;
	}
	else 
	{
		answer = 1;
		for (int i = 0; i < p; i++) 
		{
			answer *= x;
		}
	}
	return answer;
}

int main() 
{
	std::cout << power(3, 3) << std::endl;
	std::cin.ignore();

	return 0;
}