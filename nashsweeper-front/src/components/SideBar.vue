<template>
    <div>
        <div class="col-span-1">
            <div class="w-full border-4">
                <div class="h-32">
                    <div class="grid grid-cols-4 gap-1 h-15 p-3">
                        <div class="col-span-3 card-title">Nashsweeper</div>
                        <button class="col-span-1 btn btn-sm">⇦</button>
                    </div>

                    <div class="flex justify-center items-center p-2">
                        <div class="btn-group">
                            <button class="btn btn-sm">Player</button>
                            <button class="btn btn-sm">Strategy</button>
                            <button class="btn btn-sm">Type</button>
                        </div>
                    </div>
                </div>
                <div class="flex justify-center items-center h-60 border-4">
                    <PartA />
                </div>
                <div class="flex justify-center items-center h-12">
                    <button class="btn btn-sm btn-circle w-11/12 p-1">Solution</button>
                </div>
                <div class="flex justify-center items-center h-56 border-4">
                    <PartB />
                </div>
                <div class="flex justify-center items-center h-12">
                    <button class="btn btn-sm btn-circle w-11/12 p-1">Solution Explorer</button>
                </div>
                <div class="flex justify-center items-center h-72 border-4">
                    <PartC />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import PartA from "./PartA.vue"
import PartB from "./PartB.vue"
import PartC from "./PartC.vue"

export default {
    name: "SideBar",
    components: { PartA, PartB, PartC },
    data() {
        return {}
    },
    methods: {},
    mounted() { },
}
</script>
