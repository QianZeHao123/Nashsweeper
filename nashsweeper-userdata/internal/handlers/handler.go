package handlers

import "github.com/gin-gonic/gin"

// PingHandler for testing service
func PingHandler(c *gin.Context) {
	c.JSON(200, gin.H{
		"message": "pong123",
	})
}
