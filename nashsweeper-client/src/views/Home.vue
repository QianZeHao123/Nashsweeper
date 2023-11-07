<template>
    <div>

        <div class="mockup-window border border-base-300 h-screen">
            <div class="flex justify-center px-4 py-16 border-t border-base-300">
                <div>Welcome to Nashsweeper!<br /><br />
                    The program is detecting your device type, please wait a momment...<br /><br />
                    We have detected that your system is {{ userAgent }}<br /><br />
                    Redirecting...
                </div>
            </div>
        </div>

    </div>
</template>

<script>
// import SideBar from "../components/SideBar.vue"
// import DataBarShow from "../components/DataBarShow.vue"
export default {
    name: "Home",
    components: {
        // SideBar,
        // DataBarShow
    },
    data() {
        const userAgent = window.navigator.userAgent.toLowerCase();
        return {
            userAgent
        }
    },
    methods: {
        // Alert_version: alert('For security reasons, this version does not connect to the backend.'),
        // Alert_connection: alert('Thank you for your understanding, the full version of the program is detailed at: https://gitee.com/qian_zehao/nashsweeper'),
    },
    mounted() {
        // Alert_version(),
        // Alert_connection(),
    },
    created() {
        // Detect user device and redirect accordingly
        const userAgent = window.navigator.userAgent.toLowerCase();

        if (userAgent.match(/android|webos|iphone|ipod|blackberry|iemobile|opera mini/i)) {
            // Mobile or tablet device, redirect to mobile page
            console.log('This is mobile system');
            this.$router.push({ name: 'Mobile' });
        }
        else if (userAgent.match(/ipad/i)) {
            // Mobile or tablet device, redirect to mobile page
            console.log('This is iPad system');
            this.$router.push({ name: 'Pad' });
        }
        else {
            // Desktop or other devices, redirect to desktop page
            console.log('This is PC system');
            this.$router.push({ name: 'Desktop' });
        }
    }
}
</script>

<style scoped></style>