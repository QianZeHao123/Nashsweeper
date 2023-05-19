<template>
    <div class="w-5/6">
        <!-- <div class="grid grid-rows-3 gap-x-4 gap-y-6 "> -->
        <div class="grid grid-rows-3 gap-x-4 gap-y-6 w-full">
            <div class="text-xl">
                <!-- <div class="border rounded-md p-2 bg-yellow-300">Time counter: 00::00::30</div> -->
                <TimeCounter />
            </div>
            <div class="text-xl w-full">
                <!-- <div class="border rounded-md p-2 bg-blue-500">Nash equilibrium counter: 0</div> -->
                <div class="btn w-full h-full border rounded-md p-2 bg-blue-800">Nash equilibrium
                    counter: {{ NEcounter }}
                </div>
            </div>
            <div class="text-xl">
                <!-- <div class="border rounded-md p-2 bg-green-500">Best response counter: 0</div> -->
                <div class="btn border rounded-md p-2 w-full h-full bg-green-800">
                    Best response counter: {{ BRcounter }}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import TimeCounter from './PartB_COM/TimeCounter.vue'
import { NsStore } from '../store/index.js'
import { storeToRefs } from 'pinia'

export default {
    name: "PartB",
    components: { TimeCounter },
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

<!-- <script setup>
import TimeCounter from './PartB_COM/TimeCounter.vue'
import { useCounterStore } from '../store/index.js'
import { storeToRefs } from 'pinia'
const store = useCounterStore()
const { count, double } = storeToRefs(store)

</script> -->

<style scoped></style>