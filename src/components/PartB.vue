<template>
    <div>
        <div class="grid grid-rows-3 gap-x-4 gap-y-6 ">
            <div class="text-xl">
                <!-- <div class="border rounded-md p-2 bg-yellow-300">Time counter: 00::00::30</div> -->
                <TimeCounter />
            </div>
            <div class="text-xl">
                <!-- <div class="border rounded-md p-2 bg-blue-500">Nash equilibrium counter: 0</div> -->
                <div class="border rounded-md p-2">Nash equilibrium counter: 0</div>
            </div>
            <div class="text-xl">
                <!-- <div class="border rounded-md p-2 bg-green-500">Best response counter: 0</div> -->
                <div class="border rounded-md p-2">Best response counter: 0</div>
            </div>
        </div>
    </div>
</template>

<script>
import TimeCounter from './PartB_COM/TimeCounter.vue'
export default {
    name: "PartB",
    components: { TimeCounter },
    data() {
        return {}
    },
    methods: {},
    mounted() { },
}
</script>

<style scoped>

</style>