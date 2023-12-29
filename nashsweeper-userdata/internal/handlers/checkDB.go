package handlers

import (
	"github.com/gin-gonic/gin"
	"nashsweeperUserData/internal/config"
)

func CheckDBconnection(c *gin.Context) {
	cfg := config.LoadConfiguration("configs/db.json")
	config.ConnectDatabase(cfg)
	c.JSON(200, gin.H{
		"message": "DB connect success",
	})
}
