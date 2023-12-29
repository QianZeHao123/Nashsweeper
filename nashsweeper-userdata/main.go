package main

import (
	"log"
	"nashsweeperUserData/routers"
)

func main() {
	//cfg := config.LoadConfiguration("configs/db.json")

	//config.ConnectDatabase(cfg)

	r := routers.SetupRouter()
	// run server
	err := r.Run(":9999")
	if err != nil {
		// return
		log.Fatalf("Failed to run server: %v\n", err)
	}
}
