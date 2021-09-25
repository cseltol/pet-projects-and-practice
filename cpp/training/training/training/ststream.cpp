#include "stdafx.h"
#include <iostream>
#include <strstream>
#include <string>

using namespace std;

int _tmain(int argc, _TCHAR* argv []) 
{
	strstream xstr;
	for (int i = 0; i < 10; i++) 
	{
		xstr << "Demo" << i << endl;
	}
	cout << xstr.str();
	string str;
	str.assign(xstr.str(), xstr.pcount());
	cout << str.c_str();
	return 0;
}