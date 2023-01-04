<template>
    <div>
        <ProjLink />
        <PlayerRate />
    </div>
</template>

<script>
import ProjLink from './PartE_COM/ProjLink.vue'
import PlayerRate from './PartE_COM/PlayerRate.vue'


export default {
    name: "PartE",
    components: {
        ProjLink,
        PlayerRate,
    },
    data() {
        return {

        }
    },
    methods: {},
    mounted() { },
}
</script>

<style scoped>

</style>