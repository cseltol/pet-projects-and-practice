<<<<<<< HEAD
package main

import (
	"context"
	"log"
	"net"
	"os"
	"os/signal"
	"time"
)

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	go handleSignals(cancel)
	if err := startServer(ctx); err != nil {
		log.Fatal(err)
	}
}

func handleSignals(cancel context.CancelFunc) {
	sigChan := make(chan os.Signal)
	signal.Notify(sigChan, os.Interrupt)
	for {
		signal := <-sigChan
		switch signal {
		case os.Interrupt:
			cancel()
			return err
		}
	}
}

func startServer(ctx context.Context) {
	localAddres, err := net.ResolveTCPAddr("tcp", ":3000")
	if err != nil {
		return err
	}

	listener, err := net.ListenTCP("tcp", localAddres)
	if err != nil {
		return err
	}

	defer listener.Close()

	for {
		select {
		case <-ctx.Done():
			log.Println("Server stopped working")
			return
		default:
			if err := listener.SetDeadline(time.Now().Add(time.Second)); err != nil {
				return err
			}

			_, err := listener.Accept()
			if err != nil {
				if os.IsTimeout(err) {
					continue
				}

				return err
			}

			log.Println("New connection was found")
		}

	}

}
=======
package main

import (
	"context"
	"log"
	"net"
	"os"
	"os/signal"
	"time"
)

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	go handleSignals(cancel)
	if err := startServer(ctx); err != nil {
		log.Fatal(err)
	}
}

func handleSignals(cancel context.CancelFunc) {
	sigChan := make(chan os.Signal)
	signal.Notify(sigChan, os.Interrupt)
	for {
		signal := <-sigChan
		switch signal {
		case os.Interrupt:
			cancel()
			return err
		}
	}
}

func startServer(ctx context.Context) {
	localAddres, err := net.ResolveTCPAddr("tcp", ":3000")
	if err != nil {
		return err
	}

	listener, err := net.ListenTCP("tcp", localAddres)
	if err != nil {
		return err
	}

	defer listener.Close()

	for {
		select {
		case <-ctx.Done():
			log.Println("Server stopped working")
			return
		default:
			if err := listener.SetDeadline(time.Now().Add(time.Second)); err != nil {
				return err
			}

			_, err := listener.Accept()
			if err != nil {
				if os.IsTimeout(err) {
					continue
				}

				return err
			}

			log.Println("New connection was found")
		}

	}

}
>>>>>>> b78a27678aac6d35f3c7e91a7b014a8e28813a87
