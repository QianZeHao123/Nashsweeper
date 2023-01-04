<template>
    <div>
        <div class="text-xl flex justify-center items-center p-2">Rating of Nashsweeper players</div>
    </div>
    <div class="overflow-auto h-96">
        <table class="table-fixed w-full border-collapse">
            <thead>
                <tr>
                    <th class="w-1/4 border">Index</th>
                    <th class="w-1/4  border">Player ID</th>
                    <th class="w-1/4  border">Total strategies</th>
                    <th class="w-1/4  border">Time(s)</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="Player in PlayerInfo" v-bind:key="Player">
                    <td class="border">{{ Player.index }}</td>
                    <td class="border">{{ Player.PlayerID }}</td>
                    <td class="border">{{ Player.TotalStrategies }}</td>
                    <td class="border">{{ Player.Time }}</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div>
        <div class="text-xl flex justify-center items-center p-4">Request Data from Server</div>
    </div>
    <div class="flex justify-center items-center">
        <div class="grid grid-cols-2 gap-3 h-1/4">
            <div><a class="flex justify-center items-center btn btn-sm px-8"
                    href="http://127.0.0.1:6778/uploadfile">Request Data</a></div>
            <div><button class="flex justify-center items-center btn btn-sm px-8">Play Again</button></div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "PlayerRate",
    components: {},
    data() {
        return {
            PlayerInfo: [
                { index: 1, PlayerID: "TestNumber", TotalStrategies: 64, Time: 200 },
            ],
        }
    },
    methods: {
        getData: function () {
            var that = this;
            axios({
                method: 'get',
                url: '/backend/userrank'
            })
                .then(function (response) {
                    // 处理成功情况
                    console.log(response.data);
                    // that.items = response.data;
                    that.PlayerInfo = response.data;
                    // that.name = response.data.name;
                    // that.age = response.data.age;
                    // that.address = response.data.address;

                })
                .catch(function (error) {
                    // 处理错误情况
                    console.log(error);
                })
        },
    },
    mounted() {
        this.getData();
    },
}
</script>

<style scoped>

</style>