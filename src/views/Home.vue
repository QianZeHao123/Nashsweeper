<template>
    <div>
        <div class="mockup-window border bg-base-90 w-full">
            <div class="grid grid-cols-4 gap-1 w-full">
                <!-- 左侧Tabbar -->
                <SideBar />



                <!-- 右侧数据展示页面 -->
                <div class="col-span-3 h-full border-4">


                    <!-- <div class="grid grid-rows-3 gap-1">
                        <div class="row-span-2">1</div>
                        <div class="row-span-1">1</div>
                    </div> -->
                    <!-- <div class="h-2/3 border-4">
                        <div class="grid grid-cols-3 gap-0">
                            <div class="border col-span-2">1</div>
                            <div class="h-96 border">1</div>
                        </div>
                    </div>
                    <div class="h-1/3 border-4">
                        <div class="grid grid-cols-3 gap-0">
                            <div class="border h-72">1</div>
                            <div class="border h-72">1</div>
                            <div class="border h-72">1</div>
                        </div>
                    </div> -->
                    <div class="grid grid-rows-3 grid-cols-3 gap-2">
                        <div class="row-span-2 col-span-2 border-4">PartD</div>
                        <div class="row-span-2 border-4">PartE</div>
                        <div class="h-72 border-4">C-1</div>
                        <div class="h-72 border-4">C-2</div>
                        <div class="h-72 border-4">C-3</div>
                    </div>


                </div>



            </div>

        </div>
    </div>
</template>

<script>
import SideBar from "../components/SideBar.vue"
export default {
    name: "Home",
    components: {
        SideBar,
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