package main

import (
	"fmt"
	"sync"
)

type MObject struct {
	MapMutex *sync.Mutex
	Map      map[string]string
}

func main() {
	object := MObject{
		Map:      make(map[string]string, 0),
		MapMutex: new(sync.Mutex),
	}
	WriteToMap(&object)
}

func WriteToMap(object *MObject) {
	object.MapMutex.Lock()
	defer object.MapMutex.Unlock()
	object.Map["hi"] = "123"
}

func MessageInThread() {
	wg := new(sync.WaitGroup) // wg == wait group
	for i := 0; i < 10; i++ {
		go Print("Hi there!", wg)
	}
	wg.Wait()
}

func Print(word string, wg *sync.WaitGroup) {
	wg.Add(1)
	defer wg.Done()
	fmt.Println(word)
}

// Используется в редких случаях
func MessageInThread_Second() {
	once := sync.Once{}
	for i := 0; i < 10; i++ {
		once.Do(SecondPrint)
	}
}

func SecondPrint() {
	fmt.Println("Hi there!")
}
