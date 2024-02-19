#include "pch.h"
#include "framework.h"


bool isPrime(int _number)
{
	for (int i = 2; i < _number; ++i)
	{
		if (_number % i == 0)
		{
			return false;
		}
	}

	return true;
}
