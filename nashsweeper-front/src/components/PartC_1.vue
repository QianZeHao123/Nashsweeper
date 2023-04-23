<template>
    <div>
        <h1 class="border">C-1</h1>
        <div>NEcounter:{{ NEcounter }}</div>
        <div>{{ time.hour }}:{{ time.minute }}:{{ time.second }}</div>
    </div>
</template>

<script>
import { NsStore } from '../store/index.js'
import { storeToRefs } from 'pinia'

export default {
    name: "PartC_1",
    components: {},
    data() {
        const store = NsStore()
        const { time, NEcounter } = storeToRefs(store)
        // const second = storeToRefs(store.time.second)
        return {
            time,
            NEcounter
        }
    },
    methods: {},
    mounted() { },
}
</script>

<style scoped></style>