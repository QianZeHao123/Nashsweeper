<template>
    <div class=" h-full">
        <div class="grid grid-rows-6 h-full">

            <div class="flex justify-center items-center card-title">Nashsweeper ⇦ PC version</div>
            <div class="flex justify-center items-center">
                <div class="btn-group">
                    <button class="btn btn-sm">Player</button>
                    <button class="btn btn-sm bg-slate-400">Strategy</button>
                    <button class="btn btn-sm bg-slate-400">Type</button>
                </div>
            </div>
            <div>
                <div class="border flex p-2">
                    <input type="text" class="input-primary w-full max-w-xs" placeholder="Input Strategies of Player 1"
                        inputmode="numeric" pattern="\d*" />
                </div>
            </div>
            <div>
                <div class="border flex p-2">
                    <input type="text" class="input-primary w-full max-w-xs" placeholder="Input Strategies of Player 2"
                        inputmode="numeric" pattern="\d*" />
                </div>
            </div>
            <div class="h-full">
                <div class="flex justify-center items-center h-full">
                    <select class="select h-full border-4 w-full">
                        <option disabled selected>Select your game types</option>
                        <option>Prisoner Dilemma</option>
                        <option>Battle of the Sexes</option>
                        <option>Zero-Sum</option>
                        <option>Random</option>
                    </select>
                </div>
            </div>
            <div class="h-full w-full flex justify-center items-center">
                <div class="flex justify-center items-center">
                    <div class="grid grid-cols-2 gap-2">
                        <div><a class="flex justify-center items-center btn btn-sm px-8 bg-slate-400" href="">Load Data</a>
                        </div>
                        <div><a class="flex justify-center items-center btn btn-sm px-8 bg-slate-400" href="">Export
                                Data</a></div>
                    </div>
                </div>
            </div>
        </div>


    </div>
</template>

<script>
export default {
    name: "GameSetting",
    components: {},
    data() {
        return {}
    },
    methods: {},
    mounted() { },
}
</script>

<style scoped></style>