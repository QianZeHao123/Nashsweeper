# Nashsweeper
## 0x00 Introduction
Nash equilibrium is a core concept of game theory. This repo shows a playful introduction of Nash equilibrium and designs a game named Nashsweeper, which is a game designed to find the pure strategy.<br>
![](nashsweeper-front/public/JohnNash.svg)
## 0x01 How to use?
### In dev mode
* If you want to run this project, you should start the backend service firstly by changing your terminal path to [nashsweeper-banckend](./nashsweeper-backend/) and reading the [readme file](nashsweeper-backend/README.md) carefully. Then you should run the frontend service by changing your disk to [nashsweeper-front](./nashsweeper-front/) and follow the [readme file](nashsweeper-front/README.md) step by step.
* What deserves your attention most is that both the backend and frontend services ports cannot be taken by other applications, or you won't be able to run it correctly.
### In Docker Micro-service mode
Coming soon!
## 0x02 Software Architecture
### Frontend User Interface Render
```mermaid
graph LR
App[App.vue]--Router.js-->HomePage(HomePage)
HomePage-->SideBar(SideBar)
HomePage-->DataBarShow(DataBarShow)
SideBar--VueComponent-->PartA[PartA]
SideBar--VueComponent-->PartB[PartB]
SideBar--VueComponent-->PartC[PartC]
DataBarShow--VueComponent-->PartD[PartD]
DataBarShow--VueComponent-->PartE[PartE]
DataBarShow--PlayerInfo-->PartC-1[Part C-1]
DataBarShow--BestChoice-->PartC-2[Part C-2]
DataBarShow--StrategyScore-->PartC-3[Part C-3]
PartB--TimeCom-->TimeCounterCom
PartE--GetPlayerRank-->PlayerRate
PartE--Gitee, Github Link-->ProjLink
```

### Backend DataProcess
```mermaid
sequenceDiagram
    participant Backend Server
    participant Frontend
    participant NashsweeperPlayer
    NashsweeperPlayer -->> Backend Server: Upload Game Data
    Backend Server ->> NashsweeperPlayer: Template Render Page: Return Nashsweeper
    loop Load Tricker
        Backend Server -->> Backend Server: Load Game Data
    end
    Backend Server ->> Frontend: JsonData: Player Rank
    Frontend -->> NashsweeperPlayer: Player Rank
```
