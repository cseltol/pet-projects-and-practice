#include <iostream>
#include <utility>

int main() {
  return 0;
}

// Bubble Sort

template<typename T>

void sort(T array[], std::size_t size) {
    for (std::size_t i = 0; i < size - 1; i++) {
        for (std::size_t j = 0; j < size - i - 1; j++) {
            if (array[i+1] < array[j]) {
                std::swap(array[j], array[j+1]);
            }
        }
    }
}