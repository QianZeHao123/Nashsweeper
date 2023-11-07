<template>
    <div class="flex justify-center items-center">
        <div class="w-11/12 overflow-auto">

            <div tabindex="0" class="collapse collapse-plus border border-base-300 bg-base-100 rounded-box">
                <div class="collapse-title text-xl font-medium">
                    View Game Log
                </div>
                <div class="collapse-content">
                    <div class="underline underline-offset-1">
                        <router-link :to="{ name: 'ViewLogs' }" target="_blank">
                            <div>View User Logs</div>
                        </router-link>
                    </div>
                    <!-- <div class="underline underline-offset-1" v-on:click="this.$router.push({ name: 'ViewResult' })">
                        View Results
                    </div> -->
                    <div class="underline underline-offset-1">
                        <router-link :to="{ name: 'ViewResult' }" target="_blank">
                            <div>View Results</div>
                        </router-link>
                    </div>
                    <!-- Open the modal using ID.showModal() method -->
                </div>

            </div>

            <div tabindex="0" class="collapse collapse-plus border border-base-300 bg-base-100 rounded-box">
                <div class="collapse-title text-xl font-medium">
                    Download Game Resources
                </div>
                <div class="collapse-content">
                    <div class="underline underline-offset-1"><a href="https://github.com/QianZeHao123/Nashsweeper"
                            target="_blank">Game Source Code</a></div>
                    <div class="underline underline-offset-1"><a
                            href="https://qianzehao123.github.io/files/NashsweeperUserManual.pdf"
                            target="_blank">Nashsweeper User Manual</a></div>
                    <div class="underline underline-offset-1"><a
                            href="https://qianzehao123.github.io/files/NashsweeperTech.pdf" target="_blank">Core Technology
                            and Details</a></div>
                    <div>Comming Soon!</div>
                </div>
            </div>


            <div tabindex="0" class="collapse collapse-plus border border-base-300 bg-base-100 rounded-box">
                <div class="collapse-title text-xl font-medium">
                    More Useful Links
                </div>
                <div class="collapse-content">
                    <div>Nashsweeper Solver (Comming Soon)</div>
                    <div class="underline underline-offset-1"><a href="mailto:qianzehao123@gmail.com"
                            target="_blank">Contact Author (Bug Report)</a></div>
                    <div>Comming Soon!</div>
                </div>
            </div>


        </div>
    </div>
</template>

<script>
export default {
    name: "GameOperation",
    components: {},
    data() {
        return {}
    },
    methods: {},
    mounted() { },
}
</script>

<style scoped></style>