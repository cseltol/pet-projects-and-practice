package main

import (
	"fmt"
	"polimorfizmistd/models"
	"strings"
	"time"
)

type Parser interface {
	Parse() []string
}

func main() {
	s := strings.Replace("Hello!", "Hello", "Hi there", -1)
	fmt.Println(s)

	currentDate := time.Now()
	FirstDate := time.Date(currentDate.Year(), currentDate.Month(), 1, 0, 0, 0, 0, currentDate.Location())
	FirstDate = FirstDate.AddDate(0, 1, 0)
	fmt.Println(FirstDate.Add(3 * time.Hour).Day())
	currentDate = currentDate.AddDate(1, 2, 3)

	// currentDate.Sub()
	// currentDate.Truncate()

	user := models.NewUser("Daniel", "Jerkinoff", 500)
	user.GetSalary()

	// models.MyAlarm{
	// 	ID:             1,
	// 	WelcomeMessage: "Hi there!",
	// }
	// alarmExample(MyAlarm)
}

func alarmExample(alarm models.Alarm) {
	alarm.PlayAlarm()
	alarm.SetAlarmSound("gagaga")
}
