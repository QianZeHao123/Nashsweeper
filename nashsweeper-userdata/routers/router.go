package routers

import (
	"github.com/gin-gonic/gin"
	"nashsweeperUserData/internal/handlers"
)

// SetupRouter for defining router and return r
func SetupRouter() *gin.Engine {
	r := gin.Default()

	// define test router
	r.GET("/ping", handlers.PingHandler)
	r.GET("/DBcheck", handlers.CheckDBconnection)

	return r
}
