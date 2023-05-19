<template>
    <div>
        <!-- <h1 class="border">Part-A</h1> -->
        <div class="grid grid-rows-4">
            <div class="p-1 h-1/4">
                <div class="grid grid-cols-2 gap-3 p-1  h-1/4">
                    <div>
                        Strategies of player1
                    </div>
                    <div><input type="text" class="input-primary w-full max-w-xs" placeholder="Input your strategy"
                            inputmode="numeric" pattern="\d*" /></div>
                </div>
            </div>
            <div class="p-1  h-1/4">
                <!-- Strategies of player2 -->
                <div class="grid grid-cols-2 gap-3 p-1  h-1/4">
                    <div>
                        Strategies of player2
                    </div>
                    <div><input type="text" class="input-primary w-full max-w-xs" placeholder="Input your strategy"
                            inputmode="numeric" pattern="\d*" /></div>
                </div>
            </div>
            <div class="flex justify-center items-center border-4">
                <select class="select w-11/12 max-w-xs">
                    <option disabled selected>Select your game types</option>
                    <option>Prisoner Dilemma</option>
                    <option>Battle of the Sexes</option>
                    <option>Zero-Sum</option>
                    <option>Random</option>
                </select>
            </div>
            <div class="flex justify-center items-center">
                <div class="grid grid-cols-2 gap-3 h-1/4">
                    <div><a class="flex justify-center items-center btn btn-sm px-8 bg-slate-400"
                            href="http://198.74.121.61:803">Load Data</a></div>
                    <div><a class="flex justify-center items-center btn btn-sm px-8 bg-slate-400" href="https://gitee.com/qian_zehao">Export Data</a></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "PartA",
    components: {},
    data() {
        return {}
    },
    methods: {},
    mounted() { },
}
</script>

<style scoped>

</style>