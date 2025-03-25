package main

import (
	"fmt"
)

type contactInfo struct {
	email   string
	zipCode int
}

type person struct {
	firstName string
	lastName  string
	contactInfo
}

func main() {
	jim := person{
		firstName: "Jim",
		lastName:  "Party",
		contactInfo: contactInfo{
			email:   "jim@gmail.com",
			zipCode: 94000,
		},
	}
	// Give me the memory address of this var
	// value to address & pointer = &jim
	jim.updateName("jimmy")
	jim.print()

}

// *pointer give me the value this memory address is pointing at
// *person = pointer to a person type not an operator
func (pointerToPerson *person) updateName(newFirstaname string) {
	(*pointerToPerson).firstName = newFirstaname // address to value *
}

func (p person) print() {
	fmt.Printf("%+v", p)
}

// Value types -- need pointers to change in a function
// int
// float
// string
// bool
// structs

// Reference Types -- dont need pointers to update values
// slices
// maps
// channels
// pointers
// functions
