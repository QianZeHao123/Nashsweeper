<template>
    <div class="h-screen">
        <div class="mockup-window border border-base-300 h-4/5 w-2/3">
            <div class="w-full h-full">
                <div class="grid grid-rows-6 w-full h-full">
                    <div class="row-span-5">
                        <div class="grid grid-cols-10 w-full h-full">
                            <div class="w-full h-full border"></div>
                            <div class="col-span-8 w-full h-full border">
                                <ViewResultCom />
                            </div>
                            <div class="w-full h-full border"></div>
                        </div>
                    </div>
                    <div class="row-span-1">
                        <!-- ViewResult -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import ViewResultCom from '../../components/DesktopComponents/ViewResultPage/ViewResultCom.vue'
export default {
    name: "ViewResult",
    components: {
        // SideBar,
        ViewResultCom
        // DataBarShow
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