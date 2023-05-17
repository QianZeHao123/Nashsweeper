<template>
    <div class="p-3">
        <div class="grid grid-rows-3 gap-y-2 ">
            <div class="text-xl">
                <!-- <div class="border rounded-md p-2 bg-yellow-300">Time counter: 00::00::30</div> -->
                <TimeCounter />
            </div>
            <div class="text-base">
                <!-- <div class="border rounded-md p-2 bg-blue-500">Nash equilibrium counter: 0</div> -->
                <div class="btn w-full h-full border rounded-md text-sm" v-on:click="increase_NEcounter()">Nash equilibrium
                    counter: {{ NEcounter }}
                </div>
            </div>
            <div class="text-xl">
                <!-- <div class="border rounded-md p-2 bg-green-500">Best response counter: 0</div> -->
                <div class="btn border rounded-md w-full h-full" v-on:click="increase_BestResponse()">
                    Best response counter: {{ BRcounter }}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import TimeCounter from './PartB_COM/TimeCounter.vue'
import TimeCounter from '../PartB_COM/TimeCounter.vue'
import { NsStore } from '../../store/index.js'
import { storeToRefs } from 'pinia'

export default {
    name: "PartB",
    components: { TimeCounter },
    data() {
        const store = NsStore();
        const { NEcounter, BRcounter } = storeToRefs(store)
        return {
            NEcounter,
            BRcounter
        }
    },
    methods: {
        increase_NEcounter: function () {
            this.NEcounter += 2
            console.log(this.NEcounter)
        },
        increase_BestResponse: function () {
            this.BRcounter++
            console.log(this.BRcounter)
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