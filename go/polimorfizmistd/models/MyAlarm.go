package models

import "time"

type MyAlarm struct {
	ID             int64
	WelcomeMessage string
	PlayDate       time.Time
}

func (a *MyAlarm) SetTime(time.Time) {
	panic("implement me")
}

func (a *MyAlarm) SetAlarmSound(string) {
	panic("implement me")
}

func (a *MyAlarm) PlayAlarm() {
	panic("implement me")
}
