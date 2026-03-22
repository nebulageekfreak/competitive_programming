#include <iostream>

int main() {
  int watermelon;

  std::cin >> watermelon;

  if (watermelon >= 4 && watermelon % 2 == 0) {
    std::cout << "YES";
  } else {
    std::cout << "NO";
  }
}
