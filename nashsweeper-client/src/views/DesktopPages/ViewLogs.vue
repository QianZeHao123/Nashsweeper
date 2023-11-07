<template>
    <div class="h-screen">
        <div class="mockup-window border border-base-300 h-4/5 w-2/3">
            <div class="w-full h-full">
                <div class="grid grid-rows-6 w-full h-full">
                    <div class="row-span-5">
                        <div class="grid grid-cols-10 w-full h-full">
                            <div class="w-full h-full border"></div>
                            <div class="col-span-8 w-full h-full border">
                                <ViewLogCom />
                            </div>
                            <div class="w-full h-full border"></div>
                        </div>
                    </div>
                    <div class="row-span-1">
                        <!-- ViewLogs -->
                        <div class="grid grid-cols-8 h-1/2 w-full justify-center items-center">
                            <div></div>
                            <div></div>
                            <div class="w-full h-full p-2"><button class="btn btn-primary w-full h-full">Previous</button></div>
                            <div></div>
                            <div></div>
                            <div class="w-full h-full p-2"><button class="btn btn-accent w-full h-full">Next</button></div>
                            <div></div>
                            <div></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import ViewLogCom from '../../components/DesktopComponents/ViewLogPage/ViewLogCom.vue'
export default {
    name: "ViewLogs",
    components: {
        // SideBar,
        // DataBarShow
        ViewLogCom
    },
    data() {
        return {
        }
    },
    methods: {

    },
    mounted() {

    },
}
</script>

<style scoped></style>