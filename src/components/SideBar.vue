<template>
    <div>
        <div class="col-span-1">
            <div class="w-full border-4">
                <div class="h-32">
                    <div class="grid grid-cols-4 gap-1 h-15 p-3">
                        <div class="col-span-3 card-title">Nashswepper</div>
                        <button class="col-span-1 btn btn-sm">🔙</button>
                    </div>

                    <div class="flex justify-center items-center p-2">
                        <div class="btn-group">
                            <button class="btn btn-sm">Player</button>
                            <button class="btn btn-sm">Strategy</button>
                            <button class="btn btn-sm">Type</button>
                        </div>
                    </div>
                </div>
                <div class="flex justify-center items-center h-48 border-4">Part A</div>
                <div class="flex justify-center items-center h-10">
                    <button class="btn btn-sm btn-circle w-11/12 p-1">Solution</button>
                </div>
                <div class="flex justify-center items-center h-56 border-4">Part B</div>
                <div class="flex justify-center items-center h-10">
                    <button class="btn btn-sm btn-circle w-11/12 p-1">Solution Explorer</button>
                </div>
                <div class="flex justify-center items-center h-64 border-4">Part C</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "SideBar",
    components: {},
    data() {
        return {}
    },
    methods: {},
    mounted() { },
}
</script>
