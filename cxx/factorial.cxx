#include <iostream>

template<size_t n>
struct factorial
{
  static const size_t result = factorial<n - 1>::result * n;
};

template<>
struct factorial<1>
{
  static const size_t result = 1;
};

int main()
{
  std::cout << "5! is is " << factorial<5>::result << "\n";
}
