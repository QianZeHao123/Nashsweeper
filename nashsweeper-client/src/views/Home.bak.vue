<template>
    <div>
        <div class="mockup-window border bg-base-90 w-full">
            <div class="grid grid-cols-4 gap-1 w-full">
                <!-- 左侧Tabbar -->
                <SideBar />
                <!-- 右侧数据展示页面 -->
                <DataBarShow />
            </div>
        </div>
    </div>
</template>

<script>
import SideBar from "../components/SideBar.vue"
import DataBarShow from "../components/DataBarShow.vue"
export default {
    name: "Home",
    components: {
        SideBar,
        DataBarShow
    },
    data() {
        return {}
    },
    methods: {
        // Alert_version: alert('For security reasons, this version does not connect to the backend.'),
        // Alert_connection: alert('Thank you for your understanding, the full version of the program is detailed at: https://gitee.com/qian_zehao/nashsweeper'),
    },
    mounted() {
        // Alert_version(),
        // Alert_connection(),
    },
}
</script>

<style scoped></style>