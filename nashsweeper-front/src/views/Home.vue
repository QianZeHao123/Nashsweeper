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
    methods: {},
    mounted() { },
}
</script>

<style scoped>

</style>