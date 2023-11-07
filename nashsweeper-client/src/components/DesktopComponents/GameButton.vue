<template>
    <div class="h-full w-full">
        <div class="grid grid-rows-6 h-full w-full">
            <div class="row-span-1 h-full w-full flex justify-center items-center">
                <button class="btn btn-sm btn-circle w-11/12 p-1">Solution</button>
            </div>

            <div class="row-span-4 p-1">
                <div class="grid grid-rows-3 h-full gap-2">
                    <div class="h-full w-full">
                        <TimeCounter />
                    </div>
                    <div class="btn w-full h-full border rounded-md bg-blue-800">Nash equilibrium
                        counter: {{ NEcounter }}
                    </div>
                    <div class="btn w-full h-full border rounded-md bg-green-800">Best response counter: {{ BRcounter }}
                    </div>
                </div>
            </div>

            <div class="row-span-1 h-full w-full flex justify-center items-center">
                <button class="btn btn-sm btn-circle w-11/12 p-1">Solution Explorer</button>
            </div>

        </div>
    </div>
</template>

<script>
import TimeCounter from "./GamebtnComponents/TimeCounter.vue"
import { NsStore } from '../../store/index.js'
import { storeToRefs } from 'pinia'

export default {
    name: "GameButton",
    components: {
        TimeCounter,
    },
    data() {
        const store = NsStore();
        const { NEcounter, BRcounter } = storeToRefs(store)
        return {
            NEcounter,
            BRcounter,
        }
    },
    methods: {
        increase_NEcounter: function () {
            this.NEcounter += 2
            console.log(this.NEcounter)
        },
        increase_BestResponse: function () {
            this.BestResponse++
            console.log(this.BestResponse)
        }
    },
    mounted() { },
}
</script>

<style scoped></style>