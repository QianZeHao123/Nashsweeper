<template>

    <div class="col-span-3 h-full border-4">
        <div class="grid grid-rows-3 grid-cols-3 gap-2">
            <div class="flex justify-center items-center row-span-2 col-span-2 border-4">
                <PartD />
            </div>
            <div class="row-span-2 border-4">
                <PartE />
            </div>
            <div class="flex justify-center items-center h-80 border-4">
                <PartC_1 />
            </div>
            <div class="flex justify-center items-center h-80 border-4">
                <PartC_2 />
            </div>
            <div class="flex justify-center items-center h-80 border-4">
                <PartC_3 />
            </div>
        </div>
    </div>

</template>

<script>
import PartD from './PartD.vue'
import PartE from './PartE.vue'
import PartC_1 from './PartC_1.vue'
import PartC_2 from './PartC_2.vue'
import PartC_3 from './PartC_3.vue'
export default {
    name: "DataBarShow",
    components: { PartD, PartE, PartC_1, PartC_2, PartC_3 },
    data() {
        return {}
    },
    methods: {},
    mounted() { },
}
</script>

<style scoped>

</style>