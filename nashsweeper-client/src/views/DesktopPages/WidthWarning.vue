<template>
    <div>
        <div class="mockup-window border border-base-300 h-screen">
            <div class="flex justify-center px-4 py-16 border-t border-base-300">
                <div>Welcome to Nashsweeper!<br /><br />
                    We have detected that the Width of your screen is below nashsweeper requirement (1400px).<br /><br />
                    For normal use, please replace a device with a larger screen /(ㄒoㄒ)/~~
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import SideBar from "../components/SideBar.vue"
// import DataBarShow from "../components/DataBarShow.vue"
export default {
    name: "WidthWarning",
    components: {
        // SideBar,
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