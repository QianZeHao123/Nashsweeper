// Package config Parsing the configs/db.json file to get the info of DB
package config

import (
	"encoding/json"
	"log"
	"os"
)

type Config struct {
	DBUsername string `json:"DBUsername"`
	DBPassword string `json:"DBPassword"`
	DBHost     string `json:"DBHost"`
	DBPort     string `json:"DBPort"`
	DBName     string `json:"DBName"`
}

func LoadConfiguration(file string) Config {
	var config Config
	configFile, err := os.Open(file)
	defer func(configFile *os.File) {
		err := configFile.Close()
		if err != nil {
			return
		}
	}(configFile)
	if err != nil {
		log.Fatalf("Failed to open config file: %v", err)
	}
	jsonParser := json.NewDecoder(configFile)
	err = jsonParser.Decode(&config)
	if err != nil {
		return Config{}
	}
	return config
}
