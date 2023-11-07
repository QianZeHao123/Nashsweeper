<template>
    <div>
        <!-- Desktop Page -->
        <div class="h-screen">
            <div class="grid grid-cols-5 w-full h-full">
                <div class="border h-full" id="SideBar">
                    <div class="grid grid-rows-3 h-full">
                        <div>
                            <GameSetting />
                        </div>
                        <div class="border">
                            <GameButton />
                        </div>
                        <div class="border">
                            <GameOperation />
                        </div>
                    </div>
                </div>
                <div class="border h-full col-span-4" id="MainPart">
                    <div class="grid grid-rows-3 w-full h-full">
                        <div class="border row-span-2" id="game_checker_and_userranking">
                            <div class="grid grid-cols-3 w-full h-full">
                                <div class="border col-span-2">
                                    <ChessBoard />
                                </div>
                                <div class="border">
                                    <ProjectLink />
                                    <UserRank />
                                </div>
                            </div>
                        </div>
                        <div class="border">
                            <div class="grid grid-cols-3 w-full h-full" id="game_log">
                                <div class="border flex justify-center" id="NEr">
                                    <NeLog />
                                </div>
                                <div class="border flex justify-center" id="BRr">
                                    <BrLog />
                                </div>
                                <div class="border flex justify-center" id="ULr">
                                    <UoLog />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import SideBar from "../components/SideBar.vue"
// import DataBarShow from "../components/DataBarShow.vue"
import GameSetting from "../components/DesktopComponents/GameSetting.vue";
import GameButton from "../components/DesktopComponents/GameButton.vue";
import GameOperation from "../components/DesktopComponents/GameOperation.vue";

import ChessBoard from "../components/DesktopComponents/ChessBoard.vue";

import ProjectLink from "../components/DesktopComponents/ProjectLink.vue"
import UserRank from "../components/DesktopComponents/UserRank.vue"

import BrLog from "../components/DesktopComponents/UserLog/BrLog.vue";
import NeLog from "../components/DesktopComponents/UserLog/NeLog.vue";
import UoLog from "../components/DesktopComponents/UserLog/UoLog.vue";

export default {
    name: "Desktop",
    components: {
        // SideBar,
        // DataBarShow
        GameSetting,
        GameButton,
        GameOperation,
        BrLog,
        NeLog,
        UoLog,
        ChessBoard,
        ProjectLink,
        UserRank
    },
    data() {
        return {}
    },
    methods: {
        // To prevent front-end interface rendering failures, specify a minimum screen width.
        checkScreenWidth() {
            const minWidth = 1300;
            const GetScreenWidth = window.innerWidth < minWidth
            if (GetScreenWidth) {
                console.log("Unsupport Screen Width")
                this.$router.push({ name: 'WidthWarning' });
            }
            // else {
            //     this.$router.push({ name: 'Desktop' });
            // }
        },
    },
    mounted() {
        setInterval(() => {
            this.checkScreenWidth();
        }, 100)
    },
}
</script>

<style scoped></style>