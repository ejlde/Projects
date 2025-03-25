package main

import "fmt"

type numlist []int

func main() {
	n := createNumberSlice()
	n.checkEvenOrOdd()
}

func createNumberSlice() numlist {
	// Create a slice with initial length of 0 and capacity of 11
	numbers := make(numlist, 0, 11)

	// Append numbers 0 through 10
	for i := 0; i <= 10; i++ {
		numbers = append(numbers, i)
	}

	return numbers
}

func (n numlist) checkEvenOrOdd() {
	for _, value := range n {
		if value%2 == 0 {
			fmt.Printf("%v is even\n", value)
		} else {
			fmt.Printf("%v is odd\n", value)
		}
	}
}
