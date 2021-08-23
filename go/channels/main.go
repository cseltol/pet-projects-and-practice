package main

import (
	"fmt"
	"math/rand"
	"time"
)

type Producer struct {
	OutChan chan int
}

func (p *Producer) getOutChan() <-chan int { // Канал только для чтения (Инкапсулированный)
	return p.OutChan
}

func (p *Producer) produce() {
	for {
		time.Sleep(3 * time.Second)
		p.OutChan <- rand.Int()
	}
}

func main() {
	//readChan := make(chan int, 10)
	prod := Producer{
		OutChan: make(chan int, 10),
	}
	go prod.produce()

	// Первый Вариант (считается лучшим)
	// for i := range prod.getOutChan() {
	// 	fmt.Println("Got message from chan:", i)
	// }

	// Второй Вариант
	// for {
	// 	i := <- readChan
	// 	fmt.Println("Got message from chan:", i)
	// }

	prodChan := prod.getOutChan()
	ticker := time.NewTicker(2 * time.Second)
	for {
		select { // Каналы не блокируется дург другом в select{}
		case a := <-prodChan:
			fmt.Println("Got message from producer", a)
		case <-ticker.C:
			fmt.Println("Got message from ticker")
		}
	}
}
